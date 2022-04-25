import sys


def countLines(file):
    file.seek(0)
    return sum(1 for x in file)

def countChars(file):
    file.seek(0)
    return sum(len(line) for line in file) 


def countBytes(file):
    file.seek(0)
    return sum(len(line.encode()) for line in file)


def test(name):
    F = open(name)
    return countLines(F), countChars(F), countBytes(F)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(test(sys.argv[1]))
    else:
        print(test(sys.argv[0]))
