# Chapter 4 Probability Theory
- Chances are that you will face at least a couple of probability problems in most quantitative interviews. Probability theory is the foundation of every aspect of quantitative finance. As a result, it has become a popular topic in quantitative interviews.
- Although good intuition and logic can help you solve many of the probability problems, having a thorough understanding of basic probability theory will provide you with clear and concise solutions to most of the problems you are likely to encounter. Furthermore, probability theory is extremely valuable in explaining some of the seemingly-counterintuitive results. Armed with a little knowledge, you will find that many of the interview problems are no more than disguised textbook problems.
- So we dedicate this chapter to reviewing basic probability theory that is not only broadly tested in interviews but also likely to be helpful for your future career. The knowledge is applied to real interview problems to demonstrate the power of probability theory. Nevertheless, the necessity of knowledge in no way downplays the role of intuition and logic. Quite the contrary, common sense and sound judgment are always crucial for analyzing and solving either interview or real-life problems. As you will see in the following sections, all the techniques we discussed in Chapter 2 still play a vital role in solving many of the probability problems.
- Let's have some fun playing the odds.

## 4.1 Basic Probability Definitions and Set Operations
- First let's begin with some basic definitions and notations used in probability. These definitions and notations may seem dry without examples—which we will present momentarily—yet they are crucial to our understanding of probability theory. In addition, it will lay a solid ground for us to systematically approach probability
problems.
- Outcome (w)
    - the outcome of an experiment or trial.
- Sample space/Probability space (0)
    - the set of all possible outcomes of an experiment.
- Event
    - A set of outcomes and a subset of the sample space. 

### **Coin toss game**
- Two gamblers are playing a coin toss game. Gambler A has (n + 1) fair coins; B has n fair coins. What is the probability that A will have more heads than B if both flip all their coins? 
- Hint: What are the possible results (events) if We compare the number of heads in A's first 17 coins with B's n coins? By making the number of coins equal, we can take advantage of symmetry. For each event, what will happen if A's last coin is a head? Or a tail?

- Solution
    - We have yet to cover all the powerful tools probability theory offers. What do we have now? Outcomes, events, event probabilities, and surely our reasoning capabilities! The one extra coin makes A different from B. If we remove a coin from A, A and B will become symmetric. Not surprisingly, the symmetry will give us a lot of nice properties. So let's remove the last coin of A and compare the number of heads in A's first n coins with B's n coins. There are three possible outcomes:
    - E1
        - A's n coins have more heads than B's n coins;
    - E2 
        - A's n coins have equal number of heads as B's n coins;
    - E3
        - A's ii coins have fewer heads than B's n coins.
    - By symmetry, the probability that A has more heads is equal to the probability that B has more heads. So we have P(E1)= P(E3). Let's denote P(E1) = P(E3)= x and P(E2) = y. Since \sum_{w \in \Omega} P(w) = 1, we have 2x + y = 1. For event E1, A will always have more heads than B no matter what A's (n+1)th coin's side is; for event E3 , A will have no more heads than B no matter what A's (n +1)th coin's side is. For event E2, A's (n+1)th coin does make a difference. If it's a head, which happens with probability 0.5, it will make A have more heads than B. So the (n + 1)th coin increases the probability that A has more heads than B by 0.5y and the total probability that A has more heads is x + 0.5y = x + 0.5(1 - 2x) = 0.5 when A has (n + 1) coins.

### **Card game**
- A casino offers a simple card game. There are 52 cards in a deck with 4 cards for each value 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A . Each time the cards are thoroughly shuffled (so each card has equal probability of being selected). You pick up a card from the deck and the dealer picks another one without replacement. If you have a larger number, you win; if the numbers are equal or yours is smaller, the house wins- as in all other casinos, the house always has better odds of winning. What is your probability of winning?
- Solution
    - One answer to this problem is to consider all 13 different outcomes of your card. The card can have a value 2, 3, ..., A and each has 1/13 of probability. With a value of 2, the probability of winning is 0/51; with a value of 3, the probability of winning is 4/51 (when the dealer picks a 2); ...; with a value of A. the probability of winning is 48/51 (when the dealer picks a 2, 3, ..., or K). So your probability of winning is
        - 1/13 * (0/51 + 4/51 + ... + 48/51) = 4/(13 * 51) * (0 + 1 + ... + 12) = 4/(13 * 51) * (12 * 13)/2 = 8/17
    - Although this is a straightforward solution and it elegantly uses the sum of an integer sequence, it is not the most efficient way to solve the problem. If you have got the core spirits of the coin tossing problem, you may approach the problem by considering three different outcomes:
        - E1 : Your card has a number larger than the dealer's;
        - E2: Your card has a number equal to the dealer's;
        - E3: Your card has a number lower than the dealer's.
    - Again by symmetry, P(E1) = P(E3). So we only need to figure out P(E2), the
