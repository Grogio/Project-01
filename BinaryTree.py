from Stack import PilaArrayList

class BinaryNodeLazyDel:
      """Un nodo di un albero binario con Lazy Deletion e' un nodo che
         puo' essere segnato come "eliminato".
         Presenta dunque un attributo "status" che indica se e' o non e'
         segnato come "eliminato"."""
      def __init__(self, info):
        self. info = info
        self.status = True # False = "eliminato"
        self.father = None
        self.leftSon = None
        self.rightSon = None

class BinaryTree:
    """Un albero binario e' una struttura dati composta da nodi.
       Ogni nodo puo' avere al massimo due figli, uno destro e uno sinistro.
       I nodi che non hanno figli vengono detti foglie, mentre la radice e'
       il primo nodo dell'albero che non possiede un padre.
       Questa classe inizializza un albero con radice il nodo passato
       come argomento, oppure inizializza un albero vuoto se non viene passato
       alcun argomento."""
    def __init__(self, rootNode = None): 
        self.root = rootNode

    def insertAsLeftSubTree(self, father, subtree):
        """Permette di inserire la radice di un sottoalbero come figlio sinistro
           del nodo father."""
        son = subtree.root
        if son != None:
            son.father = father
        father.leftSon = son

    def insertAsRightSubTree(self, father, subtree):
        """Permette di inserire la radice di un sottoalbero come figlio destro
           del nodo father."""
        son = subtree.root
        if son != None:
            son.father = father
        father.rightSon = son

    def cutLeft(self, father):
        """Permette di rimuovere l'intero sottoalbero che parte dal figlio
           sinistro del nodo father"""
        son = father.leftSon
        newTree = BinaryTree(son)
        father.leftSon = None
        return newTree

    def cutRight(self, father):
        """Permette di rimuovere l'intero sottoalbero che parte dal figlio
           destro del nodo father"""
        son = father.rightSon
        newTree = BinaryTree(son)
        father.rightSon = None
        return newTree

    def cut(self, node):
        """Stacca e restituisce l'intero sottoalbero radicato in node. L'operazione
           cancella dall'albero il nodo node e tutti i suoi discendenti."""
        if node == None:
            return BinaryTree(None)
        if node.father == None:  # nodo radice
            self.root = None
            return BinaryTree(node)
        f = node.father
        if node.leftSon == None and node.rightSon == None:  # a leaf!
            if f.leftSon == node:
                f.leftSon = None
            else:
                f.rightSon = None
            return BinaryTree(node)
        elif f.leftSon == node:
            nt = self.cutLeft(f)
            # f.leftSon = None  --> Questa operazione viene fatta in cutLeft
            return nt
        else:
            nt = self.cutRight(f)
            # f.rightSon = None  --> Questa operazione viene fatta in cutRight
            return nt

    def stampa(self):
        """Permette di stampare l'albero. Per farlo si usa una pila di appoggio."""
        stack = PilaArrayList()
        if self.root != None:
            stack.push([self.root, 0])
        else:
            print("Empty Tree!")
        while not stack.isEmpty():
            current = stack.pop()
            level = current[1]
            if current[0].status == True:
                print("|---" * level + str(current[0].info))
            else:
                print("|---" * level + str(current[0].info) + "x")
                # i nodi "eliminati" sono riconoscibili anche sulla stampa

            if current[0].rightSon != None:
                stack.push([current[0].rightSon, level +1])
            if current[0].leftSon != None:
                stack.push([current[0].leftSon, level +1])


if __name__ == "__main__":
    print("alb1=nodo1=1")
    alb1 = BinaryTree(BinaryNodeLazyDel(1))
    nodo1 = alb1.root

    print("alb2=nodo2=2")
    alb2 = BinaryTree(BinaryNodeLazyDel(2))
    nodo2 = alb2.root

    print("alb3=nodo3=3")
    alb3 = BinaryTree(BinaryNodeLazyDel(3));
    nodo3 = alb3.root

    print("alb4=nodo4=4")
    alb4 = BinaryTree(BinaryNodeLazyDel(4))
    nodo4 = alb4.root

    print("alb5=nodo5=5")
    alb5 = BinaryTree(BinaryNodeLazyDel(5))
    nodo5 = alb5.root

    print("alb6=nodo6=6")
    alb6 = BinaryTree(BinaryNodeLazyDel(6))
    nodo6 = alb6.root

    print("alb1.innestaDestro(nodo1,alb3)")
    alb1.insertAsRightSubTree(nodo1, alb3)
    print("alb1.innestaSinistro(nodo1,alb2)")
    alb1.insertAsLeftSubTree(nodo1, alb2)
    print("alb1.innestaDestro(nodo3,alb4)")
    alb1.insertAsLeftSubTree(nodo3, alb4)
    print("alb1.innestaSinistro(nodo2,alb5)")
    alb1.insertAsLeftSubTree(nodo2, alb5)
    print("alb1.innestaDestro(nodo2,alb6)")
    alb1.insertAsRightSubTree(nodo2, alb6)

    print("Albero 1:")
    alb1.stampa()
    alb1.cut(nodo2)
    print("cut(nodo2):")
    alb1.stampa()

    alb1.root.status = False
    print('status(nodo1) = "delete":')
    alb1.stampa()



       
