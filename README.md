# fakemon

**[Who's That Fakemon?](https://twitter.com/whosthatfakemon)** is a Twitter bot that tweets randomly generated fake Pokémon, or Fakemon. The Fakemon are completely random in every way, even down to the letters in their names.

Created by Adam Aaronson for fun in 2021, this bot is not affiliated with the Pokémon Company, Game Freak, or Nintendo.

## Names

Fakemon names are generated using a Markov chain modeled after all 898 existing Pokémon names. In other words, the probability of each letter appearing is weighted by how often the letter appears after the previous letter in Pokémon names. Name length is also randomly selected, weighted by the lengths of existing Pokémon names.

Names are automatically filtered using the [wordfilter](https://github.com/dariusk/wordfilter) module to ensure they don't contain any offensive slurs.

## Types and abilities

Fakemon types and abilities are randomly selected from the lists of existing Pokémon types and abilities. Fakemon can be either single-typed or dual-typed, with equal probability.

## Stats

Fakemon stats (HP, Attack, Defense, Sp. Atk, Sp. Def, and Speed) are randomly chosen on a scale from 25 to 160, with greater weight given to values from 50 to 100. This gives Fakemon an average base stat total of roughly 500.