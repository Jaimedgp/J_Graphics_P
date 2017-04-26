# Contributing to J_Graphics_P

#### Nuevas Ideas a Implementar
* [Varias funciones, 1 sola grafica](#varias_funciones)
* [Personalizacion de las graficas](#personalizacion)

#### Problemas Detectados a Solucionar
* [Escala de los ejes](#escalas)
* [Aleatoriedad del Formula Entry](#Aleatoriedad)

#### Mejoras Posibles 
* Tamaño de los titulos y numeros en la grafica
* Volver a hacer útil la funcion Errors en el Formula Entry

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

A la hora de crear la ventana de la gráfica se han de definir los intervalos de los ejes entre los cuales se quiere hacer la representación.

### <a name="Aleatoriedad"></a> Aleatoriedad del Formula Entry

El Formula Entry no permite modificar columnas con datos
