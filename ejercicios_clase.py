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
    # Se desea graficar los valores de X e Y en un gráfico de línea

    # Función que se desea graficar:
    # y1 = x**2

    x = list(range(-10, 11, 1))
    # Estamos aprovechando el concepto de comprension de listas
    # para generar los valores que toma "Y" por cada valor de "X"
    y = [i**2 for i in x]

    # Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "Y" en función de "X"
    # Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(x, y)
    ax.set_facecolor('lightgray')
    ax.plot(x, y, color='m', label='y1 = x**2')
    ax.set_ylabel('y = [i**2 for i in x]')
    ax.set_xlabel('x = list(range(-10, 11, 1))')
    ax.legend()
    plt.show()
    

def ej2():
    # Line Plot
    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación es la siguiente:
    x = list(np.linspace(-4, 4, 20))
    # Estamos aprovechando el concepto de comprension de listas
    # para generar los valores que toma "Y" por cada valor de "X"
    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]

    # Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    fig = plt.figure()
    ax = fig.add_subplot()

    # Se debe colocar en la leyenda la función que representa
    # cada función

    ax.plot(x, y1, color='r', marker='+', label='y1 = x**2')
    ax.plot(x, y2, color='m', marker='*', label='y2 = x**3')
    ax.set_facecolor('whitesmoke')
    ax.set_title('Gráfico de comparacion de funciones')
    ax.set_ylabel('Eje Y')
    ax.set_xlabel('Eje X')
    ax.legend()
    
    # Cada función dibujarla con un color distinto
    # a su elección

    plt.show()


def ej3():
    # Scatter Plot
    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función a implementar
    # y = tanh(x) --> tangente hiperbólica

    # Implementacion
    y = np.tanh(x)

    # Graficar la función utilizando "scatter"

    fig = plt.figure()
    ax = fig.add_subplot()

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    ax.scatter(x, y, color='tab:blue', marker='*', label='y = tanh(x)')
    ax.set_facecolor('antiquewhite')
    ax.set_title('Gráfico de tangente hiperbólica')
    ax.set_ylabel('Valores en y')
    ax.set_xlabel('Valores en x')
    ax.legend()
    plt.show()

    # Elegir un marker a elección


def ej4():
    # Figura con múltiples gráficos
    # Line Plot
    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(-10, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección


    # Colocar una grilla a elección

    fig = plt.figure()

    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    ax1.plot(x, y1, color='r', marker='*', label='y1 = x^2')
    ax1.set_facecolor('white')
    ax1.set_title('Gráfico_1')
    ax1.set_xlabel('Valores x')
    ax1.set_ylabel('Valores y')
    ax1.grid(ls='dashed')
    ax1.legend()
    
    ax2.plot(x, y2, color='lime', marker='+', label='y2 = x^3')
    ax2.set_facecolor('ghostwhite')
    ax2.set_title('Gráfico_2')
    ax2.set_xlabel('Valores x')
    ax2.set_ylabel('Valores y')
    ax2.grid(ls='solid')
    ax2.legend()
    
    ax3.plot(x, y3, color='red', marker='.', label='x**4', ls='--')
    ax3.set_facecolor('blanchedalmond')
    ax3.set_title('Gráfico_3')
    ax3.set_xlabel('Valores x')
    ax3.set_ylabel('Valores y')
    ax3.grid(ls='solid')
    ax3.legend()

    ax4.plot(x, y4, color='navy', marker='v', label='raiz_cuadrada(X)')
    ax4.set_facecolor('lightgray')
    ax4.set_title('Gráfico_4')
    ax4.set_xlabel('Valores x')
    ax4.set_ylabel('Valores y')
    ax4.grid(ls='solid')
    ax4.legend()

    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    ej4()
