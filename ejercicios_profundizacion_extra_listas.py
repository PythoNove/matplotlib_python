#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import matplotlib.pyplot as plt 
import matplotlib.axes
import mplcursors
import numpy as np

'''
NOTA PARA TODOS LOS EJERCICIOS

Para la resolución de todos los problemas utilizará
el dataset "ventas.csv".

Desde ahora los de datos los generará c/u
con Numpy o comprensión de listas o ambos, queda
a su elección en cada caso. Si quiere usar Numpy
para todo, puede abrir el archivo directamente con Numpy
y trabajar sin pasar por listas o diccionarios.

TIP: Para abrir el archivo CSV con Numpy y que el header no
     quede mezclado con los datos utilizar:
     data = np.genfromtxt(file_name_csv, delimiter=',', names=True) 

NO están permitidos los bucles en la realización de estos ejercicios.

Descripción del dataset "ventas.csv"
- Este dataset contiene el importe facturado por un local
  en la venta de sus productos dividido en 4 categorías
- Se contabiliza lo vendido por categória al cerrar el día,
  el dataset está ordenado por mes y día
- El dataset contiene 3 meses (genéricos) de 30 días c/u

'''


def ej1(ventas):
    print('Comenzamos a divertirnos!')

    '''
    Para comenzar a calentar en el uso del dataset se lo solicita
    que grafique la evolución de la facturación de la categoría alimentos
    para el primer mes (mes 1) de facturación.
    Realice un line plot con los datos de facturación de alimentos del mes 1
    Deberá poder observar la evolución de ventas(y) vs días(x)

    TIP:
    1) Para aquellos que utilicen listas siempre primero deberan
    emprezar filtrando el dataset en una lista de diccionarios que
    posee solo las filas y columnas que a están buscando.
    En este caso todas las filas cuyo mes = 1 y solo la columan
    de día(x) y de alimentos(y).
    Una vez que tiene esa lista de dccionarios reducida a la información
    de interés, debe volver a utilizar comprensión de listas para separar
    los datos de los días(x) y de los alimentos(y)

    2) Para aquellos que utilicen Numpy, si transformaron su CSV en Numpy
    les debería haber quedado una matriz de 6 columnas y de 90 filas
    (recordar sacar la primera fila que es el header)
    mes | dia | alimentos | bazar | limpieza | electrodomesticos
    Luego si quisieramos acceder a solo la columna de los dias (col=1)
    podemos utilizar slicing de Numpy:
    dias = dataset[:, 1]
    ¿Cómo puedo obtener las filas solo del primer mes?
    Aplicando mask de Numpy:
    mes_1 --> col = 0
    filas_mes_1 = dataset[:, 0] == 1
    Obtengo solos los datos del mes uno
    mes_1 = dataset[filas_mes_1, :]

    x --> dias
    Obtengo solo los dias del mes1 de alimentos
    x = dataset[filas_mes_1, 1]
    o tambien puede usar
    x = mes_1[:, 1]

    y --> alimentos
    Obtengo solo los alimentos del mes1 de alimentos
    y = dataset[filas_mes_1, 2]
    o tambien puede usar
    y = mes_1[:, 2]

    '''

    # Extraer datos de archivo ventas.csv
    ventas = [{'Dia': int(ventas[x].get('Dia')), 'Alimentos': int(ventas[x].get('Alimentos'))} 
        for x in range(len(ventas)) if ventas[x].get('Mes') == '1']
    
    # formar listas para graficar
    dia = [x['Dia'] for x in ventas]
    venta_alimentos = [x['Alimentos'] for x in ventas]

    # gráfico line plot
    fig = plt.figure('ventas.csv')
    ax = fig.add_subplot()

    ax.plot(dia, venta_alimentos, color='r', marker='.', label='Cantidad vendida')
    ax.set_facecolor('whitesmoke')
    ax.set_title('Mes Enero: VENTA DE ALIMENTOS')
    ax.set_ylabel('Cantidad')
    ax.set_xlabel('Dia')
    ax.legend()
    ax.grid(ls='solid')
    mplcursors.cursor(multiple=True)

    plt.show()


def ej2(ventas):
    print('Comenzamos a ponernos serios!')

    '''
    Queremos visualizar como ver la tendencia de venta de los alimentos
    a lo largo de todo el año.
    Para eso queremos utilizar el método "np.diff" para obtener la diferencia
    día a día de lo vendido.

    Se debe poder primero discriminar las ventas por la categoría Alimentos,
    1) en el caso de usar listas se debe generar una lista de solo
       ventas de aliementos de todo el año.
    2) En el caso de usar numpy no hace falta generar una lista/array aparte,
       pero si le resulta comodo puede hacerlo.

    Luego que tienen discriminadas las ventas por alimento aplicar el método
    np.diff
    tendencia = np.diff(mis ventas de alimentos)

    Graficar el valor obtenido con un Line Plot

    NOTA: Importante!, en este caso no disponen facilmente del eje "X" de diff,
    para simplificar el caso solamente graficar la variable "tendencia"
    plot(tendencia)

    '''
  
    # obtener datos
    ventas_de_alimentos = [int(ventas[x].get('Alimentos')) for x in range(len(ventas))]

    # convertir lista ventas en array ventas
    ventas_de_alimentos = np.array(ventas_de_alimentos)

    # aplicar diff
    tendencia = np.diff(ventas_de_alimentos)
    
    # grafico de tendencia
    fig = plt.figure('ventas.csv')
    ax = fig.add_subplot()

    ax.plot(tendencia, color='g', marker='^', label='Diferencia dia a dia')
    ax.set_facecolor('lightgray')
    ax.set_title('TENDENCIA', fontsize=20)
    ax.set_ylabel('Diferencia (función np.diff)')
    ax.legend()
    ax.grid(ls='dashed')
    mplcursors.cursor(multiple=True)

    plt.show()


