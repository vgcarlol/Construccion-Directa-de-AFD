from collections import defaultdict

class State:
    def __init__(self, is_final=False):
        self.transitions = {}
        self.is_final = is_final

class DirectAFDConstructor:
    def __init__(self, regex_postfix):
        self.regex_postfix = regex_postfix
        self.states = []
        self.start_state = self.construct_afd()

    def construct_afd(self):
        stack = []

        for char in self.regex_postfix:
            if char.isalnum():
                start = State()
                end = State(is_final=True)
                start.transitions[char] = end
                stack.append((start, end))
            elif char == '.':  # Concatenación
                s1, e1 = stack.pop()
                s2, e2 = stack.pop()
                e2.transitions.update(s1.transitions)
                stack.append((s2, e1))
            elif char == '|':  # Alternancia (a|b)
                s1, e1 = stack.pop()
                s2, e2 = stack.pop()
                start = State()
                end = State(is_final=True)
                start.transitions['ε'] = [s2, s1]
                e1.transitions['ε'] = end
                e2.transitions['ε'] = end
                stack.append((start, end))
            elif char == '*':  # Cerradura de Kleene
                s, e = stack.pop()
                start = State()
                end = State(is_final=True)
                start.transitions['ε'] = [s, end]
                e.transitions['ε'] = [s, end]
                stack.append((start, end))
        
        start_state, final_state = stack.pop()
        final_state.is_final = True
        return start_state

    def get_afd(self):
        return self.start_state
