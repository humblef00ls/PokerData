# Poker Hand Analyser Library for Project Euler: Problem 54
from collections import namedtuple
import functools
from itertools import combinations
import pe_lib
import pandas as pd
import re


suits = "HDCS".split()
faces = "2,3,4,5,6,7,8,9,T,J,Q,K,A"
face = faces.split(',')

class Card(namedtuple('Card', 'face, suit')):
	def __repr__(self):
		return ''.join(self)

def royal_flush(hand):

    royalface = "TJQKA"
    # sort the cards based on the face rank of each card
    ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))
    first_card = ordered[0]
    other_cards = ordered[1:]

	# check if all are of the same suit
    if all(first_card.suit == card.suit for card in other_cards):
		# check if they are in sequential order
		# compare the ordered faces substring with the face list (which is converted to string)
	    if ''.join(card.face for card in ordered) in royalface:
		    return 'royal-flush', ordered[-1].face
    return False

def straight_flush(hand):
	# sort the cards based on the face rank of each card
	ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))

	first_card = ordered[0]
	other_cards = ordered[1:]

	# check if all are of the same suit
	if all(first_card.suit == card.suit for card in other_cards):
		# check if they are in sequential order
		# compare the ordered faces substring with the face list (which is converted to string)
		if ''.join(card.face for card in ordered) in ''.join(face):
			return 'straight-flush', ordered[-1].face
	return False

def four_of_a_kind(hand):
	allfaces = [f for f,s in hand]
	
	# create a unique set of ranks
	uniqueRanks = set(allfaces)

	# if there are more than 2 ranks, it's not four of a kind
	if len(uniqueRanks) != 2:
		return False

	for f in uniqueRanks:
		# if there are 4 faces, it is four of a kind
		if allfaces.count(f) == 4:
			uniqueRanks.remove(f)
			return "four-of-a-kind", f

	return False

def full_house(hand):
    allfaces = [f for f,s in hand]

    rankFrequency = pe_lib.character_frequency(allfaces)

	# if there are 2 types of ranks and there's a card with 1 pair and 3 of a kind
    

    rankFrequency = list({k: v for k, v in sorted(rankFrequency.items(), key=lambda item: item[1])})
    if len(rankFrequency) == 2 and (rankFrequency[0] == 2 and rankFrequency[1] == 3):
        return 'full-house'
    
    return False

def flush(hand):
	allfaces = [f for f,s in hand]

	first_card = hand[0]
	other_cards = hand[1:]

	if all(first_card.suit == card.suit for card in other_cards):
		return 'flush', sorted(allfaces, key=lambda f: face.index(f), reverse=True)

	return False

def straight(hand):
	ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))
	if ''.join(card.face for card in ordered) in ''.join(face):
		return 'straight', ordered[-1].face
	return False;

def three_of_a_kind(hand):
	allfaces = [f for f,s in hand]

	uniqueRanks = set(allfaces)

	if len(uniqueRanks) != 3:
		return False

	for f in uniqueRanks:
		if allfaces.count(f) == 3:
			uniqueRanks.remove(f)
			return "three-of-a-kind", f

	return False;

def two_pair(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)
	
	# collect pairs
	pairs = [f for f in allftypes if allfaces.count(f) == 2]
	
	# if there are more than two pairs
	if len(pairs) != 2:
		return False

	p1, p2 = pairs
	# get the difference using sets
	other_cards = [(allftypes - set(pairs)).pop()]
	return 'two-pair', pairs + other_cards if(face.index(p1) > face.index(p2)) else pairs[::-1] + other_cards

def one_pair(hand):
	allfaces = [f for f,s in hand]
	allftypes = set(allfaces)

	# collect pairs
	pairs = [f for f in allftypes if allfaces.count(f) == 2]

	# if there's more than one pair
	if len(pairs) != 1:
		return False

	allftypes.remove(pairs[0])
	return 'one-pair', pairs + sorted(allftypes, key=lambda f: face.index(f), reverse=True)

def high_card(hand):
	# collect all faces from each card
	allfaces = [f for f,s in hand]

	#sort the faces and show the highest card
	return "high_card", sorted(allfaces, key=lambda f: allfaces.index(f), reverse=True)[0] 

def create_hand_tuple(cards = "5D 8C 9S JS AC"):
	hand = []

	for card in cards.split():
		face, suit = card[:-1], card[-1]
		hand.append(Card(face, suit))

	return hand;

# functions
handrankorder = (royal_flush,straight_flush,four_of_a_kind,full_house,
				flush,straight,three_of_a_kind,two_pair,
				one_pair,high_card)

def determine_rank(cards = "TS JH QH KH AH"):
	hand = create_hand_tuple(cards)
	for ranker in handrankorder:
		rank = ranker(hand)

		if rank:
			break
	return rank



datax = pd.read_csv('out/extractedBDF.csv')
datax['WIN'] = datax['net_earning'] >  0 
datax['T_CARDS'] =  datax['player_cards']+datax['community_cards']
datax['T_CARDS'] = datax['T_CARDS'].apply(lambda x: " ".join(re.findall('..',x.upper())))



cardmapx = {
    'high_card':1,
    'one-pair':2,
    'two-pair':3,
    'three-of-a-kind':4,
    'straight':5,
    'flush':6,
    'full-house':7,
    'four-of-a-kind':8,
    'straight-flush':9,
    'royal-flush':10
}
valmapx = {

    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14

}

aggr = []






for index, row in datax.iterrows():
	rc = row['T_CARDS'].split(' ')
	vx = list(combinations(rc,5))

	lx = [determine_rank(" ".join(i)) for i in vx]

	#lx = list(map(lambda x: (x[0], functools.reduce(lambda t,x : t + valmapx[x], x[1],0) ), lx))
	lx = sorted(lx, key=lambda x: (cardmapx[x[0]],valmapx[x[1]] if type(x[1]) != list else functools.reduce(lambda t,x : t + valmapx[x], x[1],0))    ,reverse=True)

	aggr.append(lx[0])

	if index % 5000 == 0 :
   		print(index)

#6 failed extractions total
datax['best_hand'] = aggr 

print(datax)

datax.to_csv('out/extractedBDF_best_hand.csv')

