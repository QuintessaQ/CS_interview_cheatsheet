https://www.educative.io/courses/grokking-the-system-design-interview?affiliate_id=5749180081373184/
##Designing a URL Shortening service like TinyURL
### Why do we need URL shortening?
- URL shortening is used for optimizing links across devices, tracking individual links to analyze audience and campaign performance, and hiding affiliated original URLs.

### Requirements and Goals of the System
## Functional Requirements
-Given a URL, our service should generate a shorter and unique alias of it. This is called a short link. This link should be short enough to be easily copied and pasted into applications.
- When users access a short link, our service should redirect them to the original link.
- Users should optionally be able to pick a custom short link for their URL.
- Links will expire after a standard default timespan. Users should be able to specify the expiration time.

## Non-Functional Requirements
- The system should be highly available. This is required because, if our service is down, all the URL redirections will start failing.
- URL redirection should happen in real-time with minimal latency.
- Shortened links should not be guessable (not predictable).

## Extended Requirements
- Analytics; e.g., how many times a redirection happened?
Our service should also be accessible through REST APIs by other services.

### Capacity Estimation and Constraints
- Our system will be read-heavy. There will be lots of redirection requests compared to new URL shortenings. Let’s assume a 100:1 ratio between read and write.

## Traffic estimates: 
- Assuming, we will have 500M new URL shortenings per month, with 100:1 read/write ratio, we can expect 50B redirections during the same period:
100 * 500M => 50B
- What would be Queries Per Second (QPS) for our system? New URLs shortenings per second:
500 million / (30 days * 24 hours * 3600 seconds) = ~200 URLs/s
- Considering 100:1 read/write ratio, URLs redirections per second will be:
100 * 200 URLs/s = 20K/s

## Storage estimates
- Let’s assume we store every URL shortening request (and associated shortened link) for 5 years. Since we expect to have 500M new URLs every month, the total number of objects we expect to store will be 30 billion:
500 million * 5 years * 12 months = 30 billion

- Let’s assume that each stored object will be approximately 500 bytes (just a ballpark estimate–we will dig into it later). We will need 15TB of total storage:
30 billion * 500 bytes = 15 TB

## Memory estimates
- If we want to cache some of the hot URLs that are frequently accessed, how much memory will we need to store them? If we follow the 80-20 rule, meaning 20% of URLs generate 80% of traffic, we would like to cache these 20% hot URLs.
- Since we have 20K requests per second, we will be getting 1.7 billion requests per day:
20K * 3600 seconds * 24 hours = ~1.7 billion
- To cache 20% of these requests, we will need 170GB of memory.
0.2 * 1.7 billion * 500 bytes = ~170GB
- One thing to note here is that since there will be a lot of duplicate requests (of the same URL), therefore, our actual memory usage will be less than 170GB.

## System APIs
- Following could be the definitions of the APIs for creating and deleting URLs:
    ```
    createURL(api_dev_key, original_url, custom_alias=None, user_name=None, expire_date=None)
    ```
- Parameters
    - api_dev_key (string): The API developer key of a registered account. This will be - used to, among other things, throttle users based on their allocated quota.
    - original_url (string): Original URL to be shortened.
    - custom_alias (string): Optional custom key for the URL.
    - user_name (string): Optional user name to be used in the encoding.
    - expire_date (string): Optional expiration date for the shortened URL.
- Returns: (string)
    - A successful insertion returns the shortened URL; otherwise, it returns an error code.
- ``deleteURL(api_dev_key, url_key)``
    Where “url_key” is a string representing the shortened URL to be retrieved. A successful deletion returns ‘URL Removed’.
- How do we detect and prevent abuse? 
    - A malicious user can put us out of business by consuming all URL keys in the current design. To prevent abuse, we can limit users via their api_dev_key. Each api_dev_key can be limited to a certain number of URL creations and redirections per some time period (which may be set to a different duration per developer key).
