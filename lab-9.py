class IdentifierChecker:
    def __init__(self):
        # List of reserved keywords
        self.keywords = {
            "auto", "break", "case", "char", "const", "continue",
            "default", "do", "double", "else", "enum", "extern", "float",
            "for", "goto", "if", "inline", "int", "long", "register",
            "restrict", "return", "short", "signed", "sizeof", "static",
            "struct", "switch", "typedef", "union", "unsigned", "void",
            "volatile", "while", "_Alignas", "_Alignof", "_Atomic", "_Bool",
            "_Complex", "_Generic", "_Imaginary", "_Noreturn",
            "_Static_assert", "_Thread_local"
        }

    def is_valid_identifier(self, identifier):
        """Check if the given identifier is valid."""
        if not identifier:
            return False
        if identifier in self.keywords:
            return False
        if not (identifier[0].isalpha() or identifier[0] == '_'):
            return False
        for char in identifier[1:]:
            if not (char.isalnum() or char == '_'):
                return False
        return True

# Example usage
if __name__ == "__main__":
    checker = IdentifierChecker()
    identifiers = ["read", "_validIdentifier1", "float", "for", "int", "name"]
    for identifier in identifiers:
        if checker.is_valid_identifier(identifier):
            print(f"'{identifier}' is a valid identifier.")
        else:
            print(f"'{identifier}' is not a valid identifier.")
