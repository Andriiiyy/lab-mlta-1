from datatypes.adjacency_list import AdjacencyList
from utils.graph_utils import create_undirected_graph, create_directed_graph

def undirected():
    print("Створення  НЕНАПРАВЛЕНОГО списку суміжності")
    adj_list: AdjacencyList = create_undirected_graph(AdjacencyList)
    adj_list.print()

def directed():
    print("Створення  НАПРАВЛЕНОГО списку суміжності")
    adj_list: AdjacencyList = create_directed_graph(AdjacencyList)
    adj_list.print()
