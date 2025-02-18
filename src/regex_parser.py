class RegexParser:
    precedence = {'*': 3, '+': 3, '.': 2, '|': 1, '(': 0, ')': 0}

    @staticmethod
    def add_concatenation_operators(regex):
        new_regex = ""
        for i in range(len(regex) - 1):
            new_regex += regex[i]
            if (regex[i].isalnum() or regex[i] in ['*', '+', ')']) and \
               (regex[i + 1].isalnum() or regex[i + 1] in ['(', '+']):
                new_regex += '.'
        new_regex += regex[-1]
        return new_regex

    @staticmethod
    def infix_to_postfix(regex):
        regex = RegexParser.add_concatenation_operators(regex)
        output = []
        stack = []

        for char in regex:
            if char.isalnum():  # Si es un símbolo alfanumérico (a-z, 0-9)
                output.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Eliminar '(' de la pila
            else:  # Operadores (*, ., |, +)
                while stack and RegexParser.precedence[char] <= RegexParser.precedence.get(stack[-1], 0):
                    output.append(stack.pop())
                stack.append(char)

        while stack:
            output.append(stack.pop())

        return ''.join(output)
