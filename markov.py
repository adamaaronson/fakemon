from random import uniform

def increment_dict(dict, a, b):
    if a in dict:
        if b in dict[a]:
            dict[a][b] += 1
        else:
            dict[a][b] = 1
    else:
        dict[a] = {}
        dict[a][b] = 1

def markov_chain(wordlist):
    chain = {}
    for w in wordlist:
        if len(w) == 0:
            continue
        for i in range(len(w) + 1):
            if i == 0:
                increment_dict(chain, '^', w[i])
            elif i == len(w):
                increment_dict(chain, w[i - 1], '$')
            else:
                increment_dict(chain, w[i - 1], w[i])

    for letter1 in chain:
        total = 0
        for letter2 in chain[letter1]:
            total += chain[letter1][letter2]
        for letter2 in chain[letter1]:
            chain[letter1][letter2] /= total

    return chain

def weighted_random_key(dict):
    rand = uniform(0, 1)
    total = 0
    for k in dict:
        total += dict[k]
        if total > rand:
            return k
    return None

def generate_word_from(wordlist, minlen=0, maxlen=float("inf")):
    chain = markov_chain(wordlist)
    word = ''

    while True:
        next_char = weighted_random_key(chain['^'])
        word += next_char
        while not word.endswith('$'):
            next_char = weighted_random_key(chain[word[-len(next_char):len(word)]])
            word += next_char
        word = word[:-1]

        if len(word) >= minlen and len(word) <= maxlen:
            break
        else:
            word = ''

    return word
