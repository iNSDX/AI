import problema_espacio_estados as probee
import búsqueda_espacio_estados as busqee
import copy

#Exercise 2
class Map:
    def __init__(self, celdas):
        self.celdas = celdas

    def tamaño_hor(self):
        return len(self.celdas[0])

    def tamaño_ver(self):
        return len(self.celdas)

    def tipo_celda(self, f, c):
        return self.celdas[f][c]

e_ini = (5,0)
e_fin = (0,9)

def cost(state):
    (i, j) = state
    return map.tipo_celda(i, j)

map = Map([[1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
           [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
           [1, 1, 1, 2, 2, 4, 2, 2, 1, 1],
           [1, 1, 1, 2, 4, 4, 4, 2, 1, 1],
           [1, 1, 1, 2, 2, 4, 0, 0, 0, 0],
           [1, 1, 1, 1, 2, 2, 0, 0, 0, 0]])

def applicabilityU(state):
    (i, j) = state
    return (i>0) and map.tipo_celda(i-1,j)!=0

def applyU(state):
    (i, j) = state
    return (i-1,j)

moveUp=probee.Acción("Up",applicabilityU,applyU,cost)

def applicabilityD(state):
    (i, j) = state
    return (i < map.tamaño_ver()-1) and map.tipo_celda(i+1, j) !=0

def applyD(state):
    (i, j) = state
    return (i+1, j)

moveDown = probee.Acción("Down", applicabilityD, applyD, cost)

def applicabilityL(state):
    (i, j) = state
    return (j > 0) and map.tipo_celda(i, j-1) != 0

def applyL(state):
    (i, j) = state
    return (i, j-1)


moveLeft = probee.Acción("Left", applicabilityL, applyL, cost)

def applicabilityR(state):
    (i, j) = state
    return (j < map.tamaño_hor()-1) and map.tipo_celda(i, j+1) != 0

def applyR(state):
    (i, j) = state
    return (i, j+1)

moveRight = probee.Acción("Right", applicabilityR, applyR, cost)

actions=[moveUp,moveDown,moveLeft,moveRight]

MapPathProblem = probee.ProblemaEspacioEstados(actions,e_ini,[e_fin])

import math

def h(node): #Basic heuristic
    res=None
    (i,j)=node.estado

    for final_state in [e_fin]:
        aux=math.sqrt((i-final_state[0])**2 + (j-final_state[1])**2)

        if res == None:
            res = aux
        elif aux < res:
            res = aux

    return res


aStar_search=busqee.BúsquedaAEstrella(h,detallado=True).buscar(MapPathProblem)
print(aStar_search)

#If we want it to pass by waypoints
def search_path_with_waypoints(waypoints):
    if waypoints and len(waypoints) > 1:
        initial_state = waypoints[0]

        for i in range(len(waypoints)-1):
            print(initial_state)

            final_state = waypoints[i+1]
            MapPathProblemWaypoints=probee.ProblemaEspacioEstados(actions,initial_state,[final_state])

            solution=busqee.BúsquedaÓptima().buscar(MapPathProblemWaypoints)
            if solution:
                print(solution)
                initial_state=waypoints[i+1]
            else:
                print("No solution found")

search_path_with_waypoints([(5, 0), (1, 6), (5, 5), (0, 9)])




