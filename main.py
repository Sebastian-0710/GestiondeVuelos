# ------------------------------------------------------------------------------
# PARTE 2 - INTEGRANTE 2: Cálculo de ingresos y descuentos
# ------------------------------------------------------------------------------
def calcular_precio_final(precio_original):
    """
    Aplica un descuento del 15% si el precio del tiquete supera las 500 unidades.
    """
    if precio_original > 500:
        return precio_original * 0.85
    return precio_original

def calcular_ingreso_vuelo(pasajeros, precio_original):
    """
    Calcula el precio final del tiquete y el ingreso total por vuelo.
    """
    precio_final = calcular_precio_final(precio_original)
    ingreso_total = pasajeros * precio_final
    return precio_final, ingreso_total