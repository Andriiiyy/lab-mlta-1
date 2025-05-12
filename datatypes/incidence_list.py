from datatypes.node import Node

class IncidenceList:
    def __init__(self, list_type: str) -> None:
        self.edge_list: list[list[int]] = []
        self.node_list: list[Node] = []
        allowed_types: list[str] = ["directed", "undirected"]
        if not list_type in allowed_types:
            raise TypeError("Invalid matrix type")
        self.list_type: str = list_type

    def add_node(self, node: Node) -> None:
        self.node_list.append(node)

    def check_edge(self, src: int, dest: int) -> int:
        for index, edge in enumerate(self.edge_list):
            if edge == [src, dest]:
                return index
        return -1

    def add_edge(self, src: int, dest: int) -> None:
        if not (0 <= src < len(self.node_list)) or not (0 <= dest < len(self.node_list)):
            raise IndexError("Index is out of bounds")
        self.edge_list.append([src, dest])
        if self.list_type == "undirected":
            self.edge_list.append([dest, src])

    def del_edge(self, src: int, dest: int):
        index: int = self.check_edge(src, dest)
        if index != -1:
            self.edge_list.pop(index)
        
    def print(self) -> None:
        for edge in self.edge_list:
            print(self.node_list[edge[0]].data, self.node_list[edge[1]].data, sep=" -> ")
