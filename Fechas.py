def convertir_fecha(fecha_texto):
    # Diccionario para mapear nombres de meses a números
    meses = {
        "Enero": 1, "Febrero": 2, "Marzo": 3,
        "Abril": 4, "Mayo": 5, "Junio": 6,
        "Julio": 7, "Agosto": 8, "Septiembre": 9,
        "Octubre": 10, "Noviembre": 11, "Diciembre": 12
    }
    
    # Separar la fecha en día, mes y año
    dia, mes_texto, año = fecha_texto.replace(',', '').split()        
    
    # Convertir el mes de texto a número    
    mes_numero = meses[mes_texto]
    
    # Devolver la fecha en formato numérico
    return f"{dia} {mes_numero} {año}"

# Ejemplo de uso
fecha_texto = "15, Febrero 1989"
fecha_numerica = convertir_fecha(fecha_texto)
print(fecha_numerica)  # Salida: 15 2 1989
