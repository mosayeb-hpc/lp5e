class Spam:
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    @staticmethod
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)


if __name__ == "__main__":
    a, b, c = Spam(), Spam(), Spam()
    Spam.printNumInstances()
    a.printNumInstances()
