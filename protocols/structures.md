# Examples of Header Fields in Different Protocols

## TCP (Transmission Control Protocol)
Source Port: Identifies the sending port.
Destination Port: Identifies the receiving port.
Sequence Number: Keeps track of the order of packets.
Acknowledgment Number: Indicates the next expected byte.
Data Offset: Specifies the size of the TCP header.
Reserved: Reserved for future use.
Flags: Control bits such as SYN, ACK, FIN, RST, PSH, URG.
Window Size: Flow control, specifies the size of the sender’s receive window.
Checksum: Error-checking of the header and payload.
Urgent Pointer: Indicates that certain data is urgent.
Options: Additional TCP options, such as Maximum Segment Size (MSS).

## IP (Internet Protocol)
Version: IP version (e.g., IPv4 or IPv6).
Header Length: Length of the IP header.
Type of Service (ToS): Quality of service control.
Total Length: Length of the entire packet (header + data).
Identification: Identifies the fragments of one datagram.
Flags: Controls or indicates if fragmentation is allowed.
Fragment Offset: Indicates the position of the fragment in the original packet.
Time to Live (TTL): Limits the packet's lifetime.
Protocol: Specifies the next level protocol (e.g., TCP, UDP).
Header Checksum: Error-checking of the header.
Source IP Address: IP address of the sender.
Destination IP Address: IP address of the receiver.
Options: Additional options such as security settings.

## HTTP (HyperText Transfer Protocol)
Method: Specifies the request method (e.g., GET, POST).
URI: Uniform Resource Identifier of the resource.
HTTP Version: Version of the HTTP protocol.
Status Code: Status of the response (e.g., 200 OK).
Headers: Key-value pairs (e.g., Host, Content-Type, User-Agent).
Body: The actual data being sent or received.

## DNS (Domain Name System)
1. ID: A 16-bit identifier assigned by the program that generates any kind of query.
 This identifier is copied in the corresponding reply to facilitate matching of requests and replies.
2. Flags: A 16-bit field that contains various flags and codes:
QR: Query/Response flag (1 bit) - 0 for query, 1 for response.
Opcode: Specifies the kind of query (4 bits) - usually 0 (standard query).
AA: Authoritative Answer (1 bit).
TC: Truncation (1 bit) - indicates if the message was truncated.
RD: Recursion Desired (1 bit).
RA: Recursion Available (1 bit).
Z: Reserved for future use (3 bits).
RCODE: Response code (4 bits) - indicates the status of the response.
QDCOUNT: Number of entries in the question section (16 bits).
ANCOUNT: Number of resource records in the answer section (16 bits).
NSCOUNT: Number of name server resource records in the authority records section (16 bits).
ARCOUNT: Number of resource records in the additional records section (16 bits).

## ARP (Address Resolution Protocol)
Hardware Type: Specifies the network link protocol type; for Ethernet, this is 1 (16 bits).
Protocol Type: Specifies the internetwork protocol for which the ARP request is intended; for IP, this is 0x0800 (16 bits).
Hardware Address Length: Length in bytes of a hardware address (8 bits).
Protocol Address Length: Length in bytes of a protocol address (8 bits).
Operation: Specifies the operation that the sender is performing: 1 for request, 2 for reply (16 bits).
Sender Hardware Address: The hardware address of the sender (48 bits for Ethernet).
Sender Protocol Address: The protocol address of the sender (32 bits for IPv4).
Target Hardware Address: The hardware address of the target (48 bits for Ethernet).
Target Protocol Address: The protocol address of the target (32 bits for IPv4).
