## Overview
- start by asking you to design a system that performs a given task
### examples
- Design a URL shortening service like bit.ly.
- How would you implement the Google search?
- Design a client-server application which allows people to play chess with one another.
- How would you store the relations in a social network like Facebook and implement a feature where one user receives notifications when their friends like the same things as they do?

## Step1: System Design Process
- use cases
    - e.g. Design a URL shortening service like bit.ly.
        - shortening: take an url -> return shorter url
        - redirection: take a short url -> redirect to the original url
    - custom url: let user custom their short url
    - analytics: allow people to look at usage statistics of the url
    - automatic link expiration
    - manual link removal: remove a short url used before
    - UI vs API
- constraints
    - usage per second: e.g. assume not in top3 url service but in top10
    - start estimating from usage per month

## Step2: Abstract design
-  draw a simple diagram of your ideas
- e.g. url shortening
    - application service layer
        - shortening service
            - generate new hash
            - check if it's in data storage
                - if not, generate new mapping
                - if yes, keep generating until an unusued one is found
        - redirection service
            - retrieve the value given the hash
    - data storage layer, keeps track of the hash to url mapping
        - act like a big hash table
        - stores new mapping
        - retrieves value given a key
    - hashed_url = convert_to_base_62(md5(original_url + random_salt))[:6]

## Topics
### Concurrency
- Do you understand threads, deadlock, and starvation? Do you know how to parallelize algorithms? Do you understand consistency and coherence?

### Networking
- Do you roughly understand IPC and TCP/IP? Do you know the difference between throughput and latency, and when each is the relevant factor?

### Abstraction
- You should understand the systems you’re building upon. Do you know roughly how an OS, file system, and database work? Do you know about the various levels of caching in a modern OS?

### Real-World Performance
- You should be familiar with the speed of everything your computer can do, including the relative performance of RAM, disk, SSD and your network.

### Estimation
- Estimation, especially in the form of a back-of-the-envelope calculation, is important because it helps you narrow down the list of possible solutions to only the ones that are feasible. Then you have only a few prototypes or micro-benchmarks to write.

### Availability and Reliability
- Are you thinking about how things can fail, especially in a distributed environment? Do know how to design a system to cope with network failures? Do you understand durability?


## random links
- https://www.palantir.com/2011/10/how-to-rock-a-systems-design-interview/