def ej3(ventas):
    print("Buscando la tendencia")

    '''
    Si observa el dataset, los electrodomésticos no siempre
    tienen facturación al finalizar el día.
    Deseamos que generen una nueva lista/array/columna
    en la cual coloquen un "1" si ese día se vendió electrodomésticos
    o un "0" sino se vendio nada (facturación = 0).
    Luego graficar utilizando Line Plot esta nueva lista/array/columna
    para visualizar la tendencia de cuantos días consecutivos hay
    ventas de electrodomésticos.
    
    '''
    # Extraer datos
    dias_venta = [1 if ventas[x].get('Electrodomesticos') == '0' else 0 
                    for x in range(len(ventas))]

    # gráfico
    fig = plt.figure('ventas.csv')
    ax = fig.add_subplot()

    ax.plot(dias_venta, color='r', marker='^', label='')
    ax.set_facecolor('lightgray')
    ax.set_title('TENDENCIA', fontsize=20)
    ax.set_xlabel('Dias')
    ax.set_ylabel('Vendido / No vendido')
    # ax.legend()
    ax.grid(ls='dashed')
    mplcursors.cursor(multiple=True)

    plt.show()

def ej4(ventas):
    print("Exprimiendo los datos")

    '''
    Obtener la facturación total (la suma total en los 3 meses)
    de cada categória por separado. Nos debe quedar el total
    facturado en alimentos, en bazar, en limpieza y en
    electrodomesticos por separado (son 4 valores)

    TIP:
    1) para los que usan listas, para poder obtener estos
    valores primero deberan generar una lista de cada categoría,
    para luego poder aplicar operaciones como sum.
    2) Para los que usan numpy pueden usar directamente np.sum
    y especificando el axis=0 estarán haciendo la suma total de la columna

    Con la información obtenida realizar un Pie Plot
    para visualizar que categoría facturó más en lo que va
    del año
    '''

    # formar lista, array y suma de alimentos
    alimentos = [int(ventas[x].get('Alimentos')) for x in range(len(ventas))]
    suma_alimentos = sum(np.array(alimentos))
        
    # formar lista, array y suma de bazar
    bazar = [int(ventas[x].get('Bazar')) for x in range(len(ventas))]
    suma_bazar = sum(np.array(bazar))

    # formar lista, array y suma de limpieza
    limpieza = [int(ventas[x].get('Limpieza')) for x in range(len(ventas))]
    suma_limpieza = sum(np.array(limpieza))
    

    # formar lista, array y suma de electrodomesticos
    electro = [int(ventas[x].get('Electrodomesticos')) for x in range(len(ventas))]
    suma_electro = sum(np.array(electro))

    # lista de sumas y sumatoria total
    lista_total = [suma_alimentos, suma_bazar,  suma_limpieza, suma_electro]
    sumatoria_total = suma_alimentos + suma_bazar +  suma_limpieza + suma_electro

    
    # grafico
    productos = ['Alimentos', 'Bazar', 'Limpieza','Electrodomesticos']
    porcentajes = [suma/sumatoria_total*100 for suma in lista_total]
        
    fig = plt.figure('ventas.csv')
    fig.suptitle('Facturación en porcentaje', fontsize=18)
    ax = fig.add_subplot()

    explode = (0, 0, 0, 0.1)
    ax.pie(porcentajes, labels=productos, autopct='%1.1f%%', startangle=90, shadow=True, 
            explode=explode)
    ax.axis('equal')

    plt.show()


