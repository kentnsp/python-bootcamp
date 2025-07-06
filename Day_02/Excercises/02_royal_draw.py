ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

ranks[-4] = 'Drawn'
ranks[-3] = 'Drawn'
ranks[-2] = 'Drawn'
ranks[-1] = 'Drawn'
ranks[0] = 'Drawn'

print(ranks)

for rank in ranks:
    if rank == '10' or 'J' or 'K' or 'Q' or 'A'  or '0':
        rank = 'Drawn'

print(ranks)