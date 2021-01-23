# Chapter 2 Brain Teasers
- In this chapter, we cover problems that only require common sense, logic, reasoning, and basic—no more than high school level—math knowledge to solve. In a sense, they are real brain teasers as opposed to mathematical problems in disguise. Although these brain  teasers do not require specific math knowledge, they are no less difficult than other quantitative interview problems. Some of these problems test your analytical and general problem-solving skills; some require you to think out of the box; while others ask you to solve the problems using fundamental math techniques in a creative way. In this chapter, we review sonic interview problems to explain the general themes of brain teasers that you are likely to encounter in quantitative interviews.

## 2.1 Problem Simplification
- If the original problem is so complex that you cannot come up with an immediate solution, try to identify a simplified version of the problem and start with it. Usually you can start with the simplest sub-problem and gradually increase the complexity. You do not need to have a defined plan at the beginning. Just try to solve the simplest cases and analyze your reasoning. More often than not, you will find a pattern that will guide you through the whole problem.

### **Screwy pirates**
- Five pirates looted a chest full of 100 gold coins. Being a bunch of democratic pirates, they agree cm the following method to divide the loot:
- The most senior pirate will propose a distribution of the coins. All pirates, including the mosr senior pirate, will then vote. If at least 50% of the pirates (3 pirates in this case) accept the proposal, the gold is divided as proposed. If not, the most senior pirate will be fed to shark and the process starts over with the next most senior pirate... The process is repeated until a plan is approved. You can assume that all pirates arc perfectly rational: they want to stay alive first and to get as much gold as possible second. Finally, being blood-thirsty pirates. they want to have fewer pirates on the boat if given a choice between otherwise equal outcomes.
- How will the gold coins be divided in the end?

- **Solution** 
    - If you have not studied game theory or dynamic programming, this strategy problem may appear to be daunting. If the problem with 5 pirates seems complex, we can always ,vtari with a simplified version of the problem by reducing the number of pirates. Since the solution to 1-pirate case is trivial, let's start with 2 pirates. The senior pirate (labeled as 2) can claim all the gold since he will always get 50% of the votes from himself and pirate 1 is left with nothing.
    - Let's add a more senior pirate, 3. He knows that if his plan is voted down, pirate 1 will get nothing. But if he offers private 1 nothing. pirate 1 will be happy to kill him. So pirate 3 will offer private 1 one coin and keep the remaining 99 coins, in which strategy the plan will have 2 votes from pirate 1 and 3.
    - If pirate 4 is added, he knows that if his plan is voted down, pirate 2 will get nothing. So pirate 2 will settle for one coin if pirate 4 offers one, So pirate 4 should offer pirate 2 one coin and keep the remaining 99 coins and his plan will be approved with 50% of the votes from pirate 2 and 4.
    - Now we finally come to the 5-pirate case. He knows that if his plan is voted down, both pirate 3 and pirate 1 will get nothing. So he only needs to offer pirate 1 and pirate 3 one coin each to get their votes and keep the remaining 98 coins. If he divides the coins this way. he will have three out of the five votes: from pirates 1 and 3 as well as himself.
    - Once we start with a simplified version and add complexity to it, the answer becomes obvious. Actually after the case n = 5, a clear pattern has emerged and we do not need to stop at 5 pirates. For any 2n+1 pirate case (n should be less than 99 though), the most senior pirate will offer pirates 1. 3, and 2n-1 each one coin and keep the rest for himself.

### **Tiger and sheep**
- One hundred tigers and one sheep are put on a magic island that only has
grass. Tigers can eat grass, but they would rather eat sheep. Assume: 
    - A. Each time only one tiger can eat one sheep, and that tiger itself will become a sheep after it eats the sheep. 
    - B. All tigers are smart and perfectly rational and they want to survive. So will the sheep be eaten?

- **Solution**
    - 100 is a large number. so again let's start with a simplified version of the problem. If there is only 1 tiger (n=1), surely it will eat the sheep since it does not need to worry about being eaten. How about 2 tigers? Since both tigers are perfectly rational, either tiger probably would do some thinking as to what will happen if it eats the sheep. Either tiger is probably thinking: if I eat the sheep, I will become a sheep, and then I will be eaten by the other tiger. So to guarantee the highest likelihood of survival, neither tiger will eat the sheep.
    - If there are 3 tigers, the sheep will be eaten since each tiger will realize that once it changes to a sheep, there will be 2 tigers left and it will not be eaten. So the first tiger that thinks this through will eat the sheep. If there are 4 tigers, each tiger will understand that if it eats the sheep, it will turn to a sheep. Since there are 3 other tigers, it will be eaten. So to guarantee the highest likelihood of survival, no tiger will eat the sheep.
    - Following the same logic, we can naturally show that if the number of tigers is even, the sheep will not be eaten. If the number is odd, the sheep will be eaten. For the case n = 100, the sheep will not be eaten.

