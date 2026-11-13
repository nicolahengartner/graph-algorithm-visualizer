import pytest

from visualizer.model.graph import Graph


def test_add_edge_directed() -> None:
    g = Graph(directed=True)
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2, 5)
    assert g.neighbors(1) == {2: 5}
    assert g.neighbors(2) == {}


def test_add_edge_undirected() -> None:
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2, 5)
    assert g.neighbors(1) == {2: 5}
    assert g.neighbors(2) == {1: 5}


def test_add_edge_default_weight_is_one() -> None:
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2)
    assert g.neighbors(1) == {2: 1}


def test_add_edge_overwrites_weight() -> None:
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2, 5)
    g.add_edge(1, 2, 9)
    assert g.neighbors(1) == {2: 9}
    assert g.neighbors(2) == {1: 9}


def test_add_edge_unknown_node_raises() -> None:
    g = Graph()
    g.add_node(1)
    with pytest.raises(KeyError):
        g.add_edge(1, 2)
    with pytest.raises(KeyError):
        g.add_edge(2, 1)


def test_add_node_twice_keeps_edges() -> None:
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2, 5)
    g.add_node(1)
    assert g.neighbors(1) == {2: 5}


def test_remove_node_removes_incoming_edges_directed() -> None:
    g = Graph(directed=True)
    for n in (1, 2, 3):
        g.add_node(n)
    g.add_edge(1, 2)
    g.add_edge(3, 2)
    g.remove_node(2)
    assert g.neighbors(1) == {}
    assert g.neighbors(3) == {}
    assert sorted(g.nodes()) == [1, 3]


def test_remove_node_undirected() -> None:
    g = Graph()
    for n in (1, 2, 3):
        g.add_node(n)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.remove_node(2)
    assert g.neighbors(1) == {}
    assert g.neighbors(3) == {}
    assert sorted(g.nodes()) == [1, 3]


def test_remove_node_unknown_raises() -> None:
    g = Graph()
    with pytest.raises(KeyError):
        g.remove_node(1)


def test_remove_edge_keeps_other_edges() -> None:
    g = Graph()
    for n in (1, 2, 3):
        g.add_node(n)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.remove_edge(1, 2)
    assert g.neighbors(1) == {3: 1}
    assert g.neighbors(2) == {}
    assert g.neighbors(3) == {1: 1}


def test_remove_edge_missing_raises() -> None:
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    with pytest.raises(KeyError):
        g.remove_edge(1, 2)


def test_neighbors_returns_copy() -> None:
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2, 5)
    g.neighbors(1)[2] = 99
    assert g.neighbors(1) == {2: 5}


def test_neighbors_unknown_node_raises() -> None:
    g = Graph()
    with pytest.raises(KeyError):
        g.neighbors(1)

