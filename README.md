# Project-01
Prima prova pratica in itinere, corso di Ingegneria degli Algoritmi.

La classe 'DictBinaryTreeLazyDel' implementata in "DictionaryBST_LazyDel.py" è basata sulla classe dizionario 
per alberi binari di ricerca. L'unico attributo che la classe presenta è 'tree', ovvero l'albero binario
formato dalle coppie (key, value) del nostro dizionario e implementato in "BinaryTree.py". La classe 'BinaryNode' 
è stata estesa a 'BinaryNodeLazyDel' aggiungendo un attributo aggiuntivo 'status' che indica appunto lo stato del nodo: 
"eliminato" oppure no.

Le operazioni base 'key' e 'value' rimangono le stesse della classe dizionario priva di lazy deletion ed operano in 
tempo costante O(1).

All'operazione 'search' viene semplicemente aggiunta un ulteriore riga di controllo dello 'status' del nodo con chiave
corrispondente a quella da ricercare. A seconda dell'esito del controllo sullo 'status' la funzione restituisce il nodo 
(il nodo non è "eliminato") oppure 'None' (il nodo è "eliminato"). L'operazione 'search' opera in tempo O(h) con h altezza
dell'albero, che può diventare O(n) per alberi molto sbilanciati.

L'operazione 'boolDelete' risulta invece più semplice della vecchia operazione 'delete', poichè dopo aver segnato
l'elemento come "eliminato" non c'è più bisogno di ripristinare la proprietà di ricerca dell'albero andando a cercare
il predecessore. Anche l'operazione di 'boolDelete' opera in tempo O(h) in quanto si basa sulla precedente operazione  'search' sul nodo da eliminare.

All'operazione 'insert', come per l'operazione 'search', viene aggiunta una riga di controllo sullo 'status' del nodo con
chiave corrispondente a quella del nuovo nodo da inserire. Se il controllo ha esito positivo (ovvero il nodo è segnato
come "eliminato") quest'ultimo viene sostituito con il nuovo nodo da inserire, mentre per un controllo con esito negativo
(il nodo non è segnato come "eliminato) procede come per la vecchia operazione 'insert'. Anche quest'ultima operazione
ha tempo di esecuzione O(h).

Analizzando i dati ottenuti da "DemoDict.py" osserviamo che, come previsto, le operazioni 'search', 'boolDelete' e 'insert'
hanno tempi di esecuzioni molto simili. Tuttavia, si nota che, mentre 'search' e 'boolDelete' hanno tempi pressochè identici
(dovuti al fatto che, come gia detto, la seconda si serve proprio della prima), 'insert' è la più lenta delle tre, per la 
maggiore quantità di dati utilizzati: creazione di nodi(chiave, valore) e alberi(nodi).

Un'ultima cosa che si nota è che i tempi di esecuzioni delle operazioni non risentono del tipo di impiego:
- search di elementi esistenti, non esistenti o eliminati;
- boolDelete di elementi non eliminati o già eliminati;
- insert di nuovi elementi o elementi a sostituzione di elementi eliminati.

In ogni caso ogni operazione ha lo stesso tempo di esecuzione.

Casi pratici in cui è vantaggioso utilizzare la classe dizionario di alberi di ricerca con lazy deletion potrebbero essere
casi in cui sia necessario tenere conto delle varie eliminazioni e visualizzarle nell'albero, o casi in cui le eliminazioni 
non siano permanenti, magari estendendo ulteriormente la classe con un'operazione 'recover' che riporta lo 'status' di un 
elemento "eliminato" al valore standard.
