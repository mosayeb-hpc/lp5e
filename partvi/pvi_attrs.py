class Attrs(object):
    def __getattr__(self, name):
        print("args: (%s: %s)" % (self.__class__.__name__, name))

    def __setattr__(self, name, value):
        print("args: (%s: %s, %s)" % (
            self.__class__.__name__,
            name, value))
