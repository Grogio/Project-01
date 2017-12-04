from DictionaryBST_LazyDel import DictBinaryTreeLazyDel
from time import time

def testDictLazyDel(steps):
    diz = DictBinaryTreeLazyDel()

    print("Test di DictBinaryTreeLazyDel (tempo medio per ogni operazione, calcolato su 2000 chiamate)")

    start = time()
    for i in range (steps):
        diz.insert(2*i, i)
    elapsed = time() - start
    print("Tempo medio insert nuovi elementi:", elapsed / steps)

    start = time()
    for i in range (steps):
        diz.search(2*i)
    elapsed = time() - start
    print("Tempo medio search elementi esistenti:", elapsed / steps)

    start = time()
    for i in range (steps):
        diz.search(2*i + 1)
    elapsed = time() - start
    print("Tempo medio search elementi non esistenti:", elapsed / steps)

    start = time()
    for i in range (steps):
        diz.boolDelete(2*i)
    elapsed = time() - start
    print("Tempo medio boolDelete elementi non eliminati:", elapsed / steps)

    start = time()
    for i in range (steps):
        diz.boolDelete(2*i)
    elapsed = time() - start
    print("Tempo medio boolDelete elementi già eliminati:", elapsed / steps)

    start = time()
    for i in range (steps):
        diz.search(2*i)
    elapsed = time() - start
    print("Tempo medio search elementi eliminati:", elapsed / steps)

    start = time()
    for i in range (steps):
        diz.insert(2*i, i + steps)
    elapsed = time() - start
    print("Tempo medio insert elementi da sostituire:", elapsed / steps)

if __name__ == "__main__":
    steps = 2000
    testDictLazyDel(steps)
