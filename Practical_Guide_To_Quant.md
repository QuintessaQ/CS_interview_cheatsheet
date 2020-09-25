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

### chess tournament
- conditional probablity approach
    - each player has 1/(2^n-1) of meeting player 1
    - 1 and 2 do not meet in round 1 has probablity (2^n-2)/(2^n-1)
    - 1 and 2 do not meet in round 2 has probablity (2^{n-1}-2)/(2^{n-1}-1)
    - multiply together, get 2^{n-1}/(2^n-1)
- counting approach
    - 1 and 2 must be in different subgroup
    - 2^{n-1}/(2^n-1)

### application letters
- let E_i be the event that envelop i is correct
- P(E_i) = 1/5
- P(E_iE_j) = 1/5 * 1/4
- \sum P(E_iE_j) = 10 * 1/5 * 1/4 = 1/2
- P(E_iE_jE_k) = 1/5 * 1/4 * 1/3
- \sum P(E_iE_jE_k) = \binom(5, 3) * 1/5 * 1/4 * 1/3 = 1/3!
- 1 - 1/2 + 1/3! - 1/4! + 1/5!

### birthday problem
- Pr(nobody has the same birtyday) < 1/2
- 365 * 364 * ... * (365-n+1)/365^n < 1/2

### 100th digit
- binom theorem: (x + y)^n = \sum_{k=0}{n} \binom(n, k) x^k y^{n-k}
- calculate (1-\sqrt(2))^n and (1+\sqrt(2))^n and add together, must be an integer
- 0 < (1-\sqrt(2))^3000 <<10^{-100}

### cubic of integer
- x = a + 10b
- x^3 = (a + 10b)^3 = a^3 + 30a^2b + 300ab^2 + 1000b^3
- last digit of x^3 depends on a^3, a = 1
- second to last digit of x^3 depends on 30a^2b = 30b, 3b = 1, thus b = 7
- prob = 1/100

### boys and girls
- part A
    - A = everyone has >= son
    - B = both are boys
    - {bb, bg, gb, gg}
    - Pr = 1/3

- part B
    - 1/2

