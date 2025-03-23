# Tests simple, undirected, unweighted graphs.
# CSC 202, Lab 10
# Given tests, Summer '24

import unittest
from array_list import size as lsize, get as lget
from dictionary import size as dsize, get as dget
from graph import *


class TestGraph(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing graph equality and representation"

        graph = Graph()

        self.assertEqual(graph, graph, msg)
        self.assertEqual(repr(graph), "Graph(%r, 0)" % graph.matrix, msg)

    def test02_add(self):
        msg = "Testing adding vertices and edges to graphs"

        graph = Graph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v3")
        add_edge(graph, "v1", "v3")
        add_vertex(graph, "v0")
        add_vertex(graph, "v2")
        add_edge(graph, "v0", "v1")
        add_edge(graph, "v0", "v2")
        add_edge(graph, "v0", "v3")
        add_edge(graph, "v2", "v3")

        self.assertEqual(order(graph), 4, msg)
        self.assertEqual(size(graph), 5, msg)

        self.assertEqual(dsize(dget(graph.matrix, "v0")), 3, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v0"), "v0"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v0"), "v1"), 1, msg)
        self.assertEqual(dget(dget(graph.matrix, "v0"), "v2"), 1, msg)
        self.assertEqual(dget(dget(graph.matrix, "v0"), "v3"), 1, msg)

        self.assertEqual(dsize(dget(graph.matrix, "v1")), 2, msg)
        self.assertEqual(dget(dget(graph.matrix, "v1"), "v0"), 1, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v1"), "v1"), msg)
        self.assertIsNone(dget(dget(graph.matrix, "v1"), "v2"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v1"), "v3"), 1, msg)

        self.assertEqual(dsize(dget(graph.matrix, "v2")), 2, msg)
        self.assertEqual(dget(dget(graph.matrix, "v2"), "v0"), 1, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v2"), "v1"), msg)
        self.assertIsNone(dget(dget(graph.matrix, "v2"), "v2"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v2"), "v3"), 1, msg)

        self.assertEqual(dsize(dget(graph.matrix, "v3")), 3, msg)
        self.assertEqual(dget(dget(graph.matrix, "v3"), "v0"), 1, msg)
        self.assertEqual(dget(dget(graph.matrix, "v3"), "v1"), 1, msg)
        self.assertEqual(dget(dget(graph.matrix, "v3"), "v2"), 1, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v3"), "v3"), msg)

    def test03_remove(self):
        msg = "Testing removing vertices and edges from graphs"

        graph = Graph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v3")
        add_edge(graph, "v1", "v3")
        add_vertex(graph, "v0")
        add_vertex(graph, "v2")
        add_edge(graph, "v0", "v1")
        add_edge(graph, "v0", "v2")
        add_edge(graph, "v0", "v3")
        add_edge(graph, "v2", "v3")
        remove_vertex(graph, "v2")
        remove_edge(graph, "v3", "v0")

        self.assertEqual(order(graph), 3, msg)
        self.assertEqual(size(graph), 2, msg)
        self.assertIsNone(dget(graph.matrix, "v2"), msg)

        self.assertEqual(dsize(dget(graph.matrix, "v0")), 1, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v0"), "v0"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v0"), "v1"), 1, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v0"), "v2"), msg)
        self.assertIsNone(dget(dget(graph.matrix, "v0"), "v3"), msg)

        self.assertEqual(dsize(dget(graph.matrix, "v1")), 2, msg)
        self.assertEqual(dget(dget(graph.matrix, "v1"), "v0"), 1, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v1"), "v1"), msg)
        self.assertIsNone(dget(dget(graph.matrix, "v1"), "v2"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v1"), "v3"), 1, msg)

        self.assertEqual(dsize(dget(graph.matrix, "v3")), 1, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v3"), "v0"), msg)
        self.assertEqual(dget(dget(graph.matrix, "v3"), "v1"), 1, msg)
        self.assertIsNone(dget(dget(graph.matrix, "v3"), "v2"), msg)
        self.assertIsNone(dget(dget(graph.matrix, "v3"), "v3"), msg)

    def test04_path(self):
        msg = "Testing finding shortest paths in graphs"

        graph = Graph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v3")
        add_edge(graph, "v1", "v3")
        add_vertex(graph, "v0")
        add_vertex(graph, "v2")
        add_edge(graph, "v0", "v1")
        add_edge(graph, "v0", "v2")
        add_edge(graph, "v0", "v3")
        add_edge(graph, "v2", "v3")
        lst = path(graph, "v2", "v1")

        self.assertEqual(lsize(lst), 3, msg)
        self.assertEqual(lget(lst, 0), "v2", msg)
        self.assertIn(lget(lst, 1), {"v0", "v3"}, msg)
        self.assertEqual(lget(lst, 2), "v1", msg)

    def test05_KeyErrors(self):
        msg = "Testing all key errors"

        graph = Graph()

        with self.assertRaises(KeyError, msg = msg):
            add_edge(graph, "v1", "v3")
        with self.assertRaises(KeyError, msg = msg):
            remove_edge(graph, "v1", "v3")
        with self.assertRaises(KeyError, msg=msg):
            remove_vertex(graph, "v1")

    def test06_key_errors(self):
        msg = "Testing path key errors"

        graph = Graph()
        add_vertex(graph, "v1")
        add_vertex(graph, "v2")

        with self.assertRaises(ValueError, msg = msg):
            path(graph, "v1", "v2")

    def test08_key_errors(self):
        msg = "Testing path key errors"

        graph = Graph()

        with self.assertRaises(KeyError, msg = msg):
            path(graph, "v1", "v2")

    def test07_key_errors(self):
        msg = "Testing add_vertex key errors"

        graph = Graph()
        add_vertex(graph, "v1")

        with self.assertRaises(KeyError, msg = msg):
            add_vertex(graph, "v1")

if __name__ == "__main__":
    unittest.main()
