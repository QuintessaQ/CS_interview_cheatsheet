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
