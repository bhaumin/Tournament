Tournament Results
----------------------

This application allows you to verify the functioning of a swiss pair tournament between an even number of players.

It contains the following files.
--------------------------------------------
1 - tournament.sql
	This file contains the scripts to create the database tables and views.

2 - tournament.py
	This is the main file which implements the swiss-pair tournament functionality.

3 - tournament_test.py
	This file contains unit tests that will test the functions written in tournament.py.

4 - README.txt


How to run the application.
---------------------------
You need to have installed python 2.7.6 and psql (PostgreSQL) 9.3.10 in your machine.

1 - In terminal/cmd, navigate to the directory where the files are located.
2 - Run the command line "psql -f tournament.sql" which will run the attached script file and create the database and all the necessary database objects.
3 - Run the unit test file by the command "python tournament_test.py" which will run all the unit tests which will verify the functionality of the swiss-pair tournament rules.

You should see the following output:

1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!


Copyright: Udacity
Author: Bhaumin Shah
Date: Nov 24, 2015
