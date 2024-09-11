import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if not pattern:
        return True

    if not input_line:
        return False

    if pattern[0] == '^':
        return match_pattern(input_line, pattern[1:])

    elif pattern[0] == input_line[0]:
        return match_pattern(input_line[1:], pattern[1:])

    elif pattern[:2] == '\\d':
        return (input_line[0].isdigit() and match_pattern(input_line[1:], pattern[2:])) or match_pattern(input_line[1:], pattern)

    elif pattern[:2] == '\\w':
        return ((input_line[0].isalnum() or input_line[0] == '_') and match_pattern(input_line[1:], pattern[2:])) or match_pattern(input_line[1:], pattern)

    elif pattern[0] == '[' and ']' in pattern:
        if pattern[1] and pattern[1] == '^':
            idx = pattern.find("]")
            if idx == -1:
                return False
            newpattern = pattern[2:idx]
            for c in newpattern:
                if c in input_line:
                    return False
            return True

        for c in input_line:
            if c in pattern:
                return True
        return False
    else:
        return False

def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
