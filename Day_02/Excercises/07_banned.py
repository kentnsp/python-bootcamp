banned_words = ['moist','break','raise']

user_input = input('Enter word: ')

has_banned_word = user_input in banned_words
if has_banned_word:
    print('Banned')
else:
    print('OK')

#SAMPLE 2
if user_input in ('moist','break','raise'):
    print('sample 2')