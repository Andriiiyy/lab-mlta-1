from datatypes.incidence_matrix import IncidenceMatrix
from utils.graph_utils import create_undirected_graph, create_directed_graph

def undirected():
    print("Створення  НЕНАПРАВЛЕНОЇ матриці інцидентності")
    inc_matrix: IncidenceMatrix = create_undirected_graph(IncidenceMatrix)
    inc_matrix.print()
    print("\nПеретворення матриці інцидентності в матрицю суміжності")
    inc_matrix.to_adjacency_matrix().print()
    print("\nПеретворення матриці інцидентності в список ребер")
    print(inc_matrix.to_edge_list())
    print("\nПеретворення матриці інцидентності в список суміжності")
    inc_matrix.to_adjacency_list().print()
    inc_matrix.to_networkx_graph()
    

def directed():
    print("Створення  НАПРАВЛЕНОЇ матриці інцидентності")
    inc_matrix: IncidenceMatrix = create_directed_graph(IncidenceMatrix)
    inc_matrix.print()
    print("\nПеретворення матриці інцидентності в матрицю суміжності")
    inc_matrix.to_adjacency_matrix().print()
    print("\nПеретворення матриці інцидентності в список ребер")
    print(inc_matrix.to_edge_list())
    print("\nПеретворення матриці інцидентності в список суміжності")
    inc_matrix.to_adjacency_list().print()
    inc_matrix.to_networkx_graph()
