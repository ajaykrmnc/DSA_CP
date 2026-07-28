# HLD System Design

This folder contains high-level system design notes and a generated PDF.

## Systems Covered

| # | System | Main Themes |
|---:|---|---|
| 1 | [URL Shortener](01-url-shortener.md) | encoding, redirects, storage, caching, rate limits |
| 2 | [Rate Limiter](02-rate-limiter.md) | token bucket, sliding window, distributed counters |
| 3 | [Chat Messaging](03-chat-messaging.md) | WebSocket, delivery, fanout, ordering |
| 4 | [News Feed](04-news-feed.md) | feed generation, fanout, ranking, cache |
| 5 | [Video Streaming](05-video-streaming.md) | upload, transcoding, CDN, metadata |
| 6 | [Notification System](06-notification-system.md) | channels, retries, preferences, fanout |
| 7 | [Search Engine](07-search-engine.md) | crawling, indexing, ranking, query serving |
| 8 | [Distributed Cache](08-distributed-cache.md) | sharding, replication, eviction, consistency |
| 9 | [Object Storage](09-object-storage.md) | blob storage, metadata, durability, multipart upload |
| 10 | [Ride Sharing](10-ride-sharing.md) | matching, location indexing, dispatch, pricing |
| 11 | [Payment System](11-payment-system.md) | idempotency, ledger, reconciliation, webhooks |
| 12 | [Ticket Booking](12-ticket-booking.md) | inventory, locking, payment, concurrency |
| 13 | [Typeahead Suggestion](13-typeahead-suggestion.md) | trie, ranking, prefix index, cache |
| 14 | [Key Value Store](14-key-value-store.md) | replication, consistency, partitioning |
| 15 | [Metrics Monitoring](15-metrics-monitoring.md) | ingestion, aggregation, time series, alerting |

## How To Use These Notes

1. Start by writing requirements and scale assumptions.
2. Identify APIs and data model.
3. Draw the high-level architecture.
4. Discuss bottlenecks, consistency, failure modes, and tradeoffs.
5. End with observability and operational concerns.

## Reusable Design Patterns

| Pattern | Common Systems |
|---|---|
| Sharding | cache, key-value store, object storage, search |
| Fanout | chat, news feed, notifications |
| Idempotency | payments, booking, notifications |
| Distributed locking | booking, inventory, payment workflows |
| Queue-based async processing | video, notifications, search indexing |
| CDN/cache | video, URL shortener, search, typeahead |
| Event sourcing / ledger | payments, metrics, booking audit |

## Supporting Files

- [HLD-System-Design-Book.pdf](HLD-System-Design-Book.pdf)
- [build-pdf.sh](build-pdf.sh)
- [split-long-blocks.py](split-long-blocks.py)
- [keep-code-together.lua](keep-code-together.lua)

