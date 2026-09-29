# Ejercicio 1: Contador ponderado
def crear_contador_paso(fn_paso):
    cuenta = 0

    def incrementar():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)
        return cuenta

    return incrementar


contador = crear_contador_paso(lambda cuenta_actual: cuenta_actual + 2)
print(contador())
print(contador())


# Ejercicio 2: Acumulador con filtro
def crear_acumulador_validado(criterio_lambda):
    total = 0

    def acumular(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        return total

    return acumular


acumular_mayores = crear_acumulador_validado(lambda valor: valor > 10)
print(acumular_mayores(8))
print(acumular_mayores(15))
print(acumular_mayores(20))


# Ejercicio 3: Promediador con filtro de ruido
def crear_promediador_filtrado(filtro_ruido_lambda):
    valores = []

    def agregar(valor):
        nonlocal valores
        valores = list(filter(filtro_ruido_lambda, valores + [valor]))
        return sum(valores) / len(valores) if valores else 0

    return agregar


promediar = crear_promediador_filtrado(lambda valor: 0 <= valor <= 100)
print(promediar(80))
print(promediar(110))
print(promediar(90))


# Ejercicio 4: Limitador de tasa con reset
def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0

    def ejecutar(tarea):
        nonlocal intentos
        if intentos >= max_intentos:
            fn_alerta(intentos)
            intentos = 0
        intentos += 1
        return tarea()

    return ejecutar


limitar = crear_limitador_avanzado(2, lambda intentos: print(f"Limite superado: {intentos}"))
print(limitar(lambda: "ejecucion 1"))
print(limitar(lambda: "ejecucion 2"))
print(limitar(lambda: "ejecucion 3"))


# Ejercicio 5: Interruptor multiple
def crear_conmutador(lista_estados):
    indice = 0

    def cambiar():
        nonlocal indice
        estado = lista_estados[indice]
        indice = (indice + 1) % len(lista_estados)
        return estado

    return cambiar


conmutar = crear_conmutador(["rojo", "verde", "amarillo"])
print(conmutar())
print(conmutar())
print(conmutar())
print(conmutar())