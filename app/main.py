import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line

    elif pattern[0] == '[' and pattern[-1] == ']':
        if pattern[1] and pattern[1] == '^':
            for c in input_line:
                if c in pattern:
                    return False
            return True

        for c in input_line:
            if c in pattern:
                return True
        return False

    elif pattern == '\\w':
        for c in input_line:
            if c.isalnum():
                return True
        return False

    elif pattern == '\\d':
        for c in input_line:
            if c.isdigit():
                return True
        return False

    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


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
