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
- draw a simple diagram of your ideas
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

## Step3: Understanding bottleneck
- traffic is probably not going to be hard, data more interesting

## Step4: Scalability
- ideas
    - Vertical scaling
    - Horizontal scaling
    - Caching
    - Load balancing
    - Database replication
    - Database partitioning
- clones
    - every server contains exactly the same codebase and does not store any user-related data, like sessions or profile pictures, on local disc or memory. 
    - Sessions need to be stored in a centralized data store which is accessible to all your application servers. 
    - a code change is sent to all your servers without one server still serving old code, serving the same codebase from all your servers
    - servers can now horizontally scale and you can already serve thousands of concurrent requests
- database
    - can stay with MySQL, and use it like a NoSQL database
    - or you can switch to a better and easier to scale NoSQL database like MongoDB or CouchDB, using NoSQL instead of scaling a relational database
- cache
    - A cache is a simple key-value store and it should reside as a buffering layer between your application and your data storage.
    - Whenever your application has to read data it should at first try to retrieve the data from your cache.
    - if it’s not in the cache should it then try to get the data from the main data source
    - Cached Database Queries
        - A hashed version of your query is the cache key
        - issues
            - expiration: it is hard to delete a cached result when you cache a complex query 
            - When one piece of data changes (for example a table cell) you need to delete all cached queries who may include that table cell.
    - Cached Objects
        - store the complete instance of the class or the assembed dataset in the cache
        - easily get rid of the object whenever something did change and makes the overall operation of your code faster and more logical.
- asynchronism
    - Async #1
        - doing the time-consuming work in advance and serving the finished work with a low request time.
    - Async #2
        - start the task when the customer is in the bakery and tell him to come back at the next day. Refering to a web service that means to handle tasks asynchronously.
        - A user comes to your website and starts a very computing intensive task which would take several minutes to finish. So the frontend of your website sends a job onto a job queue and immediately signals back to the user: your job is in work, please continue to the browse the page



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

