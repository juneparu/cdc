class FinalCodeGenerator:
    def __init__(self):
        self.instructions = []
        # Register mapping for temporary variables
        self.registers = {"t1": "R1", "t2": "R2", "t3": "R3", "t4": "R4"}

    def generate_final_code(self, intermediate_code):
        """Generate final assembly code from intermediate code."""
        for instruction in intermediate_code:
            self.translate_instruction(instruction)
        return self.instructions

    def translate_instruction(self, instruction):
        """Translate a single intermediate code instruction to assembly."""
        parts = instruction.split()
        temp_var = parts[0]
        op1 = parts[2]
        operator = parts[3]
        op2 = parts[4]

        # Load operands into registers
        if op1.isdigit():
            self.add_instruction(f"LOADI {op1}, {self.registers[temp_var]}")
        else:
            self.add_instruction(f"LOAD {op1}, {self.registers[temp_var]}")

        if op2.isdigit():
            self.add_instruction(f"LOADI {op2}, R3")
        else:
            self.add_instruction(f"LOAD {op2}, R3")

        # Perform the operation
        if operator == "+":
            self.add_instruction(f"ADD {self.registers[temp_var]}, R3")
        elif operator == "-":
            self.add_instruction(f"SUB {self.registers[temp_var]}, R3")
        elif operator == "*":
            self.add_instruction(f"MUL {self.registers[temp_var]}, R3")
        elif operator == "/":
            self.add_instruction(f"DIV {self.registers[temp_var]}, R3")

        # Store the result back to the temporary variable
        self.add_instruction(f"STORE {self.registers[temp_var]}, {temp_var}")

    def add_instruction(self, instruction):
        """Add an instruction to the list of final instructions."""
        self.instructions.append(instruction)

# Example usage
if __name__ == "__main__":
    # Example intermediate code
    intermediate_code = [
        "t1 = 7 - 5",
        "t3 = t1 * 5"
    ]

    # Generate final code
    final_generator = FinalCodeGenerator()
    final_code = final_generator.generate_final_code(intermediate_code)

    # Print final code
    for instruction in final_code:
        print(instruction)

