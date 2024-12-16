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
