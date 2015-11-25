-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--1. Connect to the tournament database

\c tournament;

--2. Drop tables first (if they exist)

DROP VIEW IF EXISTS playerStandings;
DROP TABLE IF EXISTS match;
DROP TABLE IF EXISTS player;

--3. Create tables

CREATE TABLE player (
	id serial PRIMARY KEY,
	name varchar(50) NOT NULL
);

CREATE TABLE match (
	id serial PRIMARY KEY,
	winner integer NOT NULL REFERENCES player (id),
	loser integer NOT NULL REFERENCES player (id)
);


--4. Create a view which returns the player standings

CREATE VIEW playerStandings AS
	SELECT	p.id,
			p.name,
			COUNT(m1.winner) as wins,
			COUNT(m2.id) as matches,
			COUNT(m3.id) as OMW -- oppenent match wins
	FROM player p
	-- this join helps count a player's wins
	LEFT JOIN match m1 ON p.id = m1.winner
	-- this join helps count a player's total matches
	LEFT JOIN match m2 ON p.id = m2.winner OR p.id = m2.loser
	-- this join helps count a player's opponents' wins (OMW)
	LEFT JOIN match m3 ON
		(m2.loser != p.id AND m2.loser = m3.winner)
		OR
		(m2.winner != p.id AND m2.winner = m3.winner)
	GROUP BY p.id, p.name
	-- EXTRA CREDIT:
	-- if two players have same wins then they will be
	-- sorted by whoever has oppenents with more wins
	ORDER BY wins DESC, OMW DESC;
