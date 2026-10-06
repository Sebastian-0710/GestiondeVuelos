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

def procesar_vuelos(vuelos):
    """
    Recorre el diccionario, determina ingresos y detecta baja ocupación (< 50 pasajeros).
    """
    vuelos_procesados = {}

    for codigo, info in vuelos.items():
        pasajeros = info["pasajeros"]
        precio_orig = info["precio_tiquete"]

        precio_fin, ingreso_tot = calcular_ingreso_vuelo(pasajeros, precio_orig)
        baja_ocupacion = pasajeros < 50

        vuelos_procesados[codigo] = {
            "pasajeros": pasajeros,
            "precio_original": precio_orig,
            "precio_final": precio_fin,
            "ingreso_total": ingreso_tot,
            "baja_ocupacion": baja_ocupacion
        }

    return vuelos_procesados

def generar_reporte():
    """
    Ordena los vuelos de mayor a menor ingreso, suma el total global e imprime el reporte.
    """
    vuelos_iniciales = obtener_vuelos()
    vuelos_procesados = procesar_vuelos(vuelos_iniciales)

    vuelos_ordenados = sorted(
        vuelos_procesados.items(),
        key=lambda item: item[1]["ingreso_total"],
        reverse=True
    )

    ingreso_global = sum(datos["ingreso_total"] for _, datos in vuelos_ordenados)

    print("=" * 80)
    print("           REPORTE FINAL DE GESTIÓN DE VUELOS DE LA AEROLÍNEA           ")
    print("=" * 80)
    print(f"{'CÓDIGO':<10} | {'PASAJEROS':<10} | {'P. ORIG ($)':<12} | {'P. FINAL ($)':<12} | {'INGRESO ($)':<12} | {'BAJA OCUP.'}")
    print("-" * 80)

    for codigo, datos in vuelos_ordenados:
        baja_str = "SÍ" if datos["baja_ocupacion"] else "NO"
        print(f"{codigo:<10} | {datos['pasajeros']:<10} | {datos['precio_original']:<12.2f} | {datos['precio_final']:<12.2f} | {datos['ingreso_total']:<12.2f} | {baja_str}")

    print("=" * 80)
    print(f"INGRESO TOTAL GLOBAL DE LA AEROLÍNEA: ${ingreso_global:,.2f}")
    print("=" * 80)

if __name__ == "__main__":
    generar_reporte()
