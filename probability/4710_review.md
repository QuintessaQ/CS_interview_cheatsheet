Introduction To Probability
====
<!-- <img src="https://render.githubusercontent.com/render/math?math=\Omega"> -->

# Experiments with random outcomes
## Sample space & probabilities
- sample space \Omega
  - set of all the possible outcomes of the experiments
- sample points w
  - Elements of \Omega
- events
  - subset of \Omega
- \F
  - collection of events in \Omega
- probability measure / probability distribution P
  - func from \F to \R
  - P(A)
    - prob of event A
- Kolmogorov's axiom
  - 0 <= P(A) <= 1, \any A
  - P(\Omega) = 1, P(\empty) = 0
  - if A_1, A_2, A_3, ... pairwise disjoint events
    - P(\bigcup_{i=1}^{\inf} A_i) = \sum_{i=1}^{\infty} P(A_i)
    - P(A_1 \cup A_2 \cup ... \cup A_n) = P(A_1) + P(A_2) + ... + P(A_n)
- probability space (\Omega, \F, P)
- mutually exclusive
  - A_i \cap A_j = \empty
- cartesian product spaces
  - A_1 x A_2 x ... x A_n = {(x_1, x_2, ..., x_n) | x_i \in A_i, i \in [1,n]}
  - set of ordered n tuples with the i-th element from A_i

## random sampling
- sampling with & without replacement
- ordered & unordered sample

## consequence of the rules of probability
- P(A) + P(A^c) = 1
- monotonicity of probability
  - if A \subset B then P(A) <= P(B)
- inclusion - exclusion
  - P(A \cup B) = P(A) + P(B) - P(A \cap B)
  - P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)
- n person gets hat problem: n person have their hats mixed up, what is the probability that no one gets hi/her own hat? How does this probability bejave as n -> \inf
  - define event A_i = {personi gets his/her hat}
  - P(\bigcap_{i=1}^{n}A_i^c) = 1 - P(\bigcup_{i=1}^n A_i)
  - P(A_i1 \cap A_i2 \cap ... \cap A_ik) = P(i_1, ..., i_k gets their own hat) = \frac{(n-k)!}{n!}  (given k hats assigned correctly, number of ways (n-k) assigned to the rest of guests)
  - \sum_k P(A_i1 \cap A_i2 \cap ... \cap A_ik) = \binom{n}{k} \frac{(n-k)!}{n!} = \frac{1}{k!}
  - P(\bigcup_{i=1}^n A_i) = 1 - 1/2! + 1/3! + ... + (-1)^{n+1} 1/n!
  - P(\bigcap_{i=1}^{n}A_i^c) = 1/2! - 1/3! + ... + (-1)^n 1/n! = \sum_{k=0}^n (-1)^k/k!
  - if n -> \inf, then P(\bigcap_{i=1}^{n}A_i^c) = e^{-1}

## random variables
- random variable X is a function from \Omega into the real numbers
- X is degenerate if P(X = b) = 1
- probability distribution of X is P{X \in B} for set B of real numbers
- X is a discrete random variable if there exists a finite or countably infinite set {k_1, k_2, ...} of real numbers such that sum_i P(X = k_i) = 1
- probability mass function p.m.f. of a discrete random variable is p_X = p(k) = Pr(X = k) for all possible k of X

# Conditional probability and independence
## conditional probability
- The conditional probability of A given B is P(A | B) = P(AB) / P(B)
- Multiplication rule for n events
  - P(A_1A_2...A_n) = P(A_1)P(A_2|A_1)P(A_3|A_1A_2)...P(A_n|A_1A_2...A_{n-1})
- a finite collection of events {B_1, ..., B_n} is a partition of \Omega if B_iB_j = \empty whenever i != j and \bigcup_{i=1}^n B_i = \Omega

## bayes' formula
- P(B | A) = P(AB) / P(A) = \frac{P(A|B)P(B)}{P(A|B)P(B) + P(A|B^c)P(B^c)}
- general version of bayes' formula
  - P(B_k|A) = P(AB_k)/P(A) = \frac{P(A|B_k)P(B_k)}{\sum_{i=1}^n P(A|B_i)P(B_i)}

## independence
- A independent of B if P(A|B) = P(A) or P(AB) = P(A)P(B)
- if A B independent, same is true for A^c and B^c, A^c and B, A and B^c
- X_1, ..., X_n are random variables on the same probability space, then they are independent if P(X_1 \in B_1, X_2 \in B_2, ..., X_n \in B_n) = \prod_{k=1}^n P(X_k \in B_k)

## independent trials
- Bernoulli distribution
  - records the result of a single trial with 2 possile outcomes
  - 0 <= p < 1, X ~ Ber(p) with success probability p if X \in {0, 1} and P(X = 1) = p and P(X = 0) = 1-p
  - e.g. a sequence of n independent trials
    - Pr(X_1 = 0, X_2 = 1, X_3 = X_4 = 0) = p(1-p)^3
- Binomial distribution
  - X \sim Bin(n, p)
  - Let X be the number of successes in n indep trials, with success probaility p, X_i denotes the outcome of trial i
  - X = X_1 + X_2 + ... + X_n
  - Pr(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
- geometric distribution
  - X \sim Geom(p)
  - infinite sequence of indep trials
  - X is the number of trials needed to see the first success
  - P(X = k) = P(X_1 = 0, X_2 = 0, ..., X_{k-1} = 0, X_k = 1) = (1-p)^{k-1}p

## Further topics
- conditional independence 
  - P(A_i1 A_i2 ... A_ik | B) = P(A_i1 | B) P(A_i2 | B) ... P(A_ik | B)
  - e.g. Suppose 9/10 coins are fair, 1/10 coins are biased with tail probability 3/5
    - A_1 = first flip yields tail, A_2 = second flip yields tail
    - success flipis of **a given coin** are independent
    - P(A_1|F) = P(A_2|F) = 1/2, P(A_1|B) = P(A_2|B) = 3/5
    - P(A_1A_2|F) = P(A_1|F)P(A_2|F), P(A_1A_2|B) = P(A_1|B)P(A_2|B) 
    - P(A_1A_2) = P(A_1A_2|F)P(F) + P(A_1A_2|B)P(B) 
- hypergeometric distribution
  - X \sim Hypergeom(N, N_A, n)
  - X takes values in the set [0, n] 
  - P(X = k) = \frac{\binom{N_A}{k} \binom{N - N_A}{n-k}}{\binom{N}{k}}
  - sample n items without replacement, choose k items from N_A type A items, and n-k from N-N_A type B items
- the birthday problem
  - How large should a randomly selected group of people be to guarantee that with probability at least 1/2 there are two people with the same birthday?
  - Take a random sample size of k
  - p_k = Pr(there is repetition in the sample, how large should k be to have p_k > 1/2
  - A_k = the first k picks are all distinct
  - p(A_k) = \frac{365 * 364 * ... * (365 - (k-1))}{365^k}
  - p_k = 1 - p(A_k)