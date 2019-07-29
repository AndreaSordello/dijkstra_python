import math
class MyGraph():
    

    def __init__(self):
        self.grafo={}
        print("Creato nuovo grafo")
    def aggiungiNodo(self,nodo):
        if not (nodo in self.grafo):
            self.grafo[nodo]={}
            return True
        else:
            print("Nodo già presente")
            return False
    def collega(self,base,nodo,costo):
        if   base in self.grafo and  nodo in self.grafo :
            self.grafo[base][nodo]=costo
            self.grafo[nodo][base]=costo
            return True
        else:
            print("Nodo inserito non presente nel grafo")
            return False
    def getVicini(self,nodo):
        ret={}
        for element in self.grafo[nodo]:
            ret[element]=self.grafo[nodo][element]
        return ret
    def stampaGrafo(self):
        for nodo in self.grafo:
            print("Nodo", nodo ,"DISTA" ,self.getVicini(nodo))
    

    def dijkstra(self,inizio,fine):
        
        nodiVisitati=list()
        table={}

        for elm in self.grafo:
            table[elm]=list()  #ogni nodo ha una label contenente prev e costo tot
            table[elm]=["PRECEDENTE",math.inf]
        prox=inizio
        table[inizio]=[inizio,0]
        for x in self.grafo:   #Viene solo utilizzato per ciclare per tutti i nodi del grafo
            print("Il prossimo nodo è ",prox)
            nodiVisitati.append(prox)
            vicini=self.getVicini(prox)
            print("i vicini di",prox,"sono ",vicini)
            for elm in vicini:# {'B': 4, 'C': 8}
                if elm not in nodiVisitati:
                    table[elm]=[prox,self.grafo[prox][elm]+table[prox][1]] #B :[ A,9]
            print(table)
            minore=math.inf
            
            for elm in self.grafo:
                if elm not in nodiVisitati and table[elm][1]<minore:
                    minore=table[elm][1]
                    prox=elm
            print("I nodi visitati sono ",nodiVisitati)
        risultato=list()
        
        costoTot=table[fine][1]
        proxNodo=fine
        while proxNodo!=inizio:      #procedo a ritroso partendo dall'ultimo nodo risalgo all' inizio
            risultato.append(proxNodo)
            print(proxNodo)
            proxNodo =table[proxNodo][0]
        risultato.append(inizio)
        risultato=risultato[::-1]
        risultato.append(costoTot)
        print(risultato)
        return risultato
        
        
        
grafo = MyGraph()
grafo.aggiungiNodo("A")
grafo.aggiungiNodo("B")
grafo.aggiungiNodo("C")
grafo.aggiungiNodo("D")
grafo.aggiungiNodo("E")
grafo.aggiungiNodo("F")
grafo.collega("A","B",9)
grafo.collega("A","C",8)
grafo.collega("D","C",4)
grafo.collega("B","D",5)
grafo.collega("E","F",3)
grafo.collega("F","C",8)
grafo.stampaGrafo()
print("PERCORSO MINIMO ",grafo.dijkstra("A","F"))