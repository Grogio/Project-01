# Project-01
## Prima prova pratica in itinere, corso di Ingegneria degli Algoritmi.

La classe 'DictBinaryTreeLazyDel' implementata in "DictionaryBST_LazyDel.py" è basata sulla classe dizionario 
per alberi binari di ricerca. L'unico attributo che la classe presenta è 'tree', ovvero l'albero binario
formato dalle coppie (key, value) e implementato in "BinaryTree.py". La classe 'BinaryNode' è stata estesa a
'BinaryNodeLazyDel' aggiungendo un attributo 'status' che indica appunto lo stato del nodo: "eliminato" oppure no.

Le operazioni base 'key' e 'value' rimangono le stesse della classe dizionario priva di lazy deletion ed operano in 
tempo costante O(1).

L'operazione 'search' confronta la chiave k da ricercare con la chiave della radice dell'albero e utilizza poi la 
proprietà di ricerca per continuare nel sottoalbero sinistro (se la chiave k è minore) o nel sottoalbero destro
(se la chiave k è maggiore). Se viene trovata la chiave k si passa a un controllo dello 'status' del nodo.
A seconda dell'esito del controllo sullo 'status' la funzione restituisce il nodo (il nodo non è "eliminato") oppure 'None'
(il nodo è "eliminato"). Se non viene trovato nessun nodo con chiave k la funzione restituisce None.
L'operazione 'search' opera in tempo O(h) con h altezza dell'albero, che può diventare O(n) per alberi molto sbilanciati.

L'operazione 'boolDelete' sfrutta l'operazione 'search' che viene effettuata sulla chiave k da eliminare.
Se la ricerca ha esito positivo, quindi esiste un nodo con chiave k, esso viene segnato come "eliminato" e la funzione 
ritorna True, altrimenti, se il nodo non esiste oppure è gia segnato come "eliminato" la funzione ritorna False.
Risulta più semplice della vecchia operazione 'delete', poichè dopo aver segnato l'elemento come "eliminato" non c'è più
bisogno di ripristinare la proprietà di ricerca dell'albero andando a cercare il predecessore. Anche l'operazione 'boolDelete'
opera in tempo O(h) in quanto si basa sulla precedente operazione 'search' applicata sul nodo da eliminare.

L'operazione 'insert', come l'operazione 'search', scandisce l'albero dalla radice sfruttando la proprietà di ricerca
per scegliere se continuare nel sottoalbero sinistro o in quello destro. Una volta raggiunta una foglia con chiave diversa 
da quella da inserire (chiave k), il sottoalbero formato solo dal nuovo nodo viene inserito come figlio sinistro 
(se la chiave è maggiore di k) o come figlio destro (se la chiave è minore di k). Se si incontra un nodo con chiave k, invece,
per definizione di dizionario, il vecchio valore associato al nodo viene sostituito con il nuovo valore v.
Il processo di sostituzione del valore si applica anche se il nodo con chiave k è segnato come "eliminato", e in questo caso
al nodo viene attribuito nuovamente il valore standard di 'status', ovvero "non eliminato"(True).
Anche quest'ultima operazione ha tempo di esecuzione O(h).

Analizzando i dati ottenuti da "DemoDict.py" osserviamo che, come previsto, le operazioni 'search', 'boolDelete' e 'insert'
hanno tempi di esecuzioni molto simili, che dipendono dall'altezza dell'albero. Tuttavia, si nota che, mentre 'search' e
'boolDelete' hanno tempi pressochè identici (dovuti al fatto che, come gia detto, la seconda si serve proprio della prima),
'insert' è la più lenta delle tre, per la maggiore quantità di dati utilizzati: creazione di nodi(chiave, valore) e
inserimento di sottoalberi.

Un'ultima cosa che si nota è che i tempi di esecuzioni delle operazioni non risentono del tipo di impiego:
- elementi esistenti;
- elementi non esistenti;
- elementi "eliminati".

Per ogni caso ciascuna operazione ha lo stesso tempo medio di esecuzione.

Casi pratici in cui sia vantaggioso utilizzare la classe dizionario di alberi di ricerca con lazy deletion potrebbero essere
casi in cui si abbia a che fare con un numero elevato di eliminazioni, dunque si risparmierebbe molto tempo a non ripristinare
ogni volta la proprietà di ricerca dell'albero. Oppure casi in cui sia necessario tenere conto delle varie eliminazioni e
visualizzarle nell'albero, o anche casi in cui le eliminazioni non siano permanenti, magari estendendo ulteriormente la classe
con un'operazione 'recover' che riporta lo 'status' di un elemento "eliminato" al valore standard.

          ###### Giorgio Urbani 0241220
