from datatypes.adjacency_matrix import AdjacencyMatrix
from utils.graph_utils import create_undirected_graph, create_directed_graph

def undirected():
    print("Створення  НЕНАПРАВЛЕНОЇ матриці суміжності")
    adj_matrix: AdjacencyMatrix = create_undirected_graph(AdjacencyMatrix)
    adj_matrix.print()
    print("\nПеретворення матриці суміжності в матрицю інцидентності")
    adj_matrix.to_incidence_matrix().print()
    print("\nПеретворення матриці суміжності в список ребер")
    print(adj_matrix.to_edge_list())
    print("\nПеретворення матриці суміжності в список суміжності")
    adj_matrix.to_adjacency_list().print()

def directed():
    print("Створення  НАПРАВЛЕНОЇ матриці суміжності")
    adj_matrix: AdjacencyMatrix = create_directed_graph(AdjacencyMatrix)
    adj_matrix.print()
    print("\nПеретворення матриці суміжності в матрицю інцидентності")
    adj_matrix.to_incidence_matrix().print()
    print("\nПеретворення матриці суміжності в список ребер")
    print(adj_matrix.to_edge_list())
    print("\nПеретворення матриці суміжності в список суміжності")
    adj_matrix.to_adjacency_list().print()
