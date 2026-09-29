# Ejercicio 1: Pipeline de mapeo y filtrado
def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    return list(map(fn_transformacion, filter(fn_predicado, lista)))


resultado = procesar_coleccion(
    [1, 2, 3, 4, 5, 6],
    lambda numero: numero % 2 == 0,
    lambda numero: numero * 10
)
print(resultado)


# Ejercicio 2: Agrupador personalizado
def agrupar_por(lista, fn_clave):
    grupos = {}
    for elemento in lista:
        clave = fn_clave(elemento)
        grupos.setdefault(clave, []).append(elemento)
    return grupos


productos = [
    {"nombre": "Teclado", "categoria": "perifericos"},
    {"nombre": "Monitor", "categoria": "pantallas"},
    {"nombre": "Mouse", "categoria": "perifericos"},
]
print(agrupar_por(productos, lambda producto: producto["categoria"]))


# Ejercicio 3: Ejecutor repetitivo con historial
def ejecutar_y_rastrear(fn_tarea, n):
    historial = []

    def ejecutar():
        for _ in range(n):
            historial.append(fn_tarea())
        return historial.copy()

    return ejecutar


numero = 0
def siguiente_numero():
    global numero
    numero += 1
    return numero


ejecutar = ejecutar_y_rastrear(siguiente_numero, 3)
print(ejecutar())


# Ejercicio 4: Composicion de funciones
def componer_dos(f, g):
    def composicion(x):
        return f(g(x))

    return composicion


duplicar_y_sumar_uno = componer_dos(lambda valor: valor + 1, lambda valor: valor * 2)
print(duplicar_y_sumar_uno(5))


# Ejercicio 5: Profiling y auditoria
import time


def auditar_ejecucion(fn_objetivo, fn_logger):
    def ejecutar(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = fn_objetivo(*args, **kwargs)
        duracion = time.perf_counter() - inicio
        fn_logger({"resultado": resultado, "duracion": duracion})
        return resultado

    return ejecutar


auditar = auditar_ejecucion(
    lambda numero: numero ** 2,
    lambda informe: print(f"Informe: {informe['resultado']}, tiempo: {informe['duracion']:.6f}s")
)
print(auditar(8))