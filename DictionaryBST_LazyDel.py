from BinaryTree import BinaryTree
from BinaryTree import BinaryNodeLazyDel

class DictBinaryTreeLazyDel:
    """Un albero binario di ricerca è un albero che soddisfa le seguenti proprieta':
    1. ogni nodo v contiene un valore (info[1]) a cui e' associata una chiave (info[0])
       presa da un dominio totalmente ordinato;
    2. tutte le chiavi del sottoalbero destro di v sono >= chiave(v);
    3. tutte le chiavi del sottoalbero sinistro di v sono <= chiave(v).
       Inoltre, per la proprieta' di lazy deletion, ogni nodo puo' essere segnato
       come "eliminato" e risulta tale in operazioni di ricerca all'interno dell'albero,
       pur rimanendo accessibile all'utente.
       Quando viene inserito un nuovo nodo con la stessa chiave di un nodo gia'
       presente nell'albero e segnato come "eliminato", quest'ultimo viene fisicamente
       eliminato e sostituito con il nuovo nodo."""
    def __init__(self):
        self.tree = BinaryTree()

    def key(self, node): #Tempo di esecuzione O(1)
        """Restituisce la chiave associata a un nodo"""
        if node == None:
            return None
        return node.info[0]

    def value(self, node): #Tempo di esecuzione O(1)
        """Restituisce il valore associato a un nodo"""
        if node == None:
            return None
        return node.info[1]
        
    def search(self, key): #Tempo di esecuzione O(h)
        """Ricerca il nodo con chiave key all'interno del dizionario.
           Ritorna il nodo, oppure None se non esiste un nodo associato a key
           o se il nodo e' segnato come "eliminato"."""
        if self.tree.root == None:
            return None

        curr = self.tree.root
        while curr != None:
            ck = self.key(curr)
            if key == ck:
                if curr.status == True:
                    return curr
                else:
                    return None

            if key < ck:
                curr = curr.leftSon
            else:
                curr = curr.rightSon

        return None

    def boolDelete(self, key): #Tempo di esecuzione O(h)
        """Verifica se il nodo con chiave key e' segnato come "eliminato".
           Se non lo e', viene segnato come tale e ritorna True.
           Se invece e' gia segnato come "eliminato" oppure il nodo non esiste ritorna False."""
        toRemove = self.search(key)
        if toRemove == None or toRemove.status == False:
            return False
        else:
            toRemove.status = False
            return True

    def insert(self, key, value): #Tempo di esecuzione O(h)
        """Permette di inserire una coppia (key, value) all'interno del dizionario nella
           maniera corretta. Se e' possibile inserire il nodo con chiave key nella posizione
           di un nodo segnato come eliminato, quest'ultimo viene sostituito con quello nuovo."""
        pair = [key, value]
        newNode = BinaryNodeLazyDel(pair)
        newTree = BinaryTree(newNode)

        if self.tree.root == None:
            self.tree.root = newTree.root
        else:
            curr = self.tree.root
            pred = None
            while curr != None:
                pred = curr
                if key == self.key(curr) and curr.status == False:
                    curr.info = pair
                    curr.status = True
                    return
                else:
                    if key <= self.key(curr):
                        curr = curr.leftSon
                    else:
                        curr = curr.rightSon

            if key <= self.key(pred):
                self.tree.insertAsLeftSubTree(pred, newTree)
            else:
                self.tree.insertAsRightSubTree(pred, newTree)

if __name__ == "__main__":
    diz = DictBinaryTreeLazyDel()
    
    print("insert(6,12)")
    diz.insert(6, 12)
    diz.tree.stampa()

    print("insert(4,8)")
    diz.insert(4, 8)
    diz.tree.stampa()

    print("insert(3,6)")
    diz.insert(3, 6)
    diz.tree.stampa()

    print("insert(3,6)")
    diz.insert(3, 6)
    diz.tree.stampa()
    
    print("insert(2,4)")
    diz.insert(2, 4)
    diz.tree.stampa()
    
    print("insert(1,2)")
    diz.insert(1, 2)
    diz.tree.stampa()
    
    print("insert(5,10)")
    diz.insert(5, 10)
    diz.tree.stampa()
    
    print("insert(7,14)")
    diz.insert(7, 14)
    diz.tree.stampa()

    print("search(5)=" + str(diz.search(5)))
    print("search(3)=" + str(diz.search(3)))
    print("search(6)=" + str(diz.search(6)))
    print("search(8)=" + str(diz.search(8)))

    print("boolDelete(6)")
    print(diz.boolDelete(6))
    diz.tree.stampa()
    
    print("boolDelete(3)")
    print(diz.boolDelete(3))
    diz.tree.stampa()

    print("boolDelete(3)")
    print(diz.boolDelete(3))
    diz.tree.stampa()
    
    print("boolDelete(1)")
    print(diz.boolDelete(1))
    diz.tree.stampa()
    
    print("boolDelete(8)")
    print(diz.boolDelete(8))
    diz.tree.stampa()

    print("search(3)=" + str(diz.search(3)))

    print("insert(3,7)")
    diz.insert(3, 7)
    diz.tree.stampa()

    
