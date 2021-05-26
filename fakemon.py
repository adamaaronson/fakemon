import markov
import random
from wordfilter import Wordfilter

MIN_LEN = 4
MAX_LEN = 12
POKEDEX = open('txt/pokemon.txt').read().splitlines()
TYPES = open('txt/types.txt').read().splitlines()
ABILITIES = open('txt/abilities.txt').read().splitlines()

filter = Wordfilter()

class Fakemon:
    def __init__(self, name=''):
        self.name = name
        self.type1 = None
        self.type2 = None
        self.ability = None
    
    def __str__(self):
        type_str = f'{self.type1}/{self.type2}' if self.type2 else self.type1
        return f'A wild {self.name} appeared!\n- Type: {type_str}\n- Ability: {self.ability}'

def generate_fakemon():
    fakemon = Fakemon()

    # generate name, assuring it contains no bad words
    while True:
        fakemon.name = markov.generate_word_from(POKEDEX, minlen=MIN_LEN, maxlen=MAX_LEN)
        if not filter.blacklisted(fakemon.name) and fakemon.name not in POKEDEX:
            break
    
    # generate types
    if random.randrange(2) == 1:
        fakemon.type1, fakemon.type2 = random.sample(TYPES, 2)
    else:
        fakemon.type1 = random.choice(TYPES)

    # generate ability
    fakemon.ability = random.choice(ABILITIES)

    return fakemon