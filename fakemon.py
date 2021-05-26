import markov
import random
from wordfilter import Wordfilter

MIN_LEN = 4
MAX_LEN = 12
POKEDEX = open('txt/pokemon.txt').read().splitlines()
TYPES = open('txt/types.txt').read().splitlines()
ABILITIES = open('txt/abilities.txt').read().splitlines()
STATS = ['HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe']

filter = Wordfilter()

class Fakemon:
    def __init__(self, name=''):
        self.name = name
        self.type1 = None
        self.type2 = None
        self.ability = None
        self.stats = {}
    
    def __str__(self):
        type_str = f'{self.type1}/{self.type2}' if self.type2 else self.type1
        stats_str = '\n- '.join([f'{stat}: {self.stats[stat]}' for stat in STATS])
        # stats_str = ', '.join([f'{self.stats[stat]} {stat}' for stat in STATS]) + f' ({sum(self.stats.values())} total)'
        return_str = f'A wild {self.name} appeared!\n- Type: {type_str}\n- Ability: {self.ability}\n- {stats_str}'
        return return_str

def generate_fakemon():
    fakemon = Fakemon()

    # generate name, assuring it contains no bad words
    while True:
        reqlen = len(random.choice(POKEDEX))
        fakemon.name = markov.generate_word_from(POKEDEX, minlen=reqlen, maxlen=reqlen)
        if not filter.blacklisted(fakemon.name) and fakemon.name not in POKEDEX:
            break
    
    # generate types
    if random.randrange(2) == 1:
        fakemon.type1, fakemon.type2 = random.sample(TYPES, 2)
    else:
        fakemon.type1 = random.choice(TYPES)

    # generate ability
    fakemon.ability = random.choice(ABILITIES)

    # generate stats
    fakemon.stats = {stat : random.choice([random.randrange(50, 101), random.randrange(40, 161)]) for stat in STATS}

    return fakemon