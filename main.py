def obtener_vuelos():
    """
    Retorna un diccionario con la información inicial de los vuelos de la aerolínea.
    Cada vuelo incluye el número de pasajeros y el precio original del tiquete.
    """
    vuelos = {
        "AV-101": {"pasajeros": 120, "precio_tiquete": 650.0},
        "AV-102": {"pasajeros": 35,  "precio_tiquete": 450.0},
        "AV-103": {"pasajeros": 85,  "precio_tiquete": 550.0},
        "AV-104": {"pasajeros": 42,  "precio_tiquete": 700.0},
        "AV-105": {"pasajeros": 150, "precio_tiquete": 300.0},
        "AV-106": {"pasajeros": 28,  "precio_tiquete": 520.0}
    }
    return vuelos

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
