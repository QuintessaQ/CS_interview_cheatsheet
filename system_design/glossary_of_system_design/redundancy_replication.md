Redundancy & Replication
====
# keypoints
- Redundancy
    - **duplication of critical data or services** with the intention of increased reliability of the system.
    - remove single point of failure
    - if we have two servers and one fails, system can failover to the other one.
- primary-replica relationship
    - between the original and the copies. 
    - primary gets all updates
    - then ripple through to the replica servers
    - replca outputs message if received update successfully
- Shared-nothing architecture
  - Each node can operate independently of one another.
  - No central service managing state or orchestrating activities.
  - New servers can be added without special conditions or knowledge.
  - No single point of failure.


