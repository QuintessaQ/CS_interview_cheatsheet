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
