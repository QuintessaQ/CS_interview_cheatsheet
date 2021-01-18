Caching
====
# keypoints
- Take advantage of the locality of reference principle: recently requested data is likely to be requested again.
- Exist at all levels in architecture, but often found at the level nearest to the front end.

## Application server cache
- Cache placed on a request layer node.
- When a request layer node is expanded to many nodes
  - Load balancer randomly distributes requests across the nodes.
  - The same request can go to different nodes.
  - Increase cache misses.
  - Solutions:
    - Global caches
    - Distributed caches

## Distributed cache
- Each request layer node owns part of the cached data.
- Entire cache is divided up using a consistent hashing function.
- Pro
  - Cache space can be increased easily by adding more nodes to the request pool.
- Con
  - A missing node leads to cache lost.

## Global cache
- A server or file store that is faster than original store, and accessible by all request layer nodes.
- Two common forms
  - Cache server handles cache miss.
    - Used by most applications.
  - Request nodes handle cache miss.
    - Have a large percentage of the hot data set in the cache.
    - An architecture where the files stored in the cache are static and shouldn’t be evicted.
    - The application logic understands the eviction strategy or hot spots better than the cache

## Content distributed network (CDN)
- For sites serving large amounts of static media.
- Process
  - A request first asks the CDN for a piece of static media.
  - CDN serves that content if it has it locally available.
  - If content isn’t available, CDN will query back-end servers for the file, cache it locally and serve it to the requesting user.
- If the system is not large enough for CDN, it can be built like this:
  - Serving static media off a separate subdomain using lightweight HTTP server (e.g. Nginx).
  - Cutover the DNS from this subdomain to a CDN later.

## Cache invalidation
- Keep cache coherent with the source of truth. Invalidate cache when source of truth has changed.
- Write-through cache
  - Data is written into the cache and permanent storage at the same time.
  - Pro
    - Fast retrieval, complete data consistency, robust to system disruptions.
  - Con
    - Higher latency for write operations.
- Write-around cache
  - Data is written to permanent storage, not cache.
  - Pro
    - Reduce the cache that is no used.
  - Con
    - Query for recently written data creates a cache miss and higher latency.
- Write-back cache
  - Data is only written to cache.
  - Write to the permanent storage is done later on.
  - Pro
    - Low latency, high throughput for write-intensive applications.
  - Con
    - Risk of data loss in case of system disruptions.

## Cache eviction policies
- FIFO: first in first out
- LIFO: last in first out
- LRU: least recently used
- MRU: most recently used
- LFU: least frequently used
- RR: random replacement



# text
- Load balancing helps you scale horizontally across an ever-increasing number of servers, but caching will enable you to make vastly better use of the resources you already have as well as making otherwise unattainable product requirements feasible. Caches take advantage of the locality of reference principle: recently requested data is likely to be requested again. They are used in almost every layer of computing: hardware, operating systems, web browsers, web applications, and more. A cache is like short-term memory: it has a limited amount of space, but is typically faster than the original data source and contains the most recently accessed items. Caches can exist at all levels in architecture, but are often found at the level nearest to the front end where they are implemented to return data quickly without taxing downstream levels.

## Application server cache
- Placing a cache directly on a request layer node enables the local storage of response data. Each time a request is made to the service, the node will quickly return local cached data if it exists. If it is not in the cache, the requesting node will query the data from disk. The cache on one request layer node could also be located both in memory (which is very fast) and on the node’s local disk (faster than going to network storage).
- What happens when you expand this to many nodes? If the request layer is expanded to multiple nodes, it’s still quite possible to have each node host its own cache. However, if your load balancer randomly distributes requests across the nodes, the same request will go to different nodes, thus increasing cache misses. Two choices for overcoming this hurdle are global caches and distributed caches.

## Content Distribution Network (CDN)
- CDNs are a kind of cache that comes into play for sites serving large amounts of static media. In a typical CDN setup, a request will first ask the CDN for a piece of static media; the CDN will serve that content if it has it locally available. If it isn’t available, the CDN will query the back-end servers for the file, cache it locally, and serve it to the requesting user.
- If the system we are building isn’t yet large enough to have its own CDN, we can ease a future transition by serving the static media off a separate subdomain (e.g. static.yourservice.com) using a lightweight HTTP server like Nginx, and cut-over the DNS from your servers to a CDN later.

## Cache Invalidation
- While caching is fantastic, it does require some maintenance for keeping cache coherent with the source of truth (e.g., database). If the data is modified in the database, it should be invalidated in the cache; if not, this can cause inconsistent application behavior.

- Solving this problem is known as cache invalidation; there are three main schemes that are used:

- Write-through cache
    - Under this scheme, data is written into the cache and the corresponding database at the same time. The cached data allows for fast retrieval and, since the same data gets written in the permanent storage, we will have complete data consistency between the cache and the storage. Also, this scheme ensures that nothing will get lost in case of a crash, power failure, or other system disruptions.
    - Although, write through minimizes the risk of data loss, since every write operation must be done twice before returning success to the client, this scheme has the disadvantage of higher latency for write operations.

- Write-around cache
    - This technique is similar to write through cache, but data is written directly to permanent storage, bypassing the cache. This can reduce the cache being flooded with write operations that will not subsequently be re-read, but has the disadvantage that a read request for recently written data will create a “cache miss” and must be read from slower back-end storage and experience higher latency.

- Write-back cache
    - Under this scheme, data is written to cache alone and completion is immediately confirmed to the client. The write to the permanent storage is done after specified intervals or under certain conditions. This results in low latency and high throughput for write-intensive applications, however, this speed comes with the risk of data loss in case of a crash or other adverse event because the only copy of the written data is in the cache.

## Cache eviction policies
- First In First Out (FIFO)
    - The cache evicts the first block accessed first without any regard to how often or how many times it was accessed before.
- Last In First Out (LIFO) 
    - The cache evicts the block accessed most recently first without any regard to how often or how many times it was accessed before.
- Least Recently Used (LRU)
    - Discards the least recently used items first.
- Most Recently Used (MRU)
    - Discards, in contrast to LRU, the most recently used items first.
- Least Frequently Used (LFU)
    - Counts how often an item is needed. Those that are used least often are discarded first.
- Random Replacement (RR)
    - Randomly selects a candidate item and discards it to make space when necessary.