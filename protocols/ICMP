# Common ICMP Messages and Their Meanings
## ICMP (Internet Control Message Protocol) has several types and codes that convey different kinds of messages. Here are some common ICMP message types:

### Echo Request (Type 8, Code 0)

Sent by a host to check if another host is reachable.
Commonly known as a "ping".

### Echo Reply (Type 0, Code 0)

Sent in response to an echo request.
Indicates that the destination host is reachable and operational.

### Destination Unreachable (Type 3)

Indicates that a destination is unreachable.
Common codes:
0: Network Unreachable
1: Host Unreachable
2: Protocol Unreachable
3: Port Unreachable
4: Fragmentation Needed and Don't Fragment was Set


### Source Quench (Type 4, Code 0)

Indicates that the source should reduce its transmission rate.
Used for congestion control (now largely deprecated).


### Redirect (Type 5)

Informs the sender about a better route for the destination.
Common codes:
0: Redirect Datagram for the Network
1: Redirect Datagram for the Host


### Time Exceeded (Type 11)

Indicates that the Time-to-Live (TTL) field of a packet expired in transit.
Common codes:
0: TTL expired in transit
1: Fragment reassembly time exceeded


### Parameter Problem (Type 12)

Indicates a problem with the header parameters.
Common codes:
0: Pointer indicates the error
1: Missing a required option
2: Bad length


### Timestamp Request (Type 13)

Requests the current time from the target host.


### Timestamp Reply (Type 14)

Sent in response to a timestamp request.
Contains the current time.