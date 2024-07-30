class CommentChecker:
    def __init__(self):
        pass

    def is_within_comment(self, code, string):
        lines = code.split('\n')
        in_multiline_comment = False
        
        for line in lines:
            stripped_line = line.strip()

            # Check for single-line comment
            if '//' in stripped_line:
                comment_index = stripped_line.index('//')
                comment_part = stripped_line[comment_index:]
                if string in comment_part:
                    return True

            # Check for start of multi-line comment
            if '/*' in stripped_line:
                in_multiline_comment = True
                comment_index = stripped_line.index('/*')
                comment_part = stripped_line[comment_index:]
                if string in comment_part:
                    return True

            # Check for end of multi-line comment
            if '*/' in stripped_line:
                if in_multiline_comment:
                    comment_index = stripped_line.index('*/')
                    comment_part = stripped_line[:comment_index + 2]
                    if string in comment_part:
                        return True
                    in_multiline_comment = False
                    continue

            # Check for string within multi-line comment
            if in_multiline_comment:
                if string in stripped_line:
                    return True

        return False

# Example usage
if __name__ == "__main__":
    code = '''
    // This is a single-line comment
    int main() {
        printf("Hello, world!");  // This is an inline comment
        return 0;
    }
    '''

    multi_line_code = '''
    /*
    This is a multi-line comment
    spanning multiple lines
    */
    int main() {
        printf("Hello, world!");
        return 0;
    }
    '''

    checker = CommentChecker()
    string1 = "single-line comment"
    string2 = "multi-line comment"
    string3 = "not in comment"

    print(checker.is_within_comment(code, string1))   # Expected: True
    print(checker.is_within_comment(multi_line_code, string2))  # Expected: True
    print(checker.is_within_comment(code, string3))  # Expected: False
