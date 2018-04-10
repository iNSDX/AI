import problema_planificación_pddl as probpl
import búsqueda_espacio_estados as busquee

#EJERCICIO 1

en = probpl.Predicado({'rueda-pinchada','rueda-repuesto'},{'eje','maletero','suelo'})

estado_inicial_rueda = probpl.Estado(en('rueda-pinchada','eje'),en('rueda-repuesto','maletero'))
print(estado_inicial_rueda)

#Sacar la rueda de repuesto del maletero
sacar = probpl.AcciónPlanificación(
    nombre = 'sacar_repuesto',
    precondicionesP = en('rueda-repuesto','maletero'),  #Podrían ser listas de precondiciones y de efectos
    efectosP = en('rueda-repuesto','suelo'),
    efectosN = en('rueda-repuesto','maletero'))

#Quitar la rueda pinchada del eje
quitar = probpl.AcciónPlanificación(
    nombre = 'quitar_pinchada',
    precondicionesP = en('rueda-pinchada','eje'),
    efectosP = en('rueda-pinchada','suelo'),
    efectosN = en('rueda-pinchada','eje'))

#Colocar la rueda de repuesto en el eje
poner = probpl.AcciónPlanificación(
    nombre = 'poner_repuesto',
    precondicionesP = en('rueda-repuesto','suelo'),
    precondicionesN = en('rueda-pinchada','eje'),
    efectosP = en('rueda-repuesto','eje'),
    efectosN = en('rueda-repuesto','suelo'))

#Guardar la rueda pinchada en el maletero
guardar = probpl.AcciónPlanificación(
    nombre = 'guardar_pinchada',
    precondicionesP = en('rueda-pinchada','suelo'),
    precondicionesN = en('rueda-repuesto','maletero'),
    efectosP = en('rueda-pinchada','maletero'),
    efectosN = en('rueda-pinchada','suelo'))

#Problema planificación
problema_rueda_pinchada = probpl.ProblemaPlanificación(
    operadores = [quitar,guardar,sacar,poner],
    estado_inicial = probpl.Estado(en('rueda-pinchada','eje'),en('rueda-repuesto','maletero')),
    objetivosP = [en('rueda-pinchada','maletero'),en('rueda-repuesto','eje')])

#Algoritmo búsqueda profundidad
busqueda_profundidad = busquee.BúsquedaEnProfundidad()
#busqueda_profundidad.buscar(problema_rueda_pinchada)
#print(busqueda_profundidad)

#Algoritmo búsqueda anchura
busqueda_anchura = busquee.BúsquedaEnAnchura()
#busqueda_anchura.buscar(problema_rueda_pinchada)
#print(busqueda_anchura)



#EJERCICIO 2

bloques = {'A', 'B', 'C'}
despejado = probpl.Predicado(bloques)
brazolibre = probpl.Predicado({})
sobrelamesa = probpl.Predicado(bloques)
sobre = probpl.Predicado(bloques, bloques)
agarrado = probpl.Predicado(bloques)

#Estado inicial
estado_inicial_bloques = probpl.Estado(
    sobrelamesa('A'), despejado('A'),
    sobrelamesa('B'), sobre('C', 'B'), despejado('C'),
    brazolibre())

#Establecemos costes dependiendo del bloque que movemos
coste_bloque = probpl.CosteEsquema(lambda b: {'A': 1, 'B': 2, 'C': 3}[b])

# Colocar un bloque sobre otro
apilar = probpl.EsquemaPlanificación('apilar({x},{y})',
    precondicionesP = [despejado('{y}'),agarrado('{x}')],
    efectosN = [despejado('{y}'),agarrado('{x}')],
    efectosP = [despejado('{x}'),brazolibre(),sobre('{x}','{y}')],
    coste = coste_bloque('{x}'),
    dominio = {('A','B'),('A','C'),('B','A'),('B','C'),('C','A'),('C','B')},
    variables = {'x':bloques,'y':bloques})

# Quitar un bloque que estaba sobre otro
desapilar = probpl.EsquemaPlanificación('desapilar({x},{y})',
    precondicionesP = [sobre('{x}','{y}'),despejado('{x}'),brazolibre()],
    efectosN = [sobre('{x}','{y}'),despejado('{x}'),brazolibre()],
    efectosP = [agarrado('{x}'),despejado('{y}')],
    coste = coste_bloque('{x}'),
    dominio = {('A','B'),('A','C'),('B','A'),('B','C'),('C','A'),('C','B')})

# Agarrar un bloque de la mesa con el robot
agarrar = probpl.EsquemaPlanificación('agarrar({x})',
    precondicionesP = [despejado('{x}'),sobrelamesa('{x}'),brazolibre()],
    efectosN = [despejado('{x}'),sobrelamesa('{x}'),brazolibre()],
    efectosP = [agarrado('{x}')],
    coste = coste_bloque('{x}'),
    dominio = bloques)

# Bajar un bloque hasta la mesa
bajar = probpl.EsquemaPlanificación('bajar({x})',
    precondicionesP = [agarrado('{x}')],
    efectosN = [agarrado('{x}')],
    efectosP = [despejado('{x}'),sobrelamesa('{x}'),brazolibre()],
    coste = coste_bloque('{x}'),
    variables = {'x':bloques})

#print(agarrar)   Acciones que se generan a partir del esquema
#print(apilar)

#Problema planificación
problema_mundo_bloques = probpl.ProblemaPlanificación(
    operadores=[apilar, desapilar, agarrar, bajar],
    estado_inicial=estado_inicial_bloques,
    objetivosP=[sobrelamesa('C'), sobre('B', 'C'), sobre('A', 'B')])

