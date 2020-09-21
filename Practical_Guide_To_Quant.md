## Chapter 2 Brain Teasers
- starts with a simplified version
### Screwy pirates
- 100 coins divided to 5 pirates
- 2 pirates, a and b
    - b proposes: b gets 100, a gets 0
- 3 pirates, a, b, c
    - a will supports c no matter what
    - a: 1, b: 0, c: 99
- 4 pirates, abcd
    - b supports d
    - a: 0, b: 1, c: 0, d: 99
- 5 pirates, abcde
    - a: 1, b: 0, c: 1, d: 0, e: 98

### Tiger and sheep
- 1 tiger, 1 sheep
    - eat
- 2 tigers, ab
    - not eat
- 3 tigers, abc
    - a eats
- 4 tigers, abcd
    - if a eats, then 2 sheep, bcd
        - if b eats, then 3 sheep, cd
            - not eating then
    - a won't eat
- 100 tiger, not eat

### River crossing
- CD cross, D back, 3min
- AB cross, C back, 2
- CD cross, 2min


### Card game
- 2 cards

### Defective ball
- 4 + 4 + 4

### Horse race
- 5 groups, 5 races, have orderibg in each group
- pick tops from each group, 1 race, then 3 groups have potential answers, 3+2+1 candidates
- race  1,2,3,6,7, then add 11 and race 

## Chapter 4 Probablity Theory
### Coin toss game
- remove one coin from A
- E1: A more coins
- E2: equal coins
- E3: A fewer coins
- P(E1) = P(E2) = x, then 2x + y = 1
- result = x + y/2 = 0.5

### Card game
- 1/13 + 1/13 * 48/52 + 1/13 * 44/52...
= 1/(13*52) * (0 + 4 + 8 + ... + 48) 
=  1/(13*52) * (4 + 48) * 13 /2
= 24/52
= 8/17


### Drunk passenger
- E1: seat #1 taken before #100
- E2: seat #100 taken before #1

### N point on a circle
- 1/2^{N-1} chance that all 2, ..., N points in the same semi-circle
- same for all i
- N * 1/2^{N-1} 

### poker hands
- four-of-a-hand: 13 * 48
- full house: 13 * 12 * 4 * 6
- hand with two pairs: 13 * 6 * 6 * 6 * 44

### hopping rabbit
- stair(1) = 1
- stair(2) = 2
- stair(n) = stair(n-1) + stair(n-2)

### screwy pirates
- for each random group of 5, there must be a lock that none of them has the key to, yet all other 6 pirates have the key
- number of locks = \binom(11,5)
- each lock has 6 keys, each pirate has \binom(11,5) * 6 / 11
