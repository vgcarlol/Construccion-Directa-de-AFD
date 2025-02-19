class State:
    _id_counter = 0 

    def __init__(self, is_final=False):
        self.id = State._id_counter  
        State._id_counter += 1
        self.transitions = {}  
        self.is_final = is_final

    def __repr__(self):
        return f"State(id={self.id}, final={self.is_final}, transitions={list(self.transitions.keys())})"


class DirectAFDConstructor:
    def __init__(self, regex_postfix):
        self.regex_postfix = regex_postfix
        self.states = []
        self.start_state = self.construct_afd()

    def construct_afd(self):
        
        def new_state(is_final=False):
            state = State(is_final)
            self.states.append(state)
            return state

        stack = []

        for symbol in self.regex_postfix:
            if symbol.isalnum():  # Si es un carácter válido (a-z, 0-9)
                start = new_state()
                end = new_state(is_final=True)
                start.transitions[symbol] = end
                stack.append((start, end))
            elif symbol == '*':  # Cierre de Kleene
                if not stack:
                    raise ValueError(f"Error: * sin operandos en '{self.regex_postfix}'")
                start, end = stack.pop()
                loop = new_state()
                loop.transitions.update(start.transitions)
                end.transitions['ε'] = loop  # ε-transición para cerrar ciclo
                loop.transitions['ε'] = end
                stack.append((loop, end))


            elif symbol == '|':  # Unión
                if len(stack) < 2:
                    raise ValueError(f"Error: | sin suficientes operandos en '{self.regex_postfix}'")
                s2_start, s2_end = stack.pop()
                s1_start, s1_end = stack.pop()
                start = new_state()
                end = new_state(is_final=True)
                start.transitions['ε'] = [s1_start, s2_start]
                s1_end.transitions['ε'] = end
                s2_end.transitions['ε'] = end
                stack.append((start, end))
            elif symbol == '.':  # Concatenación
                if len(stack) < 2:
                    raise ValueError(f"Error: . sin suficientes operandos en '{self.regex_postfix}'")
                s2_start, s2_end = stack.pop()
                s1_start, s1_end = stack.pop()
                
                # Conectar correctamente los estados finales e iniciales
                s1_end.transitions.update(s2_start.transitions)  # Transiciones correctas
                
                # Asegurar que el estado final no se mezcle con otro
                stack.append((s1_start, s2_end))
                    

        if len(stack) != 1:
            raise ValueError(f"Error: Expresión postfix mal formada '{self.regex_postfix}'")

        start, end = stack.pop()
        return start

    def get_afd(self):
        return self.start_state