## 2.2 Logic Reasoning
### **River crossing**
- Four people, A, B. C and D need to get across a river. The only way to cross the river is by an old bridge, which holds at most 2 people at a time. Being dark, they can't cross the bridge without a torch, of which they only have one. So each pair can only walk at the speed of the slower person. They need to get all of them across to the other side as quickly as possible, A is the slowest and takes 10 minutes to cross; B takes 5 minutes; C takes 2 minutes; and D takes 1 minute.
- What is the minimum time to get all of them across to the other side?
- **Solution**
    - The key point is to realize that the 10-minute person and this should not go with the 5-min person and this shoudl not happen in the first crossing, otherwise one of them has to go back, So C and D should go across first (2 min); then send D back (1 min)l A and B go across (10 min); send C back (2 min); C and D go across again (2 min)
    - It takes 17 minutes in total. Alternatively, we the second round, which takes 17 minutes as well.

### **Birthday problem*
- You and your colleagues know that your boss A's birthday is one of the following 10 dates:
    - Mar 4, Mar 5, Mar 8
    - Jun 4, Jun 7
    - Sep 1, Sep 5
    - Dec 1, Dec 2, Dec 8
- A told you only the month of his birthday. and told your colleague C only the day. After that, you first said: "I don't know A's birthday; C doesn't know it either." After hearing what you said, C replied: "I didn't know A's birthday, but now I know it." You smiled and said: "Now I know it, too." After looking at the 10 dates and hearing your comments, your administrative assistant wrote down A's birthday without asking any questions. So what did the assistant write?
- **Solution**
    - Don't let the "he said, she said" part confuses you. Just interpret the logic behind each individual's comments and try your best to derive useful information from these comments.
    - Let D be the day of the month of A's birthday, we have D \in {1,2,4,5,7,8}. If the birthday is on a unique day, C will know the A's birthday immediately. Among possible Ds, 2 and 7 are unique days. Considering that you are sure that C does not know A's birthday, you must infer that the day the C was told of is not 2 or 7. Conclusion: the month is not June or December. (If the month had been June, the day C was told of may have been 2; if the month had been December, the day C was told of may have been 7.)
    - Now C knows that the month must be either March or September. He immediately figures out A's birthday, which means the day must be unique in the March and September list. It means A's birthday cannot be Mar 5, or Sep 5. Conclusion: the birthday must be Mar 4, Mar 8 or Sep 1.
    - Among these three possibilities left, Mar 4 and Mar 8 have the same month. So if the month you have is March, you still cannot figure out A's birthday. Since you can figure out A's birthday, A's birthday must be Sep 1. Hence, the assistant must have written Sep 1.

### **Card game**
- A casino offers a card game using a normal deck of 52 cards. The rule is that you turn, over two cards each time. For each pair, if both are black, they go to the dealer's pile; If both are red, they go to your pile; if one black and one red, they are discarded. The process is repeated until you two go through all 52 cards. If you have more cards in your pile. you win $100; otherwise (including ties) you get nothing. The casino allows you to negotiate the price you want to pay for the game. How much would you be willing to pay to play this game?
- Hint: try to approach the problem using symmetty. Each discarded pair has one black and one red card. What does that tell you as to the number of black and red cards in the rest two piles?
- **Solution**
    - This surely is an insidious casino. No matter how the cards are arranged, you and the dealer will always have the same number of cards in your piles. Why? Because each pair of discarded cards have one black card and one red card, so equal number of red and black cards are discarded. As a result, the number of red cards left for you and the number of black cards left for the dealer are always the same. The dealer always wins! So we should not pay anything to play the game.

### **Burning ropes**
- You have two ropes, each of which takes 1 hour to burn. But either rope has different densities at different points, so there's no guarantee of consistency in the time it takes different sections within the rope to bum. How do you use these two ropes to measure 45 minutes?
- **Solution**
    - This is a classic brain teaser question. For a rope that takes x minutes to burn, if you light both ends of the rope simultaneously, it takes x12 minutes to burn. So we should light both ends of the first rope and light one end of the second rope. 30 minutes later, the first rope will get completely burned, while that second rope now becomes a 30-min rope. At that moment, we can light the second rope at the other end (with the first end still burning), and when it is burned out, the total time is exactly 45 minutes.

