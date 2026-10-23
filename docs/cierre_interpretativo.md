# Cierre Interpretativo - U03.LAB08
**Asignatura:** INF-8239 Ciencia de Datos II
**Unidad:** 03 · Algoritmos y características generativas

---

## 1. Resultado principal
Se implementó con éxito un sistema recomendador reproducible que incluye un modelo *baseline* de popularidad suavizada y un recomendador basado en contenido utilizando la métrica de similitud coseno sobre los vectores TF-IDF de los géneros. Además, se configuró un entorno virtual, se superaron restricciones de red para la obtención de datos y se versionó el proyecto completo en Git.

## 2. Evidencia utilizada
* Dataset **MovieLens Latest Small** validado mediante el script de auditoría (que confirmó el hash SHA-256 y la volumetría de usuarios e ítems).
* Reporte generado en `reports/content_recommendations.csv`.
* Pruebas automatizadas (pytest) ejecutadas sin errores.
* Visualización final a través de la interfaz local en Streamlit.

## 3. Qué representa la similitud
En este modelo, la similitud coseno representa estrictamente la cercanía de las características vectoriales en el catálogo (qué tantos géneros comparten dos películas). **No representa adivinación de gustos ni calidad**; dos películas son similares simplemente porque sus metadatos (etiquetas de género) coinciden matemáticamente, independientemente de si al usuario le gustará la trama o no.

## 4. Problema de cold start observado
* **Ítems nuevos:** Si se agrega una película nueva al catálogo que no tiene géneros etiquetados, el recomendador por contenido no tendrá un vector válido para compararla y nunca la recomendará.
* **Usuarios nuevos:** Un usuario completamente nuevo no tiene interacciones previas, por lo que el sistema no sabe qué características buscar para él (aunque el *baseline* de popularidad actúa como solución temporal para este caso).

## 5. Riesgo de sobre-especialización
El recomendador por contenido tiende a encerrar al usuario en una "burbuja" (poca cobertura de catálogo). Si un usuario consulta una película de "Animación/Infantil", el Top-10 estará dominado exclusivamente por películas con exactamente esas etiquetas, repitiendo características ya conocidas y eliminando la posibilidad de descubrir géneros nuevos o relacionados.

## 6. Decisión o siguiente experimento
Para solucionar la sobre-especialización, el siguiente paso lógico es implementar un modelo de **Filtro Colaborativo** (Collaborative Filtering) o un sistema híbrido. Esto permitiría recomendar películas basándose en los patrones de consumo de otros usuarios similares, introduciendo diversidad en las recomendaciones sin depender exclusivamente de los géneros literales.