# Aho-Corasick

Aho-Corasick matches many patterns in one text in linear time after building an automaton.

## Use When

Use this when:

- many patterns must be searched in the same text;
- pattern count is large;
- trie alone is not enough because failed transitions matter.

## Core Structure

Each node stores:

```text
next[character]
link = failure link
output information
```

Failure link means:

```text
longest proper suffix of current string that is also a trie prefix
```

## Build Idea

1. Insert all patterns into a trie.
2. BFS from root.
3. Compute failure links.
4. Fill missing transitions using failure links.
5. During text scan, follow transitions and collect matches.

## Complexity

```text
build: O(total pattern length * alphabet)
scan:  O(text length + matches)
```

## Practice Problems

- CSES - Finding Patterns
- CSES - Counting Patterns
- CSES - Pattern Positions
- CSES - Word Combinations

