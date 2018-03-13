import problema_espacio_estados as probee
import búsqueda_espacio_estados as busqee
import copy


class MoverDisco(probee.Acción):
    def __init__(self, i, j):
        nombre = 'De {} a {}'.format(i, j)
        super().__init__(nombre)
        self.varilla_de = i
        self.varilla_a = j

    def está_vacía(self, estado, varilla):
        return not bool(estado[varilla - 1])

    def disco_superior(self, estado, varilla):
        return min(estado[varilla - 1])

    def es_aplicable(self, estado):
        return (not self.está_vacía(estado, self.varilla_de) and
                (self.está_vacía(estado, self.varilla_a) or
                 self.disco_superior(estado, self.varilla_de) <
                 self.disco_superior(estado, self.varilla_a)))

    def quitar_disco(self, estado, varilla):
        disco = self.disco_superior(estado, varilla)
        estado[varilla - 1].remove(disco)
        return disco

    def poner_disco(self, estado, varilla, disco):
        estado[varilla - 1].add(disco)

    def aplicar(self, estado):
        nuevo_estado = copy.deepcopy(estado)
        disco = self.quitar_disco(nuevo_estado, self.varilla_de)
        self.poner_disco(nuevo_estado, self.varilla_a, disco)
        return nuevo_estado


acciones = [MoverDisco(i, j) for i in range(1, 4) for j in range(1, 4) if i != j]
estado_inicial = [{1, 2}, set(), set()]
estado_final = [set(), set(), {1, 2}]
Torres_Hanoi_2 = probee.ProblemaEspacioEstados(acciones, estado_inicial, [estado_final])
pathAnchura=busqee.BúsquedaEnAnchura(detallado=True).buscar(Torres_Hanoi_2)
print(pathAnchura)


class TorresHanoi(probee.ProblemaEspacioEstados):
    def __init__(self, n):
        acciones = [MoverDisco(i, j) for i in range(1, 4)
                    for j in range(1, 4) if i != j]
        estado_inicial = [set(range(1, n + 1)), set(), set()]
        super().__init__(acciones, estado_inicial)
        self.n = n

    def es_estado_final(self, estado):
        return estado[2] == set(range(1, self.n + 1))

def h(nodo):
    estado = nodo.estado
    return len(estado[0]) + len(estado[1])

Torres_Hanoi_8=TorresHanoi(8)
pathAStar = busqee.BúsquedaAEstrella(h).buscar(Torres_Hanoi_8)
print(pathAStar)


