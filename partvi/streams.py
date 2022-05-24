# File streams.py (2.X + 3.X)
from __future__ import print_function

class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)
        def converter(self, data):
            assert False, 'converter must be defined'