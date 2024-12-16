# Informe de Series 

### Introducción

En este informe se discuten los hallazgos obtenidos para ver si estamos tratando con datos que tienen un componente de estacionalidad y con que fuerza estos influyen sobre el precio. Antes de empezar con el target de California, queremos destacar cómo se ha comportado el precio del Aguacate en EEUU y cómo viendolo a simple vista nos ha hecho sospechar que aquí hay una estacionalidad elevada.

![precio aguacate totalUS](../graficos_imagenes/Estacionalidad%20TotalUS.png)

### Análisis temporalidad en EEUU

![Estacionalidad TotalUS](../graficos_imagenes/Estacionalidad%20TotalUS.png)

Observando estos datos, obtenemos el insight de que se produce una estacionalidad elevada durante los meses de verano, con picos en junio y julio, vamos a analizar por greater region que tal son las estacionalidades en cada región.

![Estacionalidad por regiones](../graficos_imagenes/Estacionalidad%20por%20regiones.png)

No tan sólo es un fenómeno que se produce en el total de EEUU, sinó que también se produce en mayor o menor medida en el resto de regiones. Vemos que en Southeast y en Midshouth es dónde encontramos mayores picos de estacionalidad. 

Una de las claves és segmentar a Hass Avocado, dependiendo de si és de tipo convencional o de tipo orgánico. En el primer estudio para ver que tendencia seguía este modelo, se utilizó una linea de tendencia interpolada con datos ya conocidos, junto con una extrapolación de los datos futuros en el año 2025 con datos desconocidos. 

![Interpolacion + Extrapolacion](../graficos_imagenes/Interpolacion%20+%20Extrapolacion.png)

Se puede ver para éste gráfico de precios del aguacate orgánico, como hay una serie de outliers que dificultan que la linea pueda dar acotarse a los valores predichos, indicando un ajuste pobre, si intentamos utilizar interpolación para rellenar datos faltantes. 

![Interpolacion + Extrapolacion Convencionales](../graficos_imagenes/Interpolacion%20+%20Extrapolacion%20Convencionales.png)

Aquí el scatter nos muestra aún una mayor dispersión de los datos, por lo tanto una tarea más compleja de capturara para estos modelos de interpolación polinomicas. 

El objetivo era utilizar interpolación para poder hallar datos faltantes de manera suavizada, dentro de los periodos conocidos. El vector con los valores observados no se utilizó implicitamente, pero podemos interpretarlo como el conjunto de valores generados a través de la interpolación de la tendencia. En este caso específico, hemos utilizado "tendencia_interpolada_conventional", que es el resultado de interpolar los valores de la tendencia que obtenemos tras descomponer la serie temporal con "seasonal_decompose". Esto suaviza los valores de la tendencia a lo largo del tiempo, proporcionando estimaciones más continuas de la tendencia, especialmente en periodos donde los datos de la tendencia original podrían faltar o ser irregulares.

![Residuos interpolacion](../graficos_imagenes/Residuos%20interpolacion.png)

![Residuos interpolacion convencional](../graficos_imagenes/Residuos%20interpolacion%20convencional.png)

Podemos ver aquí como se aprecia que el ruido es mucho mayor en los aguacates de tipo convencional que no en los de tipo orgánicos, ya que los residuos de la interpolación están más alejados de 0.

Los datos de interpolación arrojaron los siguientes MSE: 

Error Absoluto Medio Aguacate Convencional (MAE): 0.5617444143101235
Error Cuadrático Medio Aguacate Convencional (RMSE): 0.5760666670544891
Error Absoluto Medio Aguacate Orgánico (MAE): 0.07694878147462166
Error Cuadrático Medio Aguacate Orgánico (RMSE): 0.5760666670544891

### Análisis en California

![Aguacates california temporalidad](../graficos_imagenes/Aguacates%20california%20temporalidad.png)

![Residuos aguacate california temporalidad](../graficos_imagenes/Residuos%20aguacate%20california%20temporalidad.png)

Para el caso de California tenemos datos muy parecidos a los agregados en Total US. Estamos viendo que la interpolación es más certera en los aguacates orgánicos y muy poco ajustada para los aguacates convencionales. Justamente la gráfica de residuos vendría a decir lo mismo o parecido a los resultados de EEUU al completo. 

Después decidimos ir haciendo ajustes a esta interpolación y empezamos con la interpolación Polinómica de grado 2. Después de realizar una selección de alpha óptimo a traves de validación cruzada con K-Fold, fuimos ajustando los valores del polinomio desde 2 hasta 5. El mejor ajuste lo capturaba el polinomio de grado 3 y estos fueron los resultados que obtuvimos:

![Interpolacion Polinomica grado 2](../graficos_imagenes/Interpolacion%20Polinomica%20grado%202.png)

![Interpolacion Polinomica grado 3](../graficos_imagenes/Interpolacion%20Polinomica%20grado%203.png)
