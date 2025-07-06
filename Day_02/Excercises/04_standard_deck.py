from itertools import product

ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

for suit in suits:
    for rank in ranks:
        print(f'{rank} of {suit}')


for rank, suit in product(ranks, suits):
    print(rank, suit)