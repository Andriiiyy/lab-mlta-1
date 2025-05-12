from datatypes.node import Node
from datatypes.adjacency_list import AdjacencyList
import networkx as nx
import matplotlib.pyplot as plt

class IncidenceMatrix:
    def __init__(self, matrix_type: str):
        allowed_types: list[str] = ["directed", "undirected"]
        if not matrix_type in allowed_types:
            raise TypeError("Invalid matrix type")

        self.matrix_type = matrix_type
        self.node_list: list[Node] = []
        self.edge_list: list[tuple[int, int]] = []
        self.imatrix: list[list[int]] = []

    def add_node(self, node: Node) -> None:
        self.node_list.append(node)
        if self.edge_list:
            self.imatrix.append([0] * len(self.imatrix[0]))

    def add_edge(self, src: int, dest:int) -> None:
        if not self.imatrix:
            self.imatrix = [[] for _ in range(len(self.node_list))]
        if (0 <= src < len(self.node_list)) and (0 <= dest < len(self.node_list)):
            if not (src, dest) in self.edge_list:
                self.edge_list.append((src, dest))
                for row in self.imatrix:
                    row.append(0)
            edge_index: int = self.edge_list.index((src, dest))
            if self.matrix_type == "directed":
                self.imatrix[src][edge_index] = -1
                self.imatrix[dest][edge_index] = 1
            else:
                self.imatrix[src][edge_index], self.imatrix[dest][edge_index] = 1, 1

    def print(self):
        print(end="\t")
        for edge in self.edge_list:
            print(edge, end="\t")
        print(end="\n")

        for i in range(len(self.imatrix)):
            print(self.node_list[i].data, end="\t")
            for j in range(len(self.imatrix[i])):
                print(f"{self.imatrix[i][j]}", sep=" ", end="\t\t")
            print(end="\n")

    def to_edge_list(self) -> list[tuple[int, int]]:
        return self.edge_list

    def to_adjacency_list(self) -> AdjacencyList:
        adjacency_list = AdjacencyList(self.matrix_type)
        for node in self.node_list:
            adjacency_list.add_node(node)
        for edge_index, (src, dest) in enumerate(self.edge_list):
            adjacency_list.add_edge(src, dest)
            if self.matrix_type == "undirected" and not adjacency_list.check_edge(dest, src):
                adjacency_list.add_edge(dest, src)
        return adjacency_list

    def to_adjacency_matrix(self):
        from datatypes.adjacency_matrix import AdjacencyMatrix

        adj_matrix = AdjacencyMatrix(self.matrix_type)
        for node in self.node_list:
            adj_matrix.add_node(node)
        for edge_index in range(len(self.edge_list)):
            src, dest = -1, -1
            for i in range(len(self.imatrix)):
                if self.imatrix[i][edge_index] == 1:
                    if self.matrix_type == "directed":
                        dest = i
                    else:
                        if src == -1:
                            src = i
                        else:
                            dest = i
                elif self.imatrix[i][edge_index] == -1:
                    src = i
            if src != -1 and dest != -1:
                adj_matrix.add_edge(src, dest)

        return adj_matrix

    def to_networkx_graph(self) -> None:
        edge_list = self.to_edge_list()
        if self.matrix_type == "directed":
            G = nx.DiGraph()
        else:
            G = nx.Graph()
        G.add_edges_from(edge_list)
        mapping = {i: node.data for i, node in enumerate(self.node_list)}
        G = nx.relabel_nodes(G, mapping)
        plt.figure(figsize=(8, 6))
        nx.draw(G, with_labels=True, node_size=700,font_size=10, edge_color='black')
        plt.title("Graph Visualization")
        plt.show()
