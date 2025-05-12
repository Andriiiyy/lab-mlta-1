from datatypes.incidence_matrix import IncidenceMatrix
from datatypes.node import Node

def create_undirected_graph(method_class):
    graph = method_class("undirected")
    nodes = ["A", "B", "C", "D", "E", "F"]
    for node in nodes:
        graph.add_node(Node(node))

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 1)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)

    return graph

def create_directed_graph(method_class):
    graph = method_class("directed")
    nodes = ["A", "B", "C", "D", "E", "F"]
#             0    1    2    3    4    5
    for node in nodes:
        graph.add_node(Node(node))

    graph.add_edge(0, 0)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 1)
    graph.add_edge(1, 3)
    graph.add_edge(2, 2)
    graph.add_edge(2, 5)
    graph.add_edge(3, 3)
    graph.add_edge(3, 5)
    graph.add_edge(5, 4)

    return graph
