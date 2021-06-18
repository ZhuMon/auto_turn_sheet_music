import sys

def base_tone(capo):
    base = [40, 45, 50, 55, 59, 64]
    base = base[::-1] # first to six
    return [b+capo for b in base]
    

def convert(string, pos, capo):
    base = base_tone(capo)

    return base[string-1]+pos


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} string pos capo")
        sys.exit(1)

    print(convert(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
