# src/visualization.py
import os
from graphviz import Digraph

GRAPHVIZ_PATH = os.path.abspath("./Graphviz/bin")
os.environ["PATH"] += os.pathsep + GRAPHVIZ_PATH


def visualize_afd(afd, filename='afd_output'):
    dot = Digraph()

    def add_nodes(state, visited):
        if id(state) in visited:
            return
        visited.add(id(state))
        dot.node(str(id(state)), shape="doublecircle" if state.is_final else "circle")

        for symbol, target in state.transitions.items():
            dot.edge(str(id(state)), str(id(target)), label=symbol)
            add_nodes(target, visited)

    add_nodes(afd, set())

    dot.render(filename, format='png', view=True)
