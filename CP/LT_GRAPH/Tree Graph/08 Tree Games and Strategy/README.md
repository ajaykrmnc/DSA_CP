# Tree Games and Strategy

Use this subsection when players, agents, or adversaries move on a tree and the result depends on distances or turn order.

## When To Use

- The statement has two players moving along tree edges with alternating turns or simultaneous movement.
- You need to decide who wins, who catches whom, or whether escape is possible.
- Rewards or profits depend on which player reaches a node first.
- The key comparison is between distances from two starting nodes.
- The tree diameter limits whether a player can force a win.

## First Choice

- Precompute distances from each relevant starting node with DFS/BFS.
- Compare arrival times for each node when profit or ownership depends on who arrives first.
- Use diameter when a player can choose any farthest escape route.
- Convert game rules into distance inequalities before coding.

## Do Not Use This Section When

- The problem is a general graph game with cycles and repeated states.
- There are no adversarial choices or timing rules: use the more direct tree distance/DP subsection.
