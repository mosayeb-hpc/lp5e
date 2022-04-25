import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="specify a file[path] to see it's content ")
args = parser.parse_args()

f = open(args.file, 'r')
s = f.read()
print(s)
