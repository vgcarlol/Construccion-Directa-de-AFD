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
        dot.node(str(id(state)), shape="circle")

        for symbol, targets in state.transitions.items():
            if isinstance(targets, list):
                targets = targets[0] 
            dot.edge(str(id(state)), str(id(targets)), label=symbol)
            add_nodes(targets, visited)

    add_nodes(afd, set())

    dot.render(filename, format='png', view=True)
