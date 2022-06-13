from __future__ import print_function


class FromatError(Exception):
    logfile = "formaterror.txt"

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at:', self.file, self.line, file=log)


def parser():
    raise FromatError(40, 'spam.txt')


if __name__ == "__main__":
    try:
        parser()
    except FromatError as exc:
        exc.logerror()
