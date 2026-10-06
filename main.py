# ------------------------------------------------------------------------------
# PARTE 3 - INTEGRANTE 3: Procesamiento y detección de baja ocupación
# ------------------------------------------------------------------------------
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


# ------------------------------------------------------------------------------
# PARTE 4 - INTEGRANTE 4: Ordenamiento y generación del reporte final
# ------------------------------------------------------------------------------
def generar_reporte():
    """
    Ordena los vuelos de mayor a menor ingreso, suma el total global e imprime el reporte.
    """
    vuelos_iniciales = obtener_vuelos()
    vuelos_procesados = procesar_vuelos(vuelos_iniciales)

    # Ordenar por ingreso total (de mayor a menor)
    vuelos_ordenados = sorted(
        vuelos_procesados.items(),
        key=lambda item: item[1]["ingreso_total"],
        reverse=True
    )

    # Cálculo del ingreso global
    ingreso_global = sum(datos["ingreso_total"] for _, datos in vuelos_ordenados)

    # Impresión del reporte final
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