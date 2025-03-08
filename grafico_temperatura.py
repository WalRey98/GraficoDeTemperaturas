import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mplcursors

#Ruta del archivo CSV
ruta = r"C:\Users\walte\Documents\Curso Python DataScience y ML\Día 9\Cuadernos para Prácticas\Datos+Meteorológicos_Arg_2023.csv"
df = pd.read_csv(ruta)

#cargar datos de un DataFrame
df = pd.read_csv(ruta)
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')

#Obtener lista de ciudades unicas
lista_ciudades = df['Ciudad'].unique().tolist()

#Diccionario de meses
dict_meses = {
    1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo',
    6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre',
    10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
}

def consultar_temperaturas():
    while True:
        #Solicitar la ciudad
        print('\nCiudades disponibles: ', lista_ciudades)
        ciudad_elegida = input('Ingrese la ciudad: ').title()

        #Solicitar el mes
        try:
            mes_elegido = int(input('Ingrese el mes (1-12): '))
        except ValueError:
            print('Debe ingresar un número válido')
            continue

        #Validar los imputs
        if ciudad_elegida not in lista_ciudades or mes_elegido not in dict_meses:
            print('Ciudad o mes no validos. Intentalo nuevamente')
            continue

        #Filtrar datos
        datos_ciudad_mes = df[(df['Ciudad'] == ciudad_elegida) & (df['Fecha'].dt.month == mes_elegido)]

        #Verificar si hay datos disponibles
        if datos_ciudad_mes.empty:
            print("No hay datos disponibles para la ciudad y mes seleccionados")
            continue

        #Graficar temperaturas
        plt.figure(figsize=(12, 6))
        max_plot, = plt.plot(datos_ciudad_mes['Fecha'], datos_ciudad_mes['Temperatura Maxima'], label='Máxima', color='red', linestyle='dashed', marker='o')
        min_plot, = plt.plot(datos_ciudad_mes['Fecha'], datos_ciudad_mes['Temperatura Minima'], label='Mínima', color='blue', linestyle='dashed', marker='o')
        plt.plot(datos_ciudad_mes['Fecha'], datos_ciudad_mes['Temperatura Maxima'], label='Maxima', color='red', linestyle='dashed', marker='o')
        plt.plot(datos_ciudad_mes['Fecha'], datos_ciudad_mes['Temperatura Minima'], label='Minima', color='blue', linestyle='dashed', marker='o')
        plt.fill_between(datos_ciudad_mes['Fecha'], datos_ciudad_mes['Temperatura Minima'], datos_ciudad_mes['Temperatura Maxima'], color='gray', alpha=0.2)
        plt.title(f'Temperaturas en {ciudad_elegida} durante {dict_meses[mes_elegido]}', fontsize=14, fontweight='bold')
        plt.xlabel('Fecha', fontsize=12)
        plt.ylabel('Temperatura (°C)', fontsize=12)
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.6)

        #Se agrega la interactividad para mostrar los valores con el cursor
        cursor = mplcursors.cursor([max_plot, min_plot], hover=True)
        cursor.connect('add', lambda sel: sel.annotation.set_text(f'{sel.target[1]:.1f} °C'))
        plt.show()

        #Preguntar si desea continuar
        otra_consulta = input('¿Desea consultar otra ciudad y mes? (s/n): ')
        if otra_consulta.lower() != 's':
            break

consultar_temperaturas()