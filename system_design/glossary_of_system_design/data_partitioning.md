Data Partitioning
====
# keypoints
- break up a big database (DB) into many smaller parts
- after a certain scale point, it is cheaper and more feasible to scale horizontally by adding more machines

## Partitioning Methods
- Horizontal partitioning (range based partitioning, data sharding)
    - put different rows into different tables
        - e.g. 0-1k, 1k-2k, ...
    - problem
        - if range for partition not chosen carefully, could have unbalanced serves
- Vertical Partitioning
    - store tables related to a specific feature in one server
        - e.g. server1: insta pics, server2: user info..;
    - problem
        - if keeps growing, may be necessary to further partition a feature specific DB across various servers
- Directory Based Partitioning
    - create a lookup service which knows your current partitioning scheme 
    - to find out where a particular data entity resides, query the directory server that holds the mapping between each tuple key to its DB server

## Partitioning Criteria
- Key or Hash-based partitioning
    - apply a hash function to some key attributes of the entity we are storing -> partition number
    - e.g. ID % 100 if we have 100 partitions
    - should ensure uniform allocation
    - problem
        - adding new serves might require rehashing -> downtime for the service
- List partitioning
    - each partition assigned a list of values
    - to insert a new record, find the partition with the corresponding key
- Round-robin partitioning
    - i^th tuple assigned to partition i % n
- Composite partitioning
    - combine the above schemes
    - e.g. list partitioning -> hash based partitioning
    - e.g. consistent hashing =  hash + list partitioning
        - when a hash table is resized, only n/m keys need to be remapped on average where n is the number of keys and m is the number of slots

## Common Problems of Data Partitioning
- Joins and Denormalization
    - if database is partitioned and spread across multiple machines then often not feasible to perform joins
    - workaround
        - denormalize the database so that queries that previously required joins can be performed from a single table
        - but denormalization leads to data inconsistency
- Referential integrity
    - enforce data integrity constraints in a partitioned database difficult, e.g. foreign keys
- Rebalancing
    - reason to change partition scheme
        - data distribution not uniform
        - a lot of load on a partition
    - solution
        - create more DB partitions or rebalance existing partitions
        - will incur downtime
        - could use directory based partitioning

