class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    @staticmethod
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)


class Sub(Spam):
    @staticmethod
    def printNumInstances():
        print('Extra stuff...')
        Spam.printNumInstances()


class Other(Spam):
    pass


if __name__ == "__main__":
    a, b, c = Sub(), Sub(), Other()
    a.printNumInstances()
    Sub.printNumInstances()
    Spam.printNumInstances()
    c.printNumInstances()
