coordinates = [
    (x,y,z)
        for x in range(10)
        for y in range(10)
        for z in range(10)
]

print(coordinates)

ranks = ["A","1","2","10","K","Q"]
suits = ["Hearts", "Spades","Diamond"]

deck = [(rank, suit) for rank in ranks for suit in suits]

print(deck)