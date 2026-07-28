# LLD Interview Notes

This folder contains low-level design problems with object modeling, APIs, classes, responsibilities, and extensibility points.

## Problems Covered

| # | Problem | Main Design Focus |
|---:|---|---|
| 1 | [Rate Limiter](01-rate-limiter.md) | strategy pattern, counters, concurrency |
| 2 | [In-Memory Cache](02-in-memory-cache.md) | eviction policy, storage, generics |
| 3 | [Pub Sub System](03-pub-sub-system.md) | topics, subscribers, dispatch |
| 4 | [Task Scheduler](04-task-scheduler.md) | scheduling, priority, workers |
| 5 | [File System](05-file-system.md) | composite pattern, metadata, paths |
| 6 | [Connection Pool](06-connection-pool.md) | pooling, lifecycle, thread safety |
| 7 | [Logging Framework](07-logging-framework.md) | chain of responsibility, appenders, levels |
| 8 | [Elevator System](08-elevator-system.md) | state machine, scheduling, commands |
| 9 | [Parking Lot](09-parking-lot.md) | entities, allocation, pricing |
| 10 | [Library Management](10-library-management.md) | catalog, borrowing, users |
| 11 | [Online Chess](11-online-chess.md) | game rules, pieces, board state |
| 12 | [Notification System](12-notification-system.md) | channels, templates, retries |
| 13 | [API Gateway](13-api-gateway.md) | routing, auth, throttling |
| 14 | [Search Autocomplete](14-search-autocomplete.md) | trie, ranking, updates |
| 15 | [URL Shortener](15-url-shortener.md) | encoding, storage, redirects |
| 16 | [Order Management](16-order-management.md) | order lifecycle, inventory, payment |
| 17 | [Movie Ticket Booking](17-movie-ticket-booking.md) | seat locking, booking flow, payment |
| 18 | [Vending Machine](18-vending-machine.md) | state pattern, inventory, payment |
| 19 | [Distributed Lock](19-distributed-lock.md) | lease, expiry, fencing token |
| 20 | [Collaborative Editor](20-collaborative-editor.md) | operations, conflict handling, sessions |

## Interview Flow

1. Clarify requirements and out-of-scope behavior.
2. Identify entities and relationships.
3. Define core APIs.
4. Model classes and responsibilities.
5. Discuss design patterns, concurrency, and extensibility.
6. Walk through one or two important flows.
7. Call out edge cases and failure handling.

## Common Design Patterns

| Pattern | Where It Appears |
|---|---|
| Strategy | rate limiter algorithms, cache eviction, pricing |
| Factory | notification channels, pieces, payment methods |
| Observer | pub-sub, notification, collaborative editor |
| State | vending machine, elevator, order lifecycle |
| Composite | file system, menu/category trees |
| Chain of Responsibility | logging framework, gateway filters |
| Repository | storage layer for users, orders, bookings |

## Extra Index

- [Tier 1 LLD Interview Questions](lld-interview-questions-tier1.md)

