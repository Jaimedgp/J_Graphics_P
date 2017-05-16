# Contributing to J_Graphics_P

#### Nuevas Ideas a Implementar
* [Personalizacion de las graficas](#personalizacion)
* [Sumatorios y demas](#sumdemas)

#### Problemas Detectados a Solucionar
* [Varias funciones, 1 sola grafica](#varias_funciones)
* [Escala de los ejes](#escalas)
* [Aleatoriedad del Formula Entry](#Aleatoriedad)

<!-- ### Mejoras Posibles -->

## Nuevas Ideas a Implementar

### <a name="personalizacion"></a> Personalizacion de las graficas

Esta idea ha surgido tras realizar una de las practicas de laboratorio de la carrera en la que necesitaba representar los datos usando la escala logaritmica en los ejes. 

Actualmente el programa no te permite personalizar nada de la grafica y tan solo se pueden cambiar los nombre de los ejes y si se representa el ajuste o no. Estaria bien poder permitir algo mas de personalizacion, o por lo menos poner una forma facil de poder cambiar los ejes a escala logaritmica.

Para ello habria que modificar la clase del archivo Plot_Graph que es la encargada de crear el objeto grafica. Esta clase utiliza la libreria [matplotlib](http://matplotlib.org/).

Ademas la forma en la que el usuario interactue con esta nueva funcion puede ser añadiendo un nuevo menu en el toolbar. Para ello habria que modificar el archivo MainWindow.py.

### <a name="sumdemas"></a> Sumatorio y demás

Como otra de las funciones se podria abrir una ventana en la que te muestre sumatorio, media, ...

## Problemas Detectados a Solucionar

### <a name="varias_funciones"></a> Varias funciones

La idea es poder representar en una misma grafica diferentes tomas de datos para una misma variable independiente y asi poder compararlos de forma mas visual. Para ello se indica mediante un CheckBox si se quiere borrar la anterior grafica o no (Re-Plot).

El problema esta que al representar la nueva grafica a partir de la anterior el intervalo de los ejes se calcula con los valores nuevos de tal manera que se pueden perder algunos puntos de la anterior grafica. Este código se encuentra en la clase del archivo GraphPlot.py.

### <a name="escalas"></a> Escala de los ejes

A la hora de crear la ventana de la gráfica se han de definir los intervalos de los ejes entre los cuales se quiere hacer la representación. Para ello se deja de margen la mitad del intervalo mayor entre puntos para cada eje. Dicho codigo se encuentra en las lineas [54, 61] del archivo GraphPlot.

Sin embargo, cuando los valores del eje y en vez de ir de menor a mayor van de mayor a menor, los ejes cortan la grafica perdiendo información.

Se quiere buscar una forma de solucionar este problema pero tambien se busca una nueva forma de obtener los ejes correctos para que en la grafica se observen correctamente los datos.

### <a name="Aleatoriedad"></a> Aleatoriedad del Formula Entry

El Formula Entry no permite modificar columnas con datos. El codigo del Formula Entry se encuentra en el archivo Calculator.

## Mejoras Posibles

### <a name="tamano"></a>Tamaño de los titulos y números en la gráfica
