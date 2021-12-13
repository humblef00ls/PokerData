# CompSci 216 Project

We are analyzing poker data compiled from online poker sites to determine the best strategies for bringing home the bacon.


## Code
Currently, the data extraction script `extractor.py` looks through all the players who partook in holdem games in a given year and month. Right now we are only looking at one month for one kind of holdem game. Also we have restricted the data for now to only hands of players which did not fold in that hand, as data about their actual cards is only availiable for those players. The result of this extractive is a CSV file with columns ` player_name     hand_id starting_bankroll  net_earning player_cards play_cards_value community_cards`, located at `out/extracted.csv`. To run it yourself:

```
source ./vm/bin/activate
pip install -r requirements.txt
python extractor.py
```

NOTE: The output files exceeded github's limit of 100mb and thus are not in this repo.