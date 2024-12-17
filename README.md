# Análisis de Datos Avanzado
**Objetivo**: Desarrollar un modelo predictivo para estimar el precio promedio del aguacate en el próximo año en una de las regiones con mayor demanda en Estados Unidos, con el fin de establecer estrategias para la apertura de una nueva sucursal en el mercado.

**Integrantes**:
- Albert Bañeres Rovirosa
- Cristian Largo Reina
- Elvis Ortega Ochoa

**Planificación:** [Github Projects](https://github.com/users/arboldeku/projects/1)

## **Calidad de datos**

### **Base de datos de venta de aguacates (2021 - Noviembre de 2024) - Hass Avocado Board**
### **Base de datos de proveedores de aguacates (2022-2024) - Hass Avocado Board**
### **Base de datos de ventas de aguacates y proveedor en California (2022-2024)**

## **Exploración de datos**

### **Análisis bivariado de la venta de aguacates en las grandes regiones y California**
### **Análisis de elasticidad de la demananda considerando los días festivos del año**

## **Modelo predictivo**


<!-- 
## Introducción

Este es el proyecto final para los estudiantes que participan en el curso. Los participantes podrán elegir, según su situación, entre las siguientes opciones:

1. **Opción 1**: Los estudiantes que participaron en el "proyecto-2-cohortes-avanzados" pueden:
   - Continuar y ampliar el **"proyecto-1-regresion"**.
   - Continuar y ampliar el **"proyecto-2-cohortes-avanzados"**.
   - Presentar un **proyecto nuevo**, que involucre como mínimo las bases de los proyectos 1 y 2.
   - Trabajar en grupos de **1 a 3 personas**.

2. **Opción 2**: Los estudiantes que **no participaron en el proyecto 2** (proyecto-2-cohortes-avanzados) solo pueden presentar un **proyecto nuevo** que involucre como mínimo las bases de los proyectos 1 y 2. Este nuevo proyecto **no debe involucrar los datos de los proyectos 1 y 2**.
   - Trabajar en grupos de **1 a 2 personas**.

## Requisitos obligatorios para todos los proyectos finales

Todos los proyectos finales deben cumplir con los siguientes requisitos mínimos:

1. **Análisis de Series de Tiempo**: Realizar un análisis exhaustivo de las tendencias y patrones temporales presentes en los datos.
2. **Análisis Exploratorio de Datos (EDA)**: Identificar patrones, anomalías y relaciones entre las variables mediante visualizaciones y estadísticas descriptivas.
3. **Análisis de Calidad de los Datos**: Evaluar la calidad de los datos, identificando problemas como valores faltantes, inconsistencias, errores o duplicados.
4. **Análisis Gráfico de los Datos**: Representar gráficamente las variables mediante gráficos como histogramas, diagramas de dispersión, boxplots, entre otros, para facilitar la comprensión visual de los datos.
5. **Segmentación Inteligente de los Datos**: Implementar técnicas de segmentación avanzadas que aporten valor al análisis y la extracción de insights relevantes.
6. **Análisis de Correlación**: Evaluar las relaciones y asociaciones entre las variables mediante matrices de correlación y análisis de dependencias.
7. **Análisis de Outliers**: Detectar y tratar los valores atípicos (outliers) presentes en los datos para mejorar la precisión de los modelos.
8. **Análisis de Cohortes Avanzados**: Realizar segmentación y análisis del comportamiento de los usuarios a lo largo del tiempo, con el objetivo de identificar patrones de retención, uso y otros comportamientos clave.
9. **Modelos de Regresión Regularizados**: Implementar modelos de regresión regularizados (como Ridge, Lasso, ElasticNet), utilizando técnicas de búsqueda de hiperparámetros para optimizar el rendimiento del modelo.
10. **Modelos de Clasificación**: Desarrollar y optimizar modelos de clasificación (como árboles de decisión, SVM, k-NN), utilizando los métodos adecuados de validación y evaluación.
11. **Validación de Modelos**: Seleccionar los mejores modelos mediante validación cruzada con k-fold, para asegurar la robustez y generalización de los modelos creados.
12. **Uso de Scraping para Variables Exógenas**: El proyecto debe incluir el uso de técnicas de web scraping para obtener variables adicionales de fuentes externas que aporten valor a los datos originales del proyecto.

## Gestión del Proyecto

La gestión del proyecto es obligatoria y se llevará a cabo a través de **GitHub Projects**. No se aceptarán excepciones. Debes utilizar la plataforma para organizar las tareas, hacer un seguimiento de los avances y colaborar con tu equipo de manera eficiente.

- **Crear un Proyecto en GitHub Projects**: Asegúrate de organizar las tareas y entregables de manera clara y ordenada.
  - Referencia: [Cómo crear un proyecto en GitHub](https://docs.github.com/es/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project)

## Entregables del Proyecto Final

1. **Código en Python**:
   - El código debe estar bien documentado, organizado y estructurado.
   - Debe incluir el preprocesamiento de los datos, implementación de modelos, análisis requeridos y visualizaciones.
   - El código debe ser comprensible y eficiente.

2. **Informe del Análisis Exploratorio de Datos (EDA)**:
   - Un informe en formato markdown que resuma los hallazgos clave del análisis exploratorio.
   - Incluir visualizaciones de los patrones encontrados y explicaciones claras sobre las conclusiones obtenidas.

3. **Informe de Calidad de los Datos**:
   - Un informe detallado sobre la calidad de los datos, incluyendo los problemas identificados y las acciones tomadas para mejorarlos (tratamiento de valores faltantes, inconsistencias, etc.).

4. **Modelos Predictivos**:
   - Los modelos de regresión regularizados y clasificación deben estar bien optimizados.
   - Incluir la búsqueda de hiperparámetros para obtener el mejor rendimiento.
   - Presentar los resultados de la validación cruzada (k-fold) y realizar un análisis de los residuos.

5. **Presentación Ejecutiva**:
   - Un informe conciso que resuma los hallazgos clave, análisis realizados, y los modelos implementados.
   - Este resumen debe estar incluido en el archivo `README.md` del repositorio de GitHub y será la única parte utilizada durante las exposiciones para defender el proyecto.

6. **Repositorio en GitHub**:
   - El código debe ser subido a un repositorio en GitHub.
   - El repositorio debe contener el archivo `README.md` con una descripción clara y precisa del proyecto.
   - El repositorio debe estar estructurado de manera que facilite la revisión y comprensión del trabajo.
   - Asegúrate de documentar adecuadamente el proyecto, utilizando **commits** frecuentes y significativos.

## Evaluación

La evaluación de los proyectos se basará en los siguientes criterios:

- La **calidad y claridad** del código.
- La **profundidad y coherencia** del análisis realizado.
- La **correcta interpretación** de los resultados obtenidos.
- La **calidad y precisión** del informe `README.md` en el repositorio de GitHub.
- El **uso adecuado** de herramientas de gestión de proyectos (GitHub Projects).
- La **innovación y aplicabilidad** de los insights generados, especialmente en términos de valor para la organización.

**¡Esperamos tus valiosas contribuciones y te deseamos mucho éxito en el proyecto final!** -->

### Análisis Univariado

**Distribuciones con Outliers**

Observamos distribuciones mcho mas constantes en las variables 4046 y 4770, en cambio para el tipo de bolsa asignado al 4225 vemos una varianza con tendencia a la bajada de ventas de ese tipo de bolsa.

Claramente deberiamos segmentar el tipo de bolsa sobre el que queremos atacar en el mercado ya que aparentemente tienen diferentes comportamientos en cuanto a ventas.



![Distribución de 4046, 4770 y 4225](imagenes/distribuciones_outliers.png)




**Distribución del precio promedio (ASP) en California**:

Vemos claramente dos segmentos de Precio Promedio en los rangos de 1.1 - 1.4 y otro en 1.6 - 1.9 que se corresponden a los precios sobre los cuales se han ejecutado los mayores volumenes de venta.

También vemos como la Claisificación para los niveles asignados de precio confirma ese mayor volumen para las cantidades con precios de 1 - 1.5 y > 1.5 

Así como podemos apreciar también rangos más amplios en los precios de los Medium - High y una menor variación en los posibles precios para la categoria Low.

![Distribución ASP California](imagenes/ASP_california.png)

![Distribución ASP niveles](imagenes/distribucion_asp_niveles.png)



**Precio Promedio por trimestre en California**

Observamos un gran pico en los primeros 3 trimestres de 2022, justo despés el mercado rectifica fuertemente el precio, y con el inicio de 2024 vuelve a la tendencia creciente aunque no con suficientes indicativos como para poder preveer un maximo en el precio promedio de California.

Parece ser que debido a causas externas como desastres medioambientales y politicas restrictivas hacia los productos de importacion en EEUU causaron este efecto.



![Precio Promedio Trimestral_California](imagenes/precio_promedio_trimestral_california.png)




**Rendimiento de ventas por Cohortes de Precio Low, Medium, High**

Observamos como los rendimientos de ventas para los precios en High se mantinenen en minimos y solo a medidados de 2022 experimentan un pico de ventas que no se vuelve a repetir.

Las ventas en nivel Medium son las que tienen un mayor valor total de volumen de ventas sostenido en el tiempo pero hay picos que sobrepasan esas cantidades con precios Low qe coinciden con la festividad de Febrero (SuperBowl)




![Rendimiento de Ventas por Cohorte de Precio ASP en California](imagenes/cohortes_ventas_level.png)




**Distribción Precio Promedio por Regiones en Festividades**

En general, los comportamientos entre las diferentes regiones son estables a lo largo de los eventos, con oscilaciones moderadas.



![Distribución del Precio Promedio durante las Festividades por Región](imagenes/Precio_Promedio_festividades_region.png)




**Evolución Precio Promedio durante las Festividades en California**

Vemos claramente como Memorial Day, Independence Day,Superbowl y Labor Day han crecido en el precio promedio sobre el cual se vende durante la festividad así como Thanksgiving y Christmas pierden valor. Buen indicativo para hacer campañas de marketing y promociones para los eventos en crecimiento de Precio Promedio



![Evolución Precios Promedio Festividad por Región](imagenes/precios_promedio_festividades_california.png)



**Precios por Region en Festividades**

Vemos como a pesar de las diferentes festividades siguen comportandose las regiones de una manera muy similar.



![Tendencia Precios por Region en Festividad](imagenes/precios_festividad_region.png)




**Heatmap de calor Precios por Mes y Festividad**

Observamos como los mejores precios en Festividades son para los que se encuentran en Periodo estivales y que coinciden con la mejor época del Aguacate. Esto podría ser una oportunidad para mejorar la experiencia del cliente y aumentar los ingresos en las fechas clave de Independence Day y Memorial Day.



![Distribución de Segmentos de Usuario](imagenes/heatmap_precios_festivos.png)



**Volumen Ventas Promedio Festividades**

Vemos como claramente el mayor evento respecto a la cantidad de Volumen de Ventas es para la SuperBowl y año nuevo.



![Volumen de Ventas Promedio durante las Festividades](imagenes/volmen_ventas_promedio_festividades.png)



**Elasticidad Precio durante las Festividades**

Observamos como las festividades más sensibles a cambios en la preferencia de consumo de los usuarios son, Independence day y Memorial day, lo que podría ser una buena oportunidad para promocionar productos relacionados con estas festividades.



![Elasticidad Precio durante las Festividades](imagenes/elasticidad_precio_festividades.png)

# Informe de Series Temporales

### Introducción

En este informe se discuten los hallazgos obtenidos para ver si estamos tratando con datos que tienen un componente de estacionalidad y con que fuerza estos influyen sobre el precio. Antes de empezar con el target de California, queremos destacar cómo se ha comportado el precio del Aguacate en EEUU y cómo viendolo a simple vista nos ha hecho sospechar que aquí hay una estacionalidad elevada.

![precio aguacate totalUS](/graficos_imagenes/precio%20aguacate%20totalUS.png)

### Análisis temporalidad en EEUU

![Estacionalidad TotalUS](/graficos_imagenes/Estacionalidad%20TotalUS.png)

Observando estos datos, obtenemos el insight de que se produce una estacionalidad elevada durante los meses de verano, con picos en junio y julio, vamos a analizar por greater region que tal son las estacionalidades en cada región.

![Estacionalidad por regiones](/graficos_imagenes/Estacionalidad%20por%20regiones.png)

No tan sólo es un fenómeno que se produce en el total de EEUU, sinó que también se produce en mayor o menor medida en el resto de regiones. Vemos que en Southeast y en Midshouth es dónde encontramos mayores picos de estacionalidad. 

Una de las claves és segmentar a Hass Avocado, dependiendo de si és de tipo convencional o de tipo orgánico. En el primer estudio para ver que tendencia seguía este modelo, se utilizó una linea de tendencia interpolada con datos ya conocidos, junto con una extrapolación de los datos futuros en el año 2025 con datos desconocidos. 

![Interpolacion + Extrapolacion](/graficos_imagenes/Interpolacion%20+%20Extrapolacion.png)

Se puede ver para éste gráfico de precios del aguacate orgánico, como hay una serie de outliers que dificultan que la linea pueda dar acotarse a los valores predichos, indicando un ajuste pobre, si intentamos utilizar interpolación para rellenar datos faltantes. 

![Interpolacion + Extrapolacion Convencionales](/graficos_imagenes/Interpolacion%20+%20Extrapolacion%20Convencionales.png)

Aquí el scatter nos muestra aún una mayor dispersión de los datos, por lo tanto una tarea más compleja de capturara para estos modelos de interpolación polinomicas. 

El objetivo era utilizar interpolación para poder hallar datos faltantes de manera suavizada, dentro de los periodos conocidos. El vector con los valores observados no se utilizó implicitamente, pero podemos interpretarlo como el conjunto de valores generados a través de la interpolación de la tendencia. En este caso específico, hemos utilizado "tendencia_interpolada_conventional", que es el resultado de interpolar los valores de la tendencia que obtenemos tras descomponer la serie temporal con "seasonal_decompose". Esto suaviza los valores de la tendencia a lo largo del tiempo, proporcionando estimaciones más continuas de la tendencia, especialmente en periodos donde los datos de la tendencia original podrían faltar o ser irregulares.

![Residuos interpolacion](/graficos_imagenes/Residuos%20interpolacion.png)

![Residuos interpolacion convencional](/graficos_imagenes/Residuos%20interpolacion%20convencional.png)

Podemos ver aquí como se aprecia que el ruido es mucho mayor en los aguacates de tipo convencional que no en los de tipo orgánicos, ya que los residuos de la interpolación están más alejados de 0.

Los datos de interpolación arrojaron los siguientes MSE: 

Error Absoluto Medio Aguacate Convencional (MAE): 0.5617444143101235
Error Cuadrático Medio Aguacate Convencional (RMSE): 0.5760666670544891
Error Absoluto Medio Aguacate Orgánico (MAE): 0.07694878147462166
Error Cuadrático Medio Aguacate Orgánico (RMSE): 0.5760666670544891

### Análisis en California

![Aguacates california temporalidad](/graficos_imagenes/Aguacates%20california%20temporalidad.png)

![Residuos aguacate california temporalidad](/graficos_imagenes/Residuos%20aguacate%20california%20temporalidad.png)

Para el caso de California tenemos datos muy parecidos a los agregados en Total US. Estamos viendo que la interpolación es más certera en los aguacates orgánicos y muy poco ajustada para los aguacates convencionales. Justamente la gráfica de residuos vendría a decir lo mismo o parecido a los resultados de EEUU al completo. 

Después decidimos ir haciendo ajustes a esta interpolación y empezamos con la interpolación Polinómica de grado 2. Después de realizar una selección de alpha óptimo a traves de validación cruzada con K-Fold, fuimos ajustando los valores del polinomio desde 2 hasta 5. El mejor ajuste lo capturaba el polinomio de grado 3 y estos fueron los resultados que obtuvimos:

![Interpolacion Polinomica grado 2](/graficos_imagenes/Interpolacion%20Polinomica%20grado%202.png)

![Interpolacion Polinomica grado 3](/graficos_imagenes/Interpolacion%20Polinomica%20grado%203.png)



# Análisis y Modelado de Precios del Aguacate en California (2021-2024)

### Propósito del análisis

El objetivo fue analizar el consumo interno y la exportación de aguacates Hass producidos en California, para comprender mejor su impacto en el precio local. California, siendo un gran consumidor y exportador, presentaba características únicas que influían en los precios debido a factores como costes de producción y elasticidad de la demanda.

### Tasa interna de Consumo

Se estimó un coeficiente del peso del consumo de aguacates en California frente a otras regiones de EE.UU. A partir de ello, se calculó la *Tasa Local de Consumo de California* como:
Exportaciones / (Consumo Total de California × Coeficiente de Peso Relativo).

Esto permitió ajustar los datos scrappeados y realizar un análisis más preciso. Se aplicaron escalas logarítmicas para normalizar variables con diferentes dimensiones.

Pesos regionales:
- California: 0.1577
- Great Lakes: 0.1087
- Midsouth: 0.1053
- Northeast: 0.1153
- Plains: 0.0564
- South Central: 0.1334
- Southeast: 0.1629
- West: 0.1603

Otra cosa importante a tener en cuenta era que al tener datos con frecuencias muy distintas (datos en millones y datos en valores más pequeños), nos disponemos a hacer un modelo LinLog, es decir, aplicar escala logarítmica a aquellos datos que tengan dimensiones en miles o millones.

![Grafico caja elasticidad](/graficos_imagenes/grafico%20caja%20elasticidad.png)

![Elasticidad sin outliers](/graficos_imagenes/Elasticidad_sin_outliers.png)

Se tuvo que arreglar antes de modelar los modelos de regresión los outliers en la Elasticidad. 

### Modelos de Regresión Lineal Múltiple:

![Resultados MCO](/graficos_imagenes/Resultados%20MCO.PNG)

Vemos que el ajuste del modelo és moderado ya que el Precio del Aguacate sólo viene explicado en un 47,3% por las variables exógenas. 

Razones  de este ajuste moderado:
1. Relaciones no lineales
2. Multicolinealidad
3. Datos insuficientes o ruido
4. Distribución desigual de los datos 

### Modelos de Regularización y comparación con Regresión Lineal

Mejor alpha para Ridge: {'alpha': 0.868511373751352}
Intercepto del modelo: 1.5385934284339489

Error Cuadrático Medio (MSE) en entrenamiento: 0.011024201387216524
Error Cuadrático Medio (MSE) en prueba: 0.06255100596780575

Puntaje R^2 en entrenamiento: 0.48359414791063704
Puntaje R^2 en prueba: 0.4664921181319336

----------------------------------------------------------------------

Mejor alpha para Lasso: {'alpha': 0.001}
Intercepto del modelo: 1.5374798735016735

Error Cuadrático Medio (MSE) en entrenamiento: 0.011056578823687001
Error Cuadrático Medio (MSE) en prueba: 0.05086490060618046

Puntaje R^2 en entrenamiento: 0.4820774940432291
Puntaje R^2 en prueba: 0.4653571802023916

![RIDGE Valor absoluto](/graficos_imagenes/RIDGE%20Valor%20absoluto.png)
![LASSO Valor absoluto](/graficos_imagenes/LASSO%20Valor%20absoluto.png)
![MCO Valores absolutos](/graficos_imagenes/MCO%20Valores%20absolutos.png)

Podemos apreciar que según el modelo que escogamos, el peso será mayor o menor dependiendo de si hemos hecho técnicas de regularización o de regresión lineal. Cabe destacar que para la parametrización de los modelos de regularización se utilizaron los hiperparámetros más óptimos que garantizasen al modelo la mayor robustez posible. Al final se concluye que el ajuste es moderado, a pesar de que el componente estacional y el componente que se hayan mezclado ambos tipos de aguacate hace que el modelo tenga menos capacidad de ajuste.

![Residuos capturando overfitting](/graficos_imagenes/Residuos%20capturando%20overfitting.png)

Este gráfico pero nos puede estar indicando un overfitting ligero, ya que todos los valores de residuos están cerca de 0. 

### Regresión con Máquinas de Soporte Vectorial e Hiperplanos.

![Precios Aguacates orgánicos por semana](/graficos_imagenes/Precio%20aguacates%20organicos%20por%20semana.png)
![Precio aguacates convencionales por semana](/graficos_imagenes/Precio%20aguacates%20convencionales%20por%20semana.png)

Cómo bien sabemos, estos datos tienen un componente de dispersión muy grande. Por ello se decidió utilizar hiperplanos para separar estos datos y hacer clusters e intentar tener algún modelo robusto. 

![Output SVM Convencional](/graficos_imagenes/Output%20SVM%20Convencional.png)
![Output SVM Organico](/graficos_imagenes/Output%20SVM%20Organico.png)

Reporte de clasificación - Orgánicos:
              precision    recall  f1-score   support

        high       0.33      1.00      0.50        10
         low       0.73      0.53      0.62        15
      medium       0.67      0.11      0.18        19

    accuracy                           0.45        44
   macro avg       0.58      0.55      0.43        44
weighted avg       0.61      0.45      0.40        44

Matriz de Confusión - Orgánicos:
[[10  0  0]
 [ 6  8  1]
 [14  3  2]]
AUC para la clase high (Orgánicos): 0.7941176470588236
AUC para la clase low (Orgánicos): 0.8666666666666666
AUC para la clase medium (Orgánicos): 0.5768421052631578

---------------------------------------------------------------------------------

Reporte de clasificación - Convencionales:
              precision    recall  f1-score   support

        high       0.37      0.73      0.49        15
         low       0.41      0.90      0.56        10
      medium       0.00      0.00      0.00        27

    accuracy                           0.38        52
   macro avg       0.26      0.54      0.35        52
weighted avg       0.18      0.38      0.25        52

Matriz de Confusión - Convencionales:
[[11  4  0]
 [ 1  9  0]
 [18  9  0]]
AUC para la clase high (Convencionales): 0.7387387387387387
AUC para la clase low (Convencionales): 0.8904761904761904
AUC para la clase medium (Convencionales): 0.5333333333333333

---------------------------------------------------------------------------------

Precisión del modelo: 95.24%

Reporte de clasificación:
precision    recall  f1-score   support

Conventional       0.95      0.95      0.95        42
     Organic       0.95      0.95      0.95        42

    accuracy                           0.95        84
   macro avg       0.95      0.95      0.95        84
weighted avg       0.95      0.95      0.95        84

La matriz de confusión nos da una precisión bastante elevada tanto de identificación de falsos positivos y falsos negativos, como de coeficiente de recall. 

Para ello se han utilizado los siguientes pasos: 
. Usar un set de prueba del 20% i uno de entrenamiento del 80%
. Creamos un modelo de soporte vectorial de dos dimensiones ya que estamos haciendo un análisis bidimensional. 

![Hiperplanos avocados](/graficos_imagenes/Hiperplanos%20avocados.png)

Precisión promedio del modelo con validación cruzada: 92.77%
Desviación estándar de la precisión: 9.37%

Apreciamos en este hiperplano como el modelo puede distinguir entre los aguacates de tipo orgánicos y de tipo convencional. Y cómo según el precio promedio que tenga, el modelo será capaz de distinguir que aguacates són convencionales y cuales són orgánicos. 

### Regresión mediante procesos estocásticos: ARIMA

ARIMA (Autoregressive Integrated Moving Average) es un modelo estadístico diseñado para trabajar con series temporales, considerando la dependencia entre valores presentes, pasados y errores previos. Este enfoque es diferente a la regresión lineal múltiple, que asume independencia entre observaciones.

Parámetros clave:

p: Número de rezagos autoregresivos que explican valores pasados.
d: Diferenciación para estabilizar la media y varianza.
q: Rezagos de errores previos considerados.

En el análisis, se utilizó un modelo SARIMAX (1, 1, 1)x(1, 1, 1, 52) con componente estacional semanal (52 semanas). Esto implica:

p = 1: Un rezago autoregresivo.
d = 1: Diferenciación de primer orden para estacionariedad.
q = 1: Un rezago de errores pasados.

![SARIMAX](/graficos_imagenes/SARIMAX.PNG)

Estadístico ADF: -2.858183261545553
Valor p: 0.05043128970952864

1. Podemos confirmar que el modelo es estacionario ya que el contraste de Dickey-Fuller nos confirma que el p-valor es = 0.05 --> Se rechaza la hipotesis nula.

2. Hemos utilizado concretamente un modelo SARIMAX (1, 1, 1) x (1 , 1, 1, 52)

![ARIMA 2](/graficos_imagenes/arima%202.png)

![Distribución de residuos ARIMA](/graficos_imagenes/distribucion_residuos_arima.png)

3. Este gráfico nos muestra que los residuos no se comportan de manera estandarizada, és decir que no siguen un ruido de camino blanco.

![FAS i FAP ARIMA](/graficos_imagenes/FAS%20i%20FAP%20ARIMA.png)

4. La FAS i la FAP, nos devuelven que claramente se evidencia una tendencia estacional, ya que los rezagos que hay con las temporalidades del periodo t, vienen correlacionadas desde varios periodos atrás.


