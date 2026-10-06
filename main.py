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