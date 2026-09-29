# Ejercicio 1: Generador de formateadores
def crear_formateador(prefijo, fn_transformacion):
    def formatear(texto):
        return prefijo + fn_transformacion(texto)

    return formatear


formatear_mensaje = crear_formateador("INFO: ", lambda texto: texto.upper())
print(formatear_mensaje("procesamiento terminado"))


# Ejercicio 2: Multiplicador parametrico
def crear_operador(factor, operacion_lambda):
    def operar(valor):
        return operacion_lambda(valor, factor)

    return operar


multiplicar_por_tres = crear_operador(3, lambda valor, factor: valor * factor)
print(list(map(multiplicar_por_tres, [2, 4, 6])))


# Ejercicio 3: Descuento con regla dinamica
def crear_descuento_dinamico(regla_condicional_lambda):
    def calcular(precio):
        if regla_condicional_lambda(precio):
            return precio * 0.9
        return precio

    return calcular


aplicar_descuento = crear_descuento_dinamico(lambda precio: precio >= 100)
print(list(map(aplicar_descuento, [80, 100, 250])))


# Ejercicio 4: Generador de nombres unicos
def crear_generador_sufijos(patron_lambda):
    def generar(nombre, numero):
        return patron_lambda(nombre, numero)

    return generar


generar_nombre = crear_generador_sufijos(lambda nombre, numero: f"{nombre}_{numero}.txt")
print(generar_nombre("reporte", 3))


# Ejercicio 5: Conversor de divisas con margen
def crear_conversor(tasa, margen_lambda):
    def convertir(monto):
        conversion = monto * tasa
        return conversion + margen_lambda(conversion)

    return convertir


convertir_a_dolares = crear_conversor(0.058, lambda monto: monto * 0.02)
print(convertir_a_dolares(1000))