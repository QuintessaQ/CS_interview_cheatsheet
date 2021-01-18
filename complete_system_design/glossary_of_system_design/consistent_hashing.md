Consistent Hashing
====
# keypoints

- Distributed Hash Table (DHT)
    - index = hash_function(key)
- distributed caching system
    - n cache servers, if index = key % n
    - problem
        - not horizontally scalable
            - when adding a new cache host, all existing mappings broken
        - may not be load balanced

## consistent hashing
- minimize reorganization when nodes are added or removed
- only k/n keys need to be remapped 
- objects mapped to the same host if possible
- if host removed from the system
    - object on that host are shared by other hosts
- if new host added
    - takes its share from a few hosts 

## how it works
- given a list of cache servers
    - hash them to integers in the range
- hash a key to a single integer
- move clockwise on the ring
    - til finding the first cache
- that cache is the one containing the key
- to add a new server D
    - keys originally at C split
    - some shifted to D
- to remove a server A
    - all keys originally mapped to A remapped to B
- problem: real data randomly distributed, might not be uniform
    - add virtual replicas for cache server
    - map each cache to multiple points on the ring, i.e. replicas
    - each cache associated with multiple portion of the ring

# text
- Distributed Hash Table (DHT) is one of the fundamental components used in distributed scalable systems. Hash Tables need a key, a value, and a hash function where hash function maps the key to a location where the value is stored.
- index = hash_function(key)
- Suppose we are designing a distributed caching system. Given ‘n’ cache servers, an intuitive hash function would be ‘key % n’. It is simple and commonly used. But it has two major drawbacks:
    - It is NOT horizontally scalable. Whenever a new cache host is added to the system, all existing mappings are broken. It will be a pain point in maintenance if the caching system contains lots of data. Practically, it becomes difficult to schedule a downtime to update all caching mappings.
    - It may NOT be load balanced, especially for non-uniformly distributed data. In practice, it can be easily assumed that the data will not be distributed uniformly. For the caching system, it translates into some caches becoming hot and saturated while the others idle and are almost empty.
- In such situations, consistent hashing is a good way to improve the caching system.

## What is Consistent Hashing?
- Consistent hashing is a very useful strategy for distributed caching systems and DHTs. It allows us to distribute data across a cluster in such a way that will minimize reorganization when nodes are added or removed. Hence, the caching system will be easier to scale up or scale down.
- In Consistent Hashing, when the hash table is resized (e.g. a new cache host is added to the system), only ‘k/n’ keys need to be remapped where ‘k’ is the total number of keys and ‘n’ is the total number of servers. Recall that in a caching system using the ‘mod’ as the hash function, all keys need to be remapped.
- In Consistent Hashing, objects are mapped to the same host if possible. When a host is removed from the system, the objects on that host are shared by other hosts; when a new host is added, it takes its share from a few hosts without touching other’s shares.

## How does it work?
- As a typical hash function, consistent hashing maps a key to an integer. Suppose the output of the hash function is in the range of [0, 256]. Imagine that the integers in the range are placed on a ring such that the values are wrapped around.
- Here’s how consistent hashing works:

    - Given a list of cache servers, hash them to integers in the range.
    - To map a key to a server,
        - Hash it to a single integer.
        - Move clockwise on the ring until finding the first cache it encounters.
        - That cache is the one that contains the key. See animation below as an example: key1 maps to cache A; key2 maps to cache C.
![hash1](../images/hash1.png)
![hash2](../images/hash2.png)
![hash3](../images/hash3.png)
![hash4](../images/hash4.png)
![hash5](../images/hash5.png)

- To add a new server, say D, keys that were originally residing at C will be split. Some of them will be shifted to D, while other keys will not be touched.
- To remove a cache or, if a cache fails, say A, all keys that were originally mapped to A will fall into B, and only those keys need to be moved to B; other keys will not be affected.
- For load balancing, as we discussed in the beginning, the real data is essentially randomly distributed and thus may not be uniform. It may make the keys on caches unbalanced.
- To handle this issue, we add “virtual replicas” for caches. Instead of mapping each cache to a single point on the ring, we map it to multiple points on the ring, i.e. replicas. This way, each cache is associated with multiple portions of the ring.
- If the hash function “mixes well,” as the number of replicas increases, the keys will be more balanced.

