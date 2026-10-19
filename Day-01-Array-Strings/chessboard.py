import sys

def determine_color(s):
    col = ord(s[0].lower()) - ord('a')
    row = int(s[1]) - 1
    if (col + row) % 2 == 0:
        return "Black"
    else:
        return "White"

def main():
    s = sys.stdin.read().strip()
    if s:
        result = determine_color(s)
        print(result)

if __name__ == "__main__":
    main()