#busqueda_profundidad.buscar(problema_mundo_bloques)
#print(busqueda_profundidad)



#EJERCICIO 3

cuevas = {'C{}'.format(i) for i in range(5)}
buceadores = {'B{}'.format(i) for i in range(2)}
cantidades = {str(i) for i in range(9)}


print("Cuevas: {}".format(cuevas))
print("Buceadores: {}".format(buceadores))
print("Cantidades: {}".format(cantidades))

conexiones = [('C0', 'C1'),
              ('C1', 'C0'),
              ('C1', 'C2'),
              ('C1', 'C4'),
              ('C2', 'C1'),
              ('C2', 'C3'),
              ('C3', 'C2'),
              ('C4', 'C1')]

#Predicados - Variables de estado
posicion_buceador = probpl.Predicado(buceadores,cuevas|{'superficie'})
disponible = probpl.Predicado(buceadores)
trabajando = probpl.Predicado(buceadores)
descompresion = probpl.Predicado(buceadores)
tanques_llenos = probpl.Predicado(buceadores|cuevas,cantidades)
con_foto_de = probpl.Predicado(cuevas)

#Estado inicial
estado_inicial_buceadores = probpl.Estado(
    posicion_buceador('B0','superficie'),posicion_buceador('B1','superficie'),disponible('B0'),disponible('B1'))

#Coste de contratar un buceador
coste_buceador = probpl.CosteEsquema(lambda b: {'B0': 10, 'B1': 67}[b])

#Acciones
contratar_B0 = probpl.AcciónPlanificación('contratar(B0)',
    precondicionesP = disponible('B0'),
    precondicionesN = trabajando('B1'),
    efectosP = trabajando('B0'),
    efectosN=[disponible('B0'), disponible('B1')],
    coste = coste_buceador('B0'))

contratar_B1 = probpl.AcciónPlanificación('contratar(B1)',
    precondicionesP = disponible('B1'),
    precondicionesN = trabajando('B0'),
    efectosP = trabajando('B1'),
    coste = coste_buceador('B1'))
#Operadores (EsquemaPlanificación)
entrar_al_agua = probpl.EsquemaPlanificación('entrar_al_agua({b})',
    precondicionesP = [trabajando('{b}'),posicion_buceador('{b}','superficie')],
    efectosP = [posicion_buceador('{b}','C0'),tanques_llenos('{b}','4')],
    efectosN = posicion_buceador('{b}','superficie'),
    variables = {'b':buceadores})

bucear = probpl.EsquemaPlanificación('bucear({b},{c1},{c2},{t1},{t2})',
    precondicionesP = [posicion_buceador('{b}','{c1}'),tanques_llenos('{b}','{t1}')],
    efectosP = [posicion_buceador('{b}','{c2}'),tanques_llenos('{b}','{t2}')],
    efectosN = [posicion_buceador('{b}', '{c1}'), tanques_llenos('{b}','{t1}')],
    dominio = [(b,c1,c2,str(t1),str(t1-1))
        for b in buceadores
        for (c1,c2) in conexiones
        for t1 in range(1,5)])

fotografiar = probpl.EsquemaPlanificación('fotografiar({b},{c},{t1},{t2})',
    precondicionesP = posicion_buceador('{b}','{c}'),
    efectosP = [con_foto_de('{c}'),tanques_llenos('{b}','{t2}')],
    efectosN = tanques_llenos('{b}','{t1}'),
    dominio = [(b,c,str(t1),str(t1-1))
        for b in buceadores
        for c in cuevas
        for t1 in range(1,5)])

soltar_tanque = probpl.EsquemaPlanificación('soltar_tanque({b},{c},{t1},{t2})',
    precondicionesP = posicion_buceador('{b}','{c}'),
    precondicionesN = tanques_llenos('{b}','0'),
    efectosP = [tanques_llenos('{b}','{t2}'),tanques_llenos('{c}','1')],
    efectosN = [tanques_llenos('{b}','{t1}'),tanques_llenos('{c}','0')],
    dominio = [(b,c,str(t1),str(t1-1))
        for b in buceadores
        for c in cuevas
        for t1 in range(1,5)])

cargar_tanque = probpl.EsquemaPlanificación('cargar_tanque({b},{c},{t1},{t2})',
    precondicionesP = [posicion_buceador('{b}','{c}'),tanques_llenos('{c}','1')],
    precondicionesN = tanques_llenos('{b}','4'),
    efectosP = [tanques_llenos('{b}','{t2}'),tanques_llenos('{c}','0')],
    efectosN = [tanques_llenos('{b}','{t1}'),tanques_llenos('{c}','1')],
    dominio = [(b,c,str(t1),str(t1+1))
        for b in buceadores
        for c in cuevas
        for t1 in range(1,4)])

salir_del_agua = probpl.EsquemaPlanificación('salir_del_agua({b})',
    precondicionesP = posicion_buceador('{b}','C0'),
    efectosP = [posicion_buceador('{b}','superficie'),descompresion('{b}')],
    efectosN = trabajando('{b}'),
    variables = {'b':buceadores})

problema_buceadores = probpl.ProblemaPlanificación(
    operadores = [contratar_B0,contratar_B1,entrar_al_agua,bucear,fotografiar,soltar_tanque,cargar_tanque,salir_del_agua],
    estado_inicial = estado_inicial_buceadores,
    objetivosP=[con_foto_de('C4'),posicion_buceador('B0','superficie'),posicion_buceador('B1','superficie')]
)

busqueda_profundidad.buscar(problema_buceadores)
print(busqueda_profundidad)