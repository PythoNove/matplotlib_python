#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def ej1():
    # Line Plot
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = list(range(-10, 11, 1))
    
    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x

    y1 = [ numero**2 for numero in x ] 
    y2 = [ numero**3 for numero in x ]
    y3 = [ numero**4 for numero in x ]

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    fig = plt.figure()
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    ax1.plot(x, y1, color='b', marker='*', label='y1 = x^2')
    ax1.set_facecolor('whitesmoke')
    ax1.set_title('Curva de función y=x^2')
    ax1.set_ylabel('valores y')
    ax1.set_xlabel('valores x')
    ax1.grid(ls='solid')
    ax1.legend()

    ax2.plot(x, y2, color='r', marker='^', label='y2 = x^3')
    ax2.set_facecolor('lightgray')
    ax2.set_title('Curva de función y=x^3')
    ax2.set_ylabel('valores y')
    ax2.set_xlabel('valores x')
    ax2.grid(ls='dashed')
    ax2.legend()

    ax3.plot(x, y3, color='g', marker='.', label='y2 = x^4')
    ax3.set_facecolor('blanchedalmond')
    ax3.set_title('Curva de función y=x^4')
    ax3.set_ylabel('valores y')
    ax3.set_xlabel('valores x')
    ax3.grid(ls='solid')
    ax3.legend()

    plt.show()


def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = np.arange(0, 4*np.pi, 0.1)

    # Realizar dos gráficos que representen
    # y1 = sin(x)
    # y2 = cos(x)
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x

    y1 = np.sin(x)
    y2 = np.cos(x)

    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.

    fig = plt.figure('Funciones Trigonométricas')  # coloca el titulo en la ventana :)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.scatter(x, y1, color='r', marker='.', label='y = sen(x)')
    ax1.set_facecolor('papayawhip')
    ax1.set_title('Gráfico de función seno')
    ax1.set_xlabel('rad')
    ax1.set_ylabel('seno de x')
    ax1.grid(ls='solid')
    ax1.legend()

    ax2.scatter(x, y2, color='g', marker='*', label='y = cos(x)')
    ax2.set_facecolor('lightgray')
    ax2.set_title('Gráfico de función coseno')
    ax2.set_xlabel('rad')
    ax2.set_ylabel('coseno de x')
    ax2.grid(ls='solid')
    ax2.legend()

    plt.show()

def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]

    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.

    fig = plt.figure('Gráfico de barras')
    fig.suptitle('Lenguajes', fontsize=14)
    ax = fig.add_subplot()

    ax.bar(lenguajes, performance, label='lenguajes')
    ax.set_facecolor('whitesmoke')
    ax.legend()
    ax.grid(ls='dashed')

    plt.show()


def ej4():
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }

    # El gráfico debe tener usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico

    fig = plt.figure('Gráfico de Torta')
    ax = fig.add_subplot()
    
    explode = (0.1, 0, 0, 0, 0, 0, 0)
    ax.pie(uso_lenguajes.values(), labels=uso_lenguajes.keys(), autopct='%1.1f%%',
            shadow=True, startangle=90, explode=explode)
    ax.axis('equal')
    ax.set_facecolor('lightgray')
    ax.set_title('Uso de lenguajes de programación', fontsize=20)
    
    plt.show()


def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]

    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valoresde "X" e "Y" para poder utilizar
    # el line plot y observar la señal

    # signal_x = [....]
    # signal_y = [....]

    signal_x = [x.get('X') for x in signal]
    signal_y = [y.get('Y') for y in signal]

    # plot(signal_x, signal_y)

    fig = plt.figure('Señal senosoidal')
    ax = fig.add_subplot()
    ax.plot(signal_x, signal_y, color='r', marker='', label='y=sin(x)')
    ax.set_facecolor('lightgray')
    ax.set_title('Señal senosoidal')
    ax.set_xlabel('Amplitud')
    ax.set_ylabel('sin(x)')
    ax.legend()
    ax.grid(ls='solid')

    plt.show(block=False)
    
    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7

    # filter_signal_x = [....]
    # filter_signal_y = [....]

    filter_signal_x = [x.get('X') for x in signal if abs(x.get('Y')) > 0.7] 
    filter_signal_y = [y.get('Y') for y in signal if abs(y.get('Y')) > 0.7]
    
    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot
    
    fig = plt.figure('Señal senosoidal')
    ax = fig.add_subplot()
    ax.plot(signal_x, signal_y, color='r', marker='', label='y=sin(x)')
    ax.scatter(filter_signal_x, filter_signal_y, color='g', marker='.', label='abs(y) > 0.7')
    ax.set_facecolor('lightgray')
    ax.set_title('Señal senosoidal')
    ax.set_xlabel('Amplitud')
    ax.set_ylabel('sin(x)')
    ax.legend()
    ax.grid(ls='solid')

    plt.show()

    # plot(signal_x, signal_y)
    # scatter(filter_signal_x, filter_signal_y)

    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    ej5()
