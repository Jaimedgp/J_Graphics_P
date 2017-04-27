# Contributing to J_Graphics_P

#### Nuevas Ideas a Implementar
* [Varias funciones, 1 sola grafica](#varias_funciones)
* [Personalizacion de las graficas](#personalizacion)

#### Problemas Detectados a Solucionar
* [Escala de los ejes](#escalas)
* [Aleatoriedad del Formula Entry](#Aleatoriedad)

#### Mejoras Posibles 
* [Tamaño de los titulos y numeros en la grafica](#tamano)
* [Volver a hacer útil la funcion Errors en el Formula Entry](#funcion_error)

## Nuevas Ideas a Implementar

### <a name="varias_funciones"></a> Varias funciones

La idea es poder representar en una misma grafica diferentes tomas de datos para una misma variable independiente y asi poder compararlos de forma mas visual.

El problema para esto es ver la forma en la que el usuario escoge que columnas quiere representar, pues la interfaz actual solo permite escoger dos columnas (eje X y eje Y).

Para ello habria que modificar los siguientes archivos:

>* Del archivo ToolsWidgets.py la clase GraphAxes que crea la interfaz necesaria para escoger las columnas que se representaran.

>* La clase del archivo Plot_Graph que es la encargada de crear el objeto grafica. Esta clase utiliza la libreria [matplotlib](http://matplotlib.org/).

Ademas habria que estudiar la forma en la que ambas clases se comunican para ejecutar la funcion. En caso de no encontrar la forma de conectarlas directamente sin tener que utilizar ninguna otra clase, se podrian modificar las clases de los archivos MainWindow.py y MainLayout.py.

### <a name="personalizacion"></a> Personalizacion de las graficas

Esta idea ha surgido tras realizar una de las practicas de laboratorio de la carrera en la que necesitaba representar los datos usando la escala logaritmica en los ejes. 

Actualmente el programa no te permite personalizar nada de la grafica y tan solo se pueden cambiar los nombre de los ejes y si se representa el ajuste o no. Estaria bien poder permitir algo mas de personalizacion, o por lo menos poner una forma facil de poder cambiar los ejes a escala logaritmica.

Para ello habria que modificar la clase del archivo Plot_Graph que es la encargada de crear el objeto grafica. Esta clase utiliza la libreria [matplotlib](http://matplotlib.org/).

Ademas la forma en la que el usuario interactue con esta nueva funcion puede ser añadiendo un nuevo menu en el toolbar. Para ello habria que modificar el archivo MainWindow.py.

## Problemas Detectados a Solucionar

### <a name="escalas"></a> Escala de los ejes

A la hora de crear la ventana de la gráfica se han de definir los intervalos de los ejes entre los cuales se quiere hacer la representación. Para ello se deja de margen la mitad del intervalo mayor entre puntos para cada eje. Dicho codigo se encuentra en las lineas [54, 61] del archivo GraphPlot.

Sin embargo, cuando los valores del eje y en vez de ir de menor a mayor van de mayor a menor, los ejes cortan la grafica perdiendo información.

Se quiere buscar una forma de solucionar este problema pero tambien se busca una nueva forma de obtener los ejes correctos para que en la grafica se observen correctamente los datos.

### <a name="Aleatoriedad"></a> Aleatoriedad del Formula Entry

El Formula Entry no permite modificar columnas con datos. El codigo del Formula Entry se encuentra en el archivo Calculator.

## Mejoras Posibles

### <a name="tamano"></a>Tamaño de los titulos y números en la gráfica
### <a name="funcion_error"></a> Funcion Errors en Formula Entry

Todavia no se ha implementado la función Errors del Formula Entry a la nueva estructura del programa. La anterior versión del programa trabajaba los datos como atributos de una clase en vez de utilizar diccionarios y todavia no se ha implementado el codigo de la función para que trabaje de la nueva forma.

El codigo de la funcion Errors se encuentra en la clase Operations del archivo Calculator, a partir de la linea 105. Dicha función utiliza la función ErrorsCalculator del archivo WidgetsScript que se encuentra en las lineas [85,114]. 
