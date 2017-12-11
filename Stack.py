class PilaArrayList:

    def __init__(self):
        self.s = []

    def push(self, elem):
        self.s.append(elem)

    def pop(self):
        if len(self.s) == 0:
            return None
        return self.s.pop()

    def top(self):
        if len(self.s) == 0:
            return None
        return self.s[-1]

    def isEmpty(self):
        return len(self.s) == 0

    def stampa(self):
        print("Elements in the collection (ordered): ")
        print(self.s)


# Test function
def testStack(s):
    if not isinstance(s, PilaArrayList):
        raise TypeError("Expected type was PilaArrayList.")

    for i in range (10):
        s.push(i)
    s.stampa()

    print("Top:", s.top())
    print("Pop:", s.pop())
    print("Top:", s.top())
    print("Pop:", s.pop())
    print("Pop:", s.pop())

    s.stampa()


if __name__ == "__main__":
    print("Test PilaArrayList")

    s = PilaArrayList()
    testStack(s)
   

# Giorgio Urbani 0241220
