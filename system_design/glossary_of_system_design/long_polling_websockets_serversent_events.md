Long-Polling vs WebSockets vs Server-Sent Events
====

# keypoints
- communication protocols 
    - long-polling
    - WebSockets
    - Server-Sent Events
    - between a client like a web browser and a web server
    - sequence of event for regular HTTP request
        - client opens a connections, request data from server
        - server calculates reponse
        - server sends response back to the client

## Ajax Polling
- client repeatedly polls/requests a server for data
- If no data is available, an empty response is returned
- steps
    - client opens a connection, requests data from the server using regular HTTP.
    - requested webpage sends requests to the server at regular intervals (e.g., 0.5 seconds).
    - server calculates the response and sends it back
    - client repeats the above three steps periodically 
- problem
    - client keeps asking the server for new data, a lot of responses are empty -> HTTP overhead

## HTTP Long-Polling
- server push information to client whenever the data is available. 
- client requests as in normal polling, but expect server may not respond immediatey
- if server has no data available, then hold request instead of sending empty response until a timeout
- once data available, full response sent
- client immediately re-request, so server always have a waiting request
- client has to reconnect periodically after connection closed due to timeouts

## WebSockets
- persistent connection between client adn server
- both parties can send data at any time
- establishes WebSocket connection througj WebSocket handshake
    - if succeeds, client server can exchange data
    - enables communication with low overheads
    - real-time data transfer

## Server-Sent Events (SSEs)
- client establishes a persistent & long-term connection with the server
- client require another tech/protocol to send data to server
- steps
    - client request data using regular HTTP
    - request webpage opens a connections to server
    - server sends data to client if new info available
- best when real-time traffic needed
- or server generate data in loop

# text
- Long-Polling, WebSockets, and Server-Sent Events are popular communication protocols between a client like a web browser and a web server. First, let’s start with understanding what a standard HTTP web request looks like. Following are a sequence of events for regular HTTP request:
    - The client opens a connection and requests data from the server.
    - The server calculates the response.
    - The server sends the response back to the client on the opened request.
![HTTP_protocol](../images/HTTP_protocol.png)

## Ajax Polling
- Polling is a standard technique used by the vast majority of AJAX applications. The basic idea is that the client repeatedly polls (or requests) a server for data. The client makes a request and waits for the server to respond with data. If no data is available, an empty response is returned.
    - The client opens a connection and requests data from the server using regular HTTP.
    - The requested webpage sends requests to the server at regular intervals (e.g., 0.5 seconds).
    - The server calculates the response and sends it back, just like regular HTTP traffic.
    - The client repeats the above three steps periodically to get updates from the server.
- The problem with Polling is that the client has to keep asking the server for any new data. As a result, a lot of responses are empty, creating HTTP overhead.
![Ajax Polling Protocol](../images/ajax.png)

## HTTP Long-Polling
- This is a variation of the traditional polling technique that allows the server to push information to a client whenever the data is available. With Long-Polling, the client requests information from the server exactly as in normal polling, but with the expectation that the server may not respond immediately. That’s why this technique is sometimes referred to as a “Hanging GET”.
    - If the server does not have any data available for the client, instead of sending an empty response, the server holds the request and waits until some data becomes available.
    - Once the data becomes available, a full response is sent to the client. The client then immediately re-request information from the server so that the server will almost always have an available waiting request that it can use to deliver data in response to an event.
- The basic life cycle of an application using HTTP Long-Polling is as follows:
    - The client makes an initial request using regular HTTP and then waits for a response.
    - The server delays its response until an update is available or a timeout has occurred.
    - When an update is available, the server sends a full response to the client.
    - The client typically sends a new long-poll request, either immediately upon receiving a response or after a pause to allow an acceptable latency period.
    - Each Long-Poll request has a timeout. The client has to reconnect periodically after the connection is closed due to timeouts.
![Long Polling Protocol](../images/long_polling.png)

## WebSockets
- WebSocket provides Full duplex communication channels over a single TCP connection. It provides a persistent connection between a client and a server that both parties can use to start sending data at any time. The client establishes a WebSocket connection through a process known as the WebSocket handshake. If the process succeeds, then the server and client can exchange data in both directions at any time. The WebSocket protocol enables communication between a client and a server with lower overheads, facilitating real-time data transfer from and to the server. This is made possible by providing a standardized way for the server to send content to the browser without being asked by the client and allowing for messages to be passed back and forth while keeping the connection open. In this way, a two-way (bi-directional) ongoing conversation can take place between a client and a server.
![WebSockets Protocol](../images/websockets.png)

## Server-Sent Events (SSEs)
- Under SSEs the client establishes a persistent and long-term connection with the server. The server uses this connection to send data to a client. If the client wants to send data to the server, it would require the use of another technology/protocol to do so.
    - Client requests data from a server using regular HTTP.
    - The requested webpage opens a connection to the server.
    - The server sends the data to the client whenever there’s new information available.
- SSEs are best when we need real-time traffic from the server to the client or if the server is generating data in a loop and will be sending multiple events to the client.
![Server Sent Events Protocol](../images/sse.png)