def ej5(ventas):
    print("Ahora sí! buena suerte :)")

    '''
    Ahora que ya hemos jugado un poco con nuestro dataset,
    queremos realizar 3 gráficos de columnas en una misma figura
    Cada gráfico de columnas deben tener 4 columnas que representan
    el total vendido de cada categoría al final del mes.
    Para poder hacer este ejercicio deben obtener primero
    total facturado por categoria por mes (deben filtrar por mes)
    Es parecido a lo realizado en el ejercicio anterior pero en vez
    de todo el año es la suma total por mes por categoría.

    Siendo que son 4 categorías y 3 meses, deben obtener al final
    12 valores, con esos 12 valores construir 3 listas/arrays
    para poder mostrar los 3 gráficos de columnas

    BONUS Track: Si están cancheros y aún quedan energías para practicar,
    les proponemos que en vez de realizar 3 gráficos de columnas separados
    realicen uno solo y agrupen la información utilizando gráfico de barras
    apilados o agrupados (a su elección)
    '''
    # sumatoria de arrays con las cantidades vendidas por producto y por mes
    alimentos_1 = sum(np.array([int(ventas[x].get('Alimentos')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '1']))
    alimentos_2 = sum(np.array([int(ventas[x].get('Alimentos')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '2']))
    alimentos_3 = sum(np.array([int(ventas[x].get('Alimentos')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '3']))
    
    bazar_1 = sum(np.array([int(ventas[x].get('Bazar')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '1']))
    bazar_2 = sum(np.array([int(ventas[x].get('Bazar')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '2']))
    bazar_3 = sum(np.array([int(ventas[x].get('Bazar')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '3']))

    limpieza_1 = sum(np.array([int(ventas[x].get('Limpieza')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '1']))
    limpieza_2 = sum(np.array([int(ventas[x].get('Limpieza')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '2']))
    limpieza_3 = sum(np.array([int(ventas[x].get('Limpieza')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '3']))

    electro_1 = sum(np.array([int(ventas[x].get('Electrodomesticos')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '1']))
    electro_2 = sum(np.array([int(ventas[x].get('Electrodomesticos')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '2']))
    electro_3 = sum(np.array([int(ventas[x].get('Electrodomesticos')) 
                for x in range(len(ventas)) if ventas[x].get('Mes') == '3']))

    productos = ['Alimentos', 'Bazar', 'Limpieza', 'Electrodomestricos']
    
    # ventas por mes
    mes_1 = [alimentos_1, bazar_1, limpieza_1, electro_1]
    mes_2 = [alimentos_2, bazar_2, limpieza_2, electro_2]
    mes_3 = [alimentos_3, bazar_3, limpieza_3, electro_3]
    
    # grafico de barras
    fig = plt.figure('ventas.csv')
        
    ax1 = fig.add_subplot(1, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)
    
    ax1.bar(productos, mes_1, label='Mes_1')
    ax1.set_facecolor('whitesmoke')
    ax1.legend()
    ax1.set_title('Mes 1', fontsize=16)
    ax1.set_xlabel('Productos', fontsize=10)
    ax1.set_ylabel('Cantidad vendidos', fontsize=10)
        
    ax2.bar(productos, mes_2, label='Mes_2')
    ax2.set_facecolor('whitesmoke')
    ax2.legend()
    ax2.set_title('Mes 2', fontsize=16)
    ax2.set_xlabel('Productos', fontsize=10)
    ax2.set_ylabel('Cantidad vendidos', fontsize=10)
    
    ax3.bar(productos, mes_3, label='Mes_3')
    ax3.set_facecolor('whitesmoke')
    ax3.legend()
    ax3.set_title('Mes 3', fontsize=16)
    ax3.set_xlabel('Productos', fontsize=10)
    ax3.set_ylabel('Cantidad vendidos', fontsize=10)
    
    plt.show(block=False)

    # gráfico de barras apilados
    meses = ['1', '2', '3']

    alimentos = np.array([alimentos_1, alimentos_2, alimentos_3])
    bazar = np.array([bazar_1, bazar_2, bazar_3])
    limpieza = np.array([limpieza_1, limpieza_2, limpieza_3])
    electro = np.array([electro_1, electro_2, electro_3])

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.bar(meses, alimentos, label='Alimentos')
    ax.bar(meses, bazar, bottom=alimentos, label='Bazar')
    ax.bar(meses, limpieza, bottom=[sum(x) for x in zip(alimentos, bazar)], label='limpieza')
    ax.bar(meses, electro, bottom=[sum(x) for x in zip(alimentos, bazar, limpieza)], 
                label='Electro')

    ax.set_facecolor('whitesmoke')
    ax.set_title('Ventas por mes', fontsize=16)
    ax.set_xlabel('Meses', fontsize=10)
    ax.set_ylabel('Cantidad vendida', fontsize=10)
    ax.legend()

    plt.show(block=False)

    # gráfico de barras agrupados
    meses = np.array([1, 2, 3])

    width = 0.2  # dividir la unidad en 5 |espacio|producto|producto|producto|producto|
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.bar(meses, alimentos, width=width, label='Alimentos')
    ax.bar(meses + width, bazar, width=width, label='Bazar')
    ax.bar(meses + 2*width, limpieza, width=width, label='Limpieza')
    ax.bar(meses + 3*width, electro, width=width, label='Electro')

    ax.set_xticks(meses)
    
    ax.set_facecolor('whitesmoke')
    ax.set_title('Ventas por mes', fontsize=16)
    ax.set_xlabel('Meses', fontsize=10)
    ax.set_ylabel('Cantidad vendida', fontsize=10)
    ax.legend()

    plt.show()  

if __name__ == '__main__':
    print("Ejercicios de práctica")

    with open('ventas.csv') as csvfile:
        ventas = list(csv.DictReader(csvfile))

    # ej1(ventas)
    # ej2(ventas)
    # ej3(ventas)
    # ej4(ventas)
    ej5(ventas)    
