class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    def printNumInstances():
        print('Number of instances created: %s' % Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)


class Sub(Spam):
    def printNumInstances():
        print('Extra stuf...')
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)
