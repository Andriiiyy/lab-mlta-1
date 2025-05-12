from datatypes.node import Node
from datatypes.incidence_matrix import IncidenceMatrix
from datatypes.adjacency_list import AdjacencyList
from datatypes.incidence_list import IncidenceList

class AdjacencyMatrix:
    def __init__(self, matrix_type: str):
        allowed_types: list[str] = ["directed", "undirected"]
        if not matrix_type in allowed_types:
            raise TypeError("Invalid matrix type")

        self.matrix_type = matrix_type
        self.node_list: list[Node] = []
        self.matrix = [[0] * 1 for _ in range(1)]

    def add_node(self, node: Node) -> None:
        if self.node_list:
            self.matrix.append([0] * len(self.matrix[0]))
            for row in self.matrix:
                row.append(0)
        self.node_list.append(node)

    def del_node(self, node_id: int) -> None:
        if node_id >= len(self.node_list) or node_id < 0:
            raise IndexError("Node index is out of bounds")
        self.node_list.pop(node_id)
        self.matrix.pop(node_id)
        for row in self.matrix:
            row.pop(node_id)

    def add_edge(self, src: int, dest: int) -> None:
        self.matrix[src][dest] = 1
        if self.matrix_type == "undirected":
            self.matrix[dest][src] = 1

    def print(self) -> None:
        print(end="\t")
        for node in self.node_list:
            print(node.data, end="\t")
        print(end="\n")

        for i in range(len(self.matrix)):
            print(self.node_list[i].data, end="\t")
            for j in range(len(self.matrix[i])):
                print(f"{self.matrix[i][j]}", sep=" ", end="\t")
            print(end="\n")

    def to_edge_list(self) -> list[tuple[int, ...]]:
        edge_list: list[tuple[int, ...]] = []
        for i, row in enumerate(self.matrix):
            for j, connection in enumerate(row):
                if connection != 0:
                    edge_list.append((i, j))

        if self.matrix_type == "undirected":
            edge_list = list(set([tuple(sorted(t)) for t in edge_list]))

        return edge_list

    def to_adjacency_list(self) -> AdjacencyList:
        edges: list[tuple[int,...]] = self.to_edge_list()
        result: AdjacencyList = AdjacencyList(self.matrix_type)
        for node in self.node_list:
            result.add_node(node)
        for edge in edges:
            result.add_edge(edge[0], edge[1])
        return  result

    def to_incidence_matrix(self) -> IncidenceMatrix:
        incidence_matrix: IncidenceMatrix = IncidenceMatrix(self.matrix_type)
        for node in self.node_list:
            incidence_matrix.add_node(node)
        for i, row in enumerate(self.matrix):
            for j, connection in enumerate(row):
                if connection != 0:
                    incidence_matrix.add_edge(i, j)
        return incidence_matrix
