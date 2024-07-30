class ShiftReduceParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.stack = []
        self.input_buffer = []

    def parse(self, tokens):
        self.input_buffer = tokens
        while self.input_buffer:
            self.shift()
            while self.reduce():
                pass
        return self.stack

    def shift(self):
        token = self.input_buffer.pop(0)
        self.stack.append(token)
        print(f"Shift: {token}, Stack: {self.stack}")

    def reduce(self):
        for lhs, rhs in self.grammar.items():
            if self.stack[-len(rhs):] == rhs:
                self.stack = self.stack[:-len(rhs)]
                self.stack.append(lhs)
                print(f"Reduce: {lhs} -> {rhs}, Stack: {self.stack}")
                return True
        return False

# Example usage
grammar = {
    'E': ['E', '+', 'T'],
    'E': ['T'],
    'T': ['T', '*', 'F'],
    'T': ['F'],
    'F': ['(', 'E', ')'],
    'F': ['id']
}

parser = ShiftReduceParser(grammar)
tokens = ['id', '+', 'id', '*', 'id']
parser.parse(tokens)