### **Defective ball**
- You have 12 identical balls. One of the balls is heavier OR lighter than the rest (you don't know which). Using just a balance that can only show you which side of the tray is heavier, how can you determine which ball is the defective one with 3 measurements?
- Hint: First do it for 9 identical balls and use only 2 measurements. knowing that one is heavier than the rest.
- **Solution**
    - This weighing problem is another classic brain teaser and is still being asked by many interviewers. The total number of balls often ranges from 8 to more than 100. Here we use n=12 to show the fundamental approach. The key is to separate the original group (as well as any intermediate subgroups) into three sets instead of two. The reason is that the comparison of the first two groups always gives inkirnat on about the third group.
    - Considering that the solution is wordy to explain, I draw a tree diagram in Figure 2.1 to show the approach in detail. Label the halls 1 through 12 and separate them to three groups with 4 balls each. Weigh balls 1, 2, 3, 4 against balls 5, 6, 7, 8. Then we go on to explore two possible scenarios: two groups balance, as expressed using an "=" sign, or 1, 2, 3, 4 are lighter than 5, 6, 7, 8, as expressed using an "<" sign. There is no need to explain the scenario that 1, 2, 3, 4 are heavier than 5, 6, 7, 8. (Why?)
    - If the two groups balance, this immediately tells us that the defective ball is in 9, 10, 11 and 12, and it is either lighter (L) or heavier (H) than other balls. Then we take 9, 10 and 11 from group 3 and compare balls 9, 10 with 8, 11. Here we have already figured out that 8 is a normal ball. If 9, 10 are lighter, it must mean either 9 or 10 is L or 11 is H. In which case, we just compare 9 with 10. If 9 is lighter, 9 is the defective one and it is L; if 9 and 10 balance, then 11 must he defective and H; If 9 is heavier, 10 is the defective one and it is L. If 9, 10 and 8, 11 balance, 12 is the defective one. If 9, 10 is heavier, than either 9 or 10 is if, or 11 is L.
    - You can easily follow the tree in Figure 2.1 for further analysis and it is clear from the tree that all possible scenarios can he resolved in 3 measurements.
    - ![Figure 2.1](images/2.1.png)
    - In general if you have the information as to whether the defective ball is heavier or lighter, you can identify the defective ball among up to 3 balls using no more than n measurements since each weighing reduces the problem size by 2/3. If you have no information as to whether defective ball is heavier or ligter, you can identify the defective ball among up to (3^n - 3)/2 balls using no more than n measurements.

### **Trailing zeros**
- How many trailing zeros are there in 100! (factorial of 100)?
- **Solution**
    - This is an easy problem. We know that each pair of 2 and 5 will give a trailing zero. If we perform prime number decomposition on all the numbers in 100!, it is obvious that the frequency of 2 will far outnumber of the frequency of 5. So the frequency of 5 determines the number of trailing zeros. Among numbers 1, 2, ...,99, and 100, 20 numbers are divisible by 5 (5, 10, ..., 100 ). Among these 20 numbers, 4 are divisible by 5^2 (25, 50, 75, 100). So the total frequency of 5 is 24 and there are 24 trailing zeros.

### **Horse race**
- There are 25 horses, each of which runs at a constant speed that is different from the other horses'. Since the track only has 5 lanes, each race can have at most 5 horses. If you need to find the 3 fastest horses, what is the minimum number of races needed to identify them?
- **Solution**
    - This problem tests your basic analytical skills. To find the 3 fastest horses, surely all horses need to he tested. So a natural first step is to divide the horses to 5 groups (with horses 1-5, 6-10, 11-15, 16-20, 21-25 in each group). After 5 races, we will have the order within each group, let's assume the order follows the order of numbers (e.g., 6 is the fastest and 10 is the slowest in the 6-10 group). Such an assumption does not affect the generality of the solution. If the order is not as described, just change the labels of the horses. That means 1. 6, 11, 16 and 21 arc the fastest within each group.
    - Surely the last two horses within each group are eliminated. What else can we infer? We know that within each group, if the fastest horse ranks 5th or 4th among 25 horses, then all horses in that group cannot he in top 3; if it ranks the 3rd, no other horse in that group can be in the top 3; if it ranks the 2nd, then one other horse in that group may be in top 3; if it ranks the first, then two other horses in that group may be in top 3.
    - So let's race horses 1, 6, 11, 16 and 21. Again without loss of generality, let's assume the order is 1, 6, 11, 16 and 21. Then we immediately know that horses 4-5, 8-10, 12-15, 16-20 and 21-25 are eliminated. Since 1 is fastest among all the horses, 1 is in. We need to determine which two among horses 2, 3, 6, 7 and 11 are in top 3, which only takes one extra race.
    - So all together we need 7 races (in 3 rounds) to identify the 3 fastest horses.

### **Infinite sequence**
- If x^x^x^x^x ... = 2, where x^y = x to the power of y. What is x?
- **Solution**
    - This problem appears to be difficult, but a simple analysis will give an elegant solution. What do we have from the original equation
    - lim_{n -> \infty} x^x^x^ ... (n terms) = 2 <==> lim_{n -> \infty} x^x^x^ ... (n-1 terms) = 2. In other words, as n -> \infty, adding or minus one x^ should yield the same result
    - so x^x^x^x^x ... = x^(x^x^x^x^x ...) = x^2 = 2
    - x = \sqrt{2}