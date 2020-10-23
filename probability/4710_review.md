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
    - P(bigcup_{i=1}^{\inf} A_i) = \sum_{i=1}^{\infty} P(A_i)
    - P(A_1 \cup A_2 \cup ... \cup A_n) = P(A_1) + P(A_2) + ... + P(A_n)
- probability space (\Omega, \F, P)
- mutually exclusive
  - A_i \cap A_j = \empty
- cartesian product spaces
  - A_1 x A_2 x ... x A_n = {(x_1, x_2, ..., x_n) | x_i \in A_i, i \in [1,n]}
  - set of ordered n tuples with the i-th element from A_i

## random sampling
