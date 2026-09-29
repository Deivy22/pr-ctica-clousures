
# Ejercicio 1: Validador compuesto
def crear_validador_multiple(*lambdas_criterios):
    def validar(objeto):
        return all(criterio(objeto) for criterio in lambdas_criterios)

    return validar


validar_usuario = crear_validador_multiple(
    lambda usuario: usuario["edad"] >= 18,
    lambda usuario: usuario["activo"]
)
print(validar_usuario({"edad": 21, "activo": True}))


# Ejercicio 2: Cache con tamano maximo
def memoizar_avanzado(fn_costosa, max_items):
    cache = {}

    def ejecutar(valor):
        if valor in cache:
            return cache[valor]
        resultado = fn_costosa(valor)
        if len(cache) >= max_items:
            primer_elemento = next(iter(cache))
            del cache[primer_elemento]
        cache[valor] = resultado
        return resultado

    return ejecutar


calcular = memoizar_avanzado(lambda numero: numero ** 2, 2)
print(calcular(4))
print(calcular(5))
print(calcular(4))


# Ejercicio 3: Pipeline secuencial
def crear_pipeline(*funciones_transformacion):
    def ejecutar(valor_inicial):
        valor = valor_inicial
        for funcion in funciones_transformacion:
            valor = funcion(valor)
        return valor

    return ejecutar


pipeline = crear_pipeline(
    lambda texto: texto.strip(),
    lambda texto: texto.upper(),
    lambda texto: f"[{texto}]"
)
print(pipeline("  funcional  "))


# Ejercicio 4: Sistema Pub/Sub
def crear_sistema_eventos():
    suscriptores = {}

    def gestionar(accion, evento=None, fn_suscriptor=None, dato=None):
        if accion == "registrar":
            suscriptores.setdefault(evento, []).append(fn_suscriptor)
        elif accion == "emitir":
            return [fn(dato) for fn in suscriptores.get(evento, [])]
        return None

    return gestionar


eventos = crear_sistema_eventos()
eventos("registrar", "mensaje", lambda texto: f"Recibido: {texto}")
print(eventos("emitir", "mensaje", dato="Hola"))


# Ejercicio 5: Mini-query engine
def crear_consultor(campo):
    def crear_filtro(operador_lambda, valor_esperado):
        def consultar(lista):
            return list(filter(
                lambda objeto: operador_lambda(objeto.get(campo), valor_esperado),
                lista
            ))

        return consultar

    return crear_filtro


productos = [
    {"nombre": "Teclado", "precio": 450},
    {"nombre": "Monitor", "precio": 3200},
    {"nombre": "Mouse", "precio": 200},
]
consultar_por_precio = crear_consultor("precio")
productos_baratos = consultar_por_precio(lambda precio, limite: precio < limite, 500)
print(productos_baratos(productos))