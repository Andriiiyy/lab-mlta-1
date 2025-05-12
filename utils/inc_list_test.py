from datatypes.incidence_list import IncidenceList
from utils.graph_utils import create_undirected_graph, create_directed_graph

def undirected():
    print("Створення  НЕНАПРАВЛЕНОГО списку ребер")
    inc_list: IncidenceList = create_undirected_graph(IncidenceList)
    inc_list.print()

def directed():
    print("Створення  НАПРАВЛЕНОГО списку ребер")
    inc_list: IncidenceList = create_directed_graph(IncidenceList)
    inc_list.print()

