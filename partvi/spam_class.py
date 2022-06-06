

class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    @classmethod
    def printNumInstances(cls):
        print("Number of instances created: %s %s"
              % (cls.numInstances, cls))


class Sub(Spam):
    @classmethod
    def printNumInstances(cls):
        print("Extra stuff..", cls)
        Spam.printNumInstances()


class Other(Spam):
    pass


if __name__ == "__main__":
    x, y = Sub(), Spam()
    x.printNumInstances()
    Sub.printNumInstances()
    y.printNumInstances()
    z = Other()
    z.printNumInstances()

    Spam.printNumInstances()
