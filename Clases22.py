def convertir_hora_24_a_12(hora_24):
    # Dividir la hora y los minutos
    hora, minuto = map(int, hora_24.split(':'))
    
    # Determinar si es AM o PM
    if hora >= 12:
        periodo = "PM"
    else:
        periodo = "AM"
    
    # Convertir la hora al formato de 12 horas
    hora_12 = hora % 12
    if hora_12 == 0:
        hora_12 = 12
    
    # Formatear la hora y el minuto para asegurar que tengan dos dígitos si es necesario
    minuto_formateado = f"{minuto:02d}"
    
    # Crear la cadena en notación de 12 horas
    hora_12_formateada = f"{hora_12}:{minuto_formateado} {periodo}"
    
    return hora_12_formateada

# Ejemplo de uso
hora_24 = "13:45"
hora_12 = convertir_hora_24_a_12(hora_24)
print(hora_12)  # Salida: 1:45 PM




