class IntermediateCodeGenerator:
    def __init__(self):
        self.temp_counter = 0
        self.instructions = []
        self.label_counter = 0

    def generate_temp(self):
        """Generate a new temporary variable name."""
        self.temp_counter += 1
        return f"t{self.temp_counter - 1}"

    def generate_label(self):
        """Generate a new label name."""
        self.label_counter += 1
        return f"L{self.label_counter - 1}"

    def add_instruction(self, instruction):
        """Add an instruction to the list of instructions."""
        self.instructions.append(instruction)

    def generate_code(self, ast):
        """Generate intermediate code from the AST."""
        self.visit(ast)
        return self.instructions

    def visit(self, node):
        """Dispatch method for visiting AST nodes."""
        if isinstance(node, BinOp):
            return self.visit_binop(node)
        elif isinstance(node, Num):
            return node.value
        elif isinstance(node, Variable):
            return node.name
        elif isinstance(node, TypeConversion):
            return self.visit_type_conversion(node)

    def visit_binop(self, node):
        """Handle binary operations."""
        left = self.visit(node.left)
        right = self.visit(node.right)
        result = self.generate_temp()
        self.add_instruction(f"{result} = {left} {node.op} {right}")
        return result

    def visit_type_conversion(self, node):
        """Handle type conversion operations."""
        operand = self.visit(node.operand)
        result = self.generate_temp()
        self.add_instruction(f"{result} = ({node.target_type}) {operand}")
        return result

class ASTNode:
    """Base class for all AST nodes."""
    pass

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(ASTNode):
    def __init__(self, value):
        self.value = value

class Variable(ASTNode):
    def __init__(self, name):
        self.name = name

class TypeConversion(ASTNode):
    def __init__(self, operand, target_type):
        self.operand = operand
        self.target_type = target_type

# Example usage
if __name__ == "__main__":
    # Constructing AST for the expression: (2 + 6.0) * 3
    ast = BinOp(
        left=BinOp(left=Num(7), op='+', right=TypeConversion(Num(5.0), "int")),
        op='+',
        right=Num(3)
    )

    # Generate intermediate code
    generator = IntermediateCodeGenerator()
    intermediate_code = generator.generate_code(ast)

    # Print intermediate code
    for instruction in intermediate_code:
        print(instruction)
