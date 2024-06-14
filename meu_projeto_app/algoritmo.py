import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}
        
    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
        
    def adicionar_aresta(self, origem, destino, peso):
        if origem not in self.vertices:
            self.adicionar_vertice(origem)
        if destino not in self.vertices:
            self.adicionar_vertice(destino)
        self.vertices[origem][destino] = peso
        self.vertices[destino][origem] = peso  # Se o grafo for não-direcionado

def dijkstra(grafo, inicio):
    distancias = {vertice: float('infinity') for vertice in grafo.vertices}
    distancias[inicio] = 0
    caminho = {vertice: None for vertice in grafo.vertices}
    prioridade = [(0, inicio)]
    
    while prioridade:
        distancia_atual, vertice_atual = heapq.heappop(prioridade)
        
        if distancia_atual > distancias[vertice_atual]:
            continue
        
        for vizinho, peso in grafo.vertices[vertice_atual].items():
            distancia = distancia_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho[vizinho] = vertice_atual
                heapq.heappush(prioridade, (distancia, vizinho))
                
    return distancias, caminho

def caminho_mais_curto(caminho, inicio, fim):
    percurso = []
    passo = fim
    
    while passo is not None:
        percurso.append(passo)
        passo = caminho[passo]
        
    percurso.reverse()
    return percurso