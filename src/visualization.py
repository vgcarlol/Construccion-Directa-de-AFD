import os
import logging
from graphviz import Digraph

GRAPHVIZ_PATH = os.path.abspath("./Graphviz/bin") # DIRECTAMENTE EN LA CARPETA POR ERRORES EN MI COMPUTADOR
os.environ["PATH"] += os.pathsep + GRAPHVIZ_PATH

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def visualize_afd(afd, filename='afd_output'):
    dot = Digraph()

    def add_nodes(state, visited):
        if id(state) in visited:
            return
        visited.add(id(state))
        dot.node(str(id(state)), shape="doublecircle" if state.is_final else "circle")
        logging.debug(f"Agregando nodo: {state}")

        for symbol, target in state.transitions.items():
            dot.edge(str(id(state)), str(id(target)), label=symbol)
            logging.debug(f"Agregando transición: {id(state)} --{symbol}--> {id(target)}")
            add_nodes(target, visited)

    add_nodes(afd, set())

    dot.render(filename, format='png', view=True)