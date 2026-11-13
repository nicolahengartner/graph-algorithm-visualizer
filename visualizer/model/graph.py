class Graph:
    """Weighted graph stored as an adjacency dict.

    Internal structure: node -> {neighbor: weight}.
    """

    def __init__(self, directed: bool = False) -> None:
        self.directed = directed
        self.adj: dict[int, dict[int, int]] = {}

    def add_node(self, node: int) -> None:
        """Add a node. Adding an existing node does nothing."""
        if node not in self.adj:
            self.adj[node] = {}

    def remove_node(self, node: int) -> None:
        """Remove a node and ALL edges touching it (incoming and outgoing).
        Raises KeyError if the node does not exist."""
        if node not in self.adj:
            raise KeyError(node)
        del self.adj[node]
        for neighbors in self.adj.values():
            neighbors.pop(node, None)
                

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """Add the edge u -> v. If the graph is undirected, v -> u as well.
        Raises KeyError if u or v does not exist.
        Adding an existing edge overwrites its weight."""
        if u not in self.adj:
            raise KeyError(u)
        if v not in self.adj:
            raise KeyError(v)
        self.adj[u][v] = weight
        if not self.directed:
            self.adj[v][u] = weight

    def remove_edge(self, u: int, v: int) -> None:
        """Remove the edge u -> v (and v -> u if undirected).
        Raises KeyError if the edge does not exist."""
        if u not in self.adj:
            raise KeyError(u)
        if v not in self.adj:
            raise KeyError(v)
        del self.adj[u][v]
        if not self.directed:
            del self.adj[v][u]

    def neighbors(self, node: int) -> dict[int, int]:
        """Return {neighbor: weight} for the outgoing edges of node.
        Raises KeyError if the node does not exist."""
        if node not in self.adj:
            raise KeyError(node)
        return dict(self.adj[node])

    def nodes(self) -> list[int]:
        """Return all nodes of the graph as a list."""
        return list(self.adj)
        