probability that two cards have equal value, Let's say you have randomly selected a card. Among the remaining 51 cards, only 3 cards will have the same value as your card. So the probability that the two cards have equal value is 3/51. As a result, the probabillty that you win is P(E1) = (1 - P(E2))/2 = (1-3/51)/2 = 8/17

### **Drunk passenger**
- A line of 100 airline passengers are waiting to board a plane. They each hold a ticket to one of the 100 seats on that flight. For convenience, let's say that the n-th passenger in line has a ticket for the seat number n. Being drunk, the first person in line random seat (equally likely for each seat). All of the other passengers are sober, and will go to their proper seats unless it is already occupied; In that ease, they will randomly choose a free seat. You're person number 100. What is the probability that you end up in your seat (i.e. seat #100)
- Solution
    - Let's consider seats #1 and #100. There are two possible outcomes:
        - E1 Seat #1 is taken before #100;
        - E2 : Seat #100 is taken before #1.
    - If any passenger takes seat #100 before #1 is taken, surely you will not end up in you own seat. But if any passenger takes #1 before #100 is taken, you will definitely end up in you own seat. By symmetry, either outcome has a probability of 0.5. So the probability that you end up in your seat is 50%.
    - In case this over-simplified version of reasoning is not clear to you, consider the following detailed explanation: If the drunk passenger takes #1 by chance, then it's clear all the rest of the passengers will have the correct seats. If he takes #100, then you will not get your seat. The probabilities that he takes #1 or #100 are equal. Otherwise assume that he takes the n-th seat, where n is a number between 2 and 99. Everyone between 2 and (n-1) will get his own seal. That means the n-th passenger essentially becomes the new "drunk" guy with designated seat #1. If he chooses #1, all the rest of the passengers will have the correct seats. If he takes #100, then you will not get your seat. (The probabilities that he takes 41 or #100 are again equal.) Otherwise he will just make another passenger down the line the new "drunk" guy with designated seat #1 and each new "drunk" guy has equal probability of taking #1 or #100. Since at all jump points there's an equal probability for the "drunk" guy to choose seat #1 or #100, by symmetry, the probability that you, as the 100-th passenger, will seat in #100 is 0.5.
    
### **N points on a circle**
- Given N points drawn randomly on the circumference of a circle, what is the probability that they are all within a semicircle?
- Hint: Consider the events that starting from a point it, you can reach all the rest of the points on the circle clockwise, n \in {1,...,N} in a semicircle. Are these events mutually exclusive?

- Solution
    - Let's start at one point and clockwise label the points as 1, 2, ..., N. The probability that all the remaining N — 1 points from 2 to N are in the clockwise semicircle starting at point 1 (That is, if point 1 is at 12:00, points 2 to N are all between 12:00 and 6:00) is 1/2^{N-1}. Similarly the probability that a clockwise semicircle starting at any point i, where i \in {2, ..., N} contains all the other N — 1 points is also 1/2^{N-1}
    - Claim: the events that all the other N — 1 points are in the clockwise semicircle starting at point 1, 2, ..., N are mutually exclusive. In other words, if we starting at point i and proceeding clockwise along the circle, sequentially encounters points i+1, i+2,...,  N, 1, ..., i — 1 in half a circle, then starting at any other point j, we cannot encounter all
    other points within a clockwise semicircle. Figure 4.1 clearly demonstrates this conclusion. if starting at point i and proceeding clockwise along the circle, we sequentially encounter points i+1, i+2, ..., N, 1, ..., i—1 within half a circle, the clockwise arc between i—1 and i must be no less than half a circle. If we start at any other point, in order to reach all other points clockwise, the clockwise arc between and i are always included. So we cannot reach all points within a clockwise semicircle starting from any other points. Hence, all these events are mutually exclusive and we have
        - P(\bigcup_{i=1}^N E_i) = \bigcup_{i=1}^N P(E_i) => P(\bigcup_{i=1}^N) = N * 1/2^{N-1} = N/2^{N-1}
    - The same argument can be extended to any arcs that have a length less than half a circle. If the ratio of the arc length to the circumference of the circle is x (X <= 1/2), then the probability of all N points fitting into the arc is N * X^{N-1}
    - ![Figure 4.1](images/4.1.png)

## 4.2 Combinatorial Analysis
- Many problems in probability theory can be solved by simply counting the number of different ways that a certain event can occur. The mathematic theory of counting is often referred to as combinatorial analysis (or combinatorics). In this section. we will cover the basics of combinatorial analysis.
Basic principle of counting: Let S be a set of length-k sequences. If there are 
    - n1 possible first entries,
    - n2 possible second entries for each first entry,
    - n3 possible third entries for each combination of first and second entries, etc. Then there are a total of n1 * n2 ... * nk possible outcomes.
- Permutation
    - A rearrangement of objects into distinct sequence (i.e., order matters).
    - Property
        - There are	n!/(n1! n2! ... nr !) different permutations of n objects of which n1 are alike, n2 are alike, ... , nr are alike.
- Combination
    - An unordered collection of objects (i.e., order doesn't matter).
    - Property: There are \binom{n}{r} = n!/(n-r)!r! different combinations of n distinct objects taken r at a time
- binomial theorem
    - (x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}
- inclusion-exclusion principle
    - P(E1 \cup E2) = P(E1) + P(E2) - P(E1E2)



### **Poker hands**
- Poker is a card game in which each player gets a hand of 5 cards. There are 52 cards in a deck. Each card has a value and belongs to a suit. There are 13 values, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A, and four suits, spade, club, heart, diamond
- What are the probabilities of getting hands with four-of-a-kind (four of the five cards with the same value)? Hands with a full house (three cards of one value and two cards of another value)? Hands with two pairs?
- Solution
    - The number of different hands of a five-card draw is the number of 5-element subsets of a 52-clement set, so total number of hands = \binom{52}{5} = 2598960
    - Hands with a four-of-a-kind
        - First we can choose the value of the four cards with the same value, there are 13 choices. The 5th card can be any of the rest 48 cards (12 choices for values and 4 choices for suits). So the number of hands with four-of-a kind is 13 * 48 = 624.
    - Hands with a Full House: In sequence we need to choose the value of the triple. 13 choices; the suits of the triple, \binom{4}{3} choices; the value of the pair, 12 choices; and the suits of the pair \binom{4}{2} choices. So the number of hands with full house is 13 * \binom{4}{3} * 12 * \binom{4}{2} = 13 * 4 * 12 * 6 = 3744
    - hands with two pairs: In sequence we need to choose the values of the two pairs, \binom{13}{2} choices; the suits of the firs pair, \binom{4}{2} choices; the suits of the second pair, \binom{4}{2} choicesl and the ramining card, 44 (52 - 4 * 2, since the last cards can not have the same value as either pair) choices. So the number of hands with two pairs is \binom{13}{2} * \binom{4}{2} * \binom{4}{2} * 44 = 78 * 6 * 6 * 44 = 123552
    - to calculate the probability of each, we only need to divide the number of hands of each kind by the total possible number of hands

### **Hopping rabbit**
- A rabbit sits at the bottom of a staircase with n stairs. The rabbit can hop up only one ortwo stairs at a tilne, How many different ways are there for the rabbit to ascend to top of the stairs?
- Hint: Consider an induction approach. Before the final hop to reach the n-th stair, the rabbit can be at either the (n-1)-th stair of the (n-2)-th stair assuming n > 2
- Solution
    - Let's begin with the simplest cases and consider solving the problem for any number of stairs using induction. For n = 1 , there is only one way and f (1) = 1. For n = 2, we can have one 2-stair hop or two 1-stair hops. So f(2) = 2. For any n > 2, there are always two possibilities for the last hop, either it's a 1-stair hop or a 2-stair bop. In the former case, the rabbit is at (n-1) before reaching n, and it has f(n —1) ways to reach (n-1). In the latter case, the rabbit is at (n-2) before reaching n, and it has f(n — 2) ways to reach (n - 2). So we have f (n) = f(n — 2) + f n —1). Using this function we can calculate f (n) for n = 3, 4, ...


### **Screwy pirates 2**
- Having peacefully divided the loot (in chapter 2), the pirate team goes on for more looting and expands the group to II pirates. To protect their hard-won treasure, they gather together to put all the loot in a safe. Still being a democratic bunch, they decide that only a majority — any majority — of them (>= 6) together can open the safe. So they ask a locksmith to put a certain number of locks on the safe. To access the treasure, every lock needs to be opened. Each lock can have multiple keys; but each key only opens one lock. The locksmith can give more than one key to each pirate.
- What is the smallest number of locks needed? And how many keys must each pirate carry?
- Hint: every subgroup of 6 pirates should have the same key to a unique lock that the other 5 pirates do not have.

- Solution
    - This problem is a good example of the application of combinatorial analysis in information sharing and cryptography. A general version of the problem was explained in a 1979 paper "How to Share a Secret" by Adi Shamir. Let's randomly select 5 pirates from the 11-member group; there must be a lock that none of them has the key to. Yet any of the other 6 pirates must have the key to this lock since any 6 pirates can open all locks. In other words, we must have a "special" lock to which none of the 5 selected pirates has a key and the other 6 pirates all have keys. Such 5-pirate groups are randomly selected. So for each combination of 5 pirates, there must be such a "special" lock. The minimum number of locks needed is \binom{11}{5} = 462 locks. Each lock has 6 keys, which are given to a unique 6-member subgroup. So each pirate must have 462 * 6 / 11 = 252 keys. That's surely a lot of locks to put on a safe and a lot of keys for each pirate to carry.

## Chess tournament
A chess tournament has 2^n players with skills 1 > 2 > ... > 2^n. It is organized as a knockout tournament, so that after each round only the winner proceeds to the next round. Except for the final, opponents in each round are drawn at random. Let's also assume that when two players meet in a game, the player with better skills always wins. What's the probability that players 1 and 2 will meet in the final?
- Hint: Consider separating the players to two 2^{n-1} subgroups. What will happen if player 1 and 2 in the same group? Or not in the same group?	
- Solution
    - There are at least two approaches to solve the problem. The standard approach applies multiplication rule based on conditional probability, while a counting approach is far more efficient. (We will cover conditional probability in detail in the next section.) Let's begin with the conditional probability approach, which is easier to grasp. Since there are 2" players. the tournament will have n rounds (including the final). For round 1, players 2, 3, ..., 2^n each have 1/(2^n - 1) probability to be 1's rival, so the probability that 1 and 2 do not meet in round 1 is (2^n - 2)/(2^n - 1) = (2 * (2^{n-1} - 1))/(2^n - 1). Condition on that 1 and 2 do not meet in round 1. 2^{n-1} players proceed to the 2nd round and the conditional probability that 1 and 2 will not meet in round 2 is (2^{n-1} - 2)/(2^{n-1} - 1) = (2 * (2^{n-2} - 1))/(2^{n-1} - 1). We can repeat the same process until the (n-1)-th round, in which there are 2^2 (= 2^n / 2^{n-2}) players left and the conditional probability that 1 and 2 will not meet inround (n — 1) is (2^2 - 2)/(2^2 - 1) = (2 * (2^{2-1} - 1))/(2^2 - 1)
    - Let E1 be the event that 1 and 2 do not meet in round 1;
    - Let E2 be the event that I and 2 do not meet in rounds 1 and 2;
    ...
    - Let E_{n-1} be the the event that 1 and 2 do not meet in round	n —1
    - Apply the multiplication rule. we have P(1 and 2 meet in the n-th game) = P(E1) * P(E2 | E1) * ... * P(E_{n-1} | E1 E2 ... E_{n-2})
    = (2 * (2^{n-1} - 1))/(2^n - 1) * (2 * (2^{n-2} - 1))/(2^n - 1) * ... * (2 * (2^{2-1} - 1))/(2^2 - 1) = 2^{n-1}/(2^n - 1)
    - Now let's move on to the counting approach. Figure 4.2A is the general case of what happens in the final. Player 1 always wins, so he will be in the final. From the figure, it is obvious that 2^n players are separated to two 2^{n-1}-player subgroups and each group will have one player reaching the final. As shown in Figure 4.2B, for player 2 to reach the final, he/she must be in a different subgroup from I . Since any of the remaining players in 2,3,..., 2^n are likely to be one of the (2^{n-1} — 1) players in the same subgroup as player 1 or one of the 2^{n-1} players in the subgroup different from player 1, the probability that 2 is in a different subgroup from 1 and that 1 and 2 will meet in the final is simply (2^{n-1})/(2^n - 1). Clearly, the counting approach provides not only a simpler solution but also more insight to the problem.
    - ![Figure 4.1](images/4.1.png)