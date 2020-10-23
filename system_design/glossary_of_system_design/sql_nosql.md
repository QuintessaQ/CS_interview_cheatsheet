SQL vs. NoSQL
====
# keypoints
## sql (relational databases)
    - structured
    - have predefined schemas
        - e.g. phone books that store phone numbers and addresses
    - store data in rows and columns
        - row contains information about one entity
        - column contains separate data points
    
## NoSQL (non-relational databases)
    - unstructured, distributed
    - have a dynamic schema 
        - e.g file folders that hold everything from a person’s address to their Facebook ‘likes’ 

## Common types of NoSQL
### Key-value stores
- Array of key-value pairs. The "key" is an attribute name.
- Redis, Vodemort, Dynamo.

### Document databases
- Data is stored in documents.
- Documents are grouped in collections.
- Each document can have an entirely different structure.
- CouchDB, MongoDB.

### Wide-column / columnar databases
- Column families - containers for rows.
- No need to know all the columns up front.
- Each row can have different number of columns.
- Cassandra, HBase.

### Graph database
- Data is stored in graph structures
  - Nodes: entities
  - Properties: information about the entities
  - Lines: connections between the entities
- Neo4J, InfiniteGraph

## Differences between SQL and NoSQL
### Storage
- SQL: store data in tables.
- NoSQL: have different data storage models.
    - key-value
    - document
    - graph
    - columnar

### Schema
- SQL
  - Each record conforms to a fixed schema.
  - each row must have data for each column
  - Schema can be altered, but it requires modifying the whole database and going offline.
- NoSQL:
  - Schemas are dynamic.
  - each ‘row’ (or equivalent) doesn’t have to contain data for each ‘column.’

### Querying
- SQL
  - Use SQL (structured query language) for defining and manipulating the data.
- NoSQL
  - Queries are focused on a collection of documents.
  - UnQL (unstructured query language).
  - Different databases have different syntax.

### Scalability
- SQL
  - Vertically scalable (by increasing the horsepower: memory, CPU, etc) and expensive.
  - Horizontally scalable (across multiple servers); but it can be challenging and time-consuming.
- NoSQL
  - Horizontablly scalable (by adding more servers) and cheap.

### ACID
- Atomicity, consistency, isolation, durability
- SQL
  - ACID compliant
  - Data reliability
  - Gurantee of transactions
- NoSQL
  - Most sacrifice ACID compliance for performance and scalability.

## Which one to use?
### SQL
- Ensure ACID compliance.
  - Reduce anomalies.
  - Protect database integrity.
- Data is structured and unchanging.

### NoSQL
- Data has little or no structure.
- Make the most of cloud computing and storage.
  - Cloud-based storage requires data to be easily spread across multiple servers to scale up.
- Rapid development.
  - Frequent updates to the data structure.
