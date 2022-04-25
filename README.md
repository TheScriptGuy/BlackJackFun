# Black Jack Fun
This is my attempt to create a Black Jack game. From this I calculate the potential win rate based over a certain number of games.

There are 2 options
* play games with a single process `letsplay-sp.py` 
* play games with multiple processes `letsplay-mp.py`


## Single Process
This python script will iterate through however many games and calculate the player win rate

```bash
$ python3 letsplay-sp.py
Number of Players: 5, Number of Decks: 5, Number of Games: 1000, Player win rate: 83.29
```

## Multiple Processes
Got multiple processors? Let's have some fun!

This is my first attempt at using multiple processes to get through more games in a quicker amount of time!

To run:
```bash
$ python3 letsplay-mp.py
Process ID: 26691, Number Of Players: 3, Number of Decks: 2, Number of Games: 38152
Process ID: 26692, Number Of Players: 3, Number of Decks: 2, Number of Games: 14274
Process ID: 26693, Number Of Players: 4, Number of Decks: 5, Number of Games: 54625
Process ID: 26694, Number Of Players: 6, Number of Decks: 8, Number of Games: 30336
Process ID: 26695, Number Of Players: 3, Number of Decks: 5, Number of Games: 24212
Process ID: 26696, Number Of Players: 4, Number of Decks: 7, Number of Games: 14998
Process ID: 26698, Number Of Players: 2, Number of Decks: 7, Number of Games: 25287
Process ID: 26704, Number Of Players: 5, Number of Decks: 8, Number of Games: 85249
Process ID: 26699, Number Of Players: 6, Number of Decks: 8, Number of Games: 24690
Process ID: 26702, Number Of Players: 2, Number of Decks: 5, Number of Games: 39869
Process ID: 26706, Number Of Players: 4, Number of Decks: 6, Number of Games: 22116
Process ID: 26709, Number Of Players: 3, Number of Decks: 6, Number of Games: 34889
Process ID: 26719, Number Of Players: 5, Number of Decks: 3, Number of Games: 58587
Process ID: 26713, Number Of Players: 6, Number of Decks: 3, Number of Games: 59504
Process ID: 26717, Number Of Players: 2, Number of Decks: 2, Number of Games: 44912
Process ID: 26720, Number Of Players: 5, Number of Decks: 5, Number of Games: 37431
Process ID: 26715, Number Of Players: 5, Number of Decks: 7, Number of Games: 80667
Process ID: 26711, Number Of Players: 4, Number of Decks: 2, Number of Games: 81829
Process ID: 26722, Number Of Players: 3, Number of Decks: 2, Number of Games: 24060
Process ID: 26723, Number Of Players: 2, Number of Decks: 8, Number of Games: 66174
Process ID: 26692, Player win rate: 81.73
Process ID: 26722, Player win rate: 81.95
Process ID: 26691, Player win rate: 82.01
Process ID: 26696, Player win rate: 80.63
Process ID: 26717, Player win rate: 81.66
Process ID: 26706, Player win rate: 81.10
Process ID: 26695, Player win rate: 81.90
Process ID: 26698, Player win rate: 80.81
Process ID: 26702, Player win rate: 80.54
Process ID: 26711, Player win rate: 80.57
Process ID: 26709, Player win rate: 81.86
Process ID: 26699, Player win rate: 80.48
Process ID: 26720, Player win rate: 80.89
Process ID: 26719, Player win rate: 81.44
Process ID: 26713, Player win rate: 81.38
Process ID: 26694, Player win rate: 81.47
Process ID: 26693, Player win rate: 80.58
Process ID: 26723, Player win rate: 81.03
Process ID: 26715, Player win rate: 80.95
Process ID: 26704, Player win rate: 81.86
Total Player Wins: 1394162
Total Dealer Wins: 1716654
Total Games Played: 861861
Overall player win rate: 81.214
```

