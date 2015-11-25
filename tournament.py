#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect(database_name="tournament"):
    try:
        """Connect to the PostgreSQL database.  Returns a database connection."""
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Could not connect to the database {}".format(database_name))


def deleteMatches():
    """Remove all the match records from the database."""
    conn, c = connect()

    c.execute("DELETE from match;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn, c = connect()

    c.execute("DELETE from player;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn, c = connect()

    c.execute("SELECT COUNT(*) AS player_count from player;")
    player_count = c.fetchone()[0]

    conn.commit()
    conn.close()

    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    conn, c = connect()

    sql = "INSERT INTO player (name) VALUES (%s);"
    c.execute(sql, (name,))

    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn, c = connect()

    c.execute("SELECT id, name, wins, matches from playerStandings;")
    standings = c.fetchall()

    conn.commit()
    conn.close()

    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn, c = connect()

    sql = "INSERT INTO match (winner, loser) VALUES (%s, %s);"
    c.execute(sql, (winner, loser))

    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    # Initialize the counter to 0, so we can pair the consecutive players
    i = 0

    # Intialize the swiss_pair to an empty list
    swiss_pair = []

    # check if there are even number of players
    if countPlayers() % 2 == 0:
        # First get the latest standings of all players
        standings = playerStandings()

        # Loop over the standings and pair up each adjacent players and append
        # them to the swiss pairs list
        for s in standings:
            if i % 2 == 0:
                player1 = (s[0], s[1])
            else:
                player2 = (s[0], s[1])
                pair = player1 + player2
                swiss_pair.append(pair)

            i = i + 1

    return swiss_pair
