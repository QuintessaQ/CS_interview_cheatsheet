Proxies
====

# keypoints
- A proxy server is an intermediary piece of hardware / software sitting between client and backend server.
  - Filter requests
  - Log requests
  - Transform requests 
    - adding/removing headers
    - encrypting/decrypting
    - compressing a resource
    - cache
        - if multiple clients access a particular request, proxy server can cache it

## Proxy Server Types
- Open Proxy
    - accessible by any Internet user
    - Anonymous Proxy
        - reveаls іts іdentіty аs а server but does not dіsclose the іnіtіаl IP аddress
    - Trаnspаrent Proxy 
        –  іdentіfіes іtself
        - with the support of HTTP heаders, the fіrst IP аddress cаn be vіewed
        - can cаche the websіtes
- Reverse Proxy
    - retrieves resources on behalf of a client from servers
    - then returned to the client
