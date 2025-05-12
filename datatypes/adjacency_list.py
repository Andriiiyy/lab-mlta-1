from datatypes.node import Node

class AdjacencyList:
    def __init__(self, list_type):
        allowed_types: list[str] = ['directed', 'undirected']

        if not list_type in allowed_types:
            raise TypeError("Invalid list type")

        self.list_type = list_type
        self.alist: list[list[Node]] = []

    def add_node(self, node: Node) -> None:
        current_list: list[Node] = [node]
        self.alist.append(current_list)

    def add_edge(self, src: int, dest: int) -> None:
        current_list: list[Node] = self.alist[src]
        dest_node: Node = self.alist[dest][0]
        current_list.append(dest_node)

        if self.list_type == "undirected":
            reverse_list: list[Node] = self.alist[dest]
            src_node: Node = self.alist[src][0]
            reverse_list.append(src_node)

    def check_edge(self, src: int, dest: int) -> bool:
        current_list: list[Node] = self.alist[src]
        dest_node: Node = self.alist[dest][0]
        for node in current_list:
            if node == dest_node:
                return True
        return False

    def print(self) -> None:
        for current_list in self.alist:
            for node in current_list:
                print(f"{node.data}", sep=" ", end=" -> ")
            print(end="\n")
