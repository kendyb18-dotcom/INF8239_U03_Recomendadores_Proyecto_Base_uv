# INF-8239 · Unidad 03 · Sistemas Recomendadores

**Autor académico:** Edwin Ramón José Nolasco  
**Estudiante:** Kendy Báez Santos  
**Repositorio:** [INF8239_U03_Recomendadores_Proyecto_Base_uv](https://github.com/kendyb18-dotcom/INF8239_U03_Recomendadores_Proyecto_Base_uv)

## Descripción

Proyecto que integra los laboratorios LAB08 y LAB09 para implementar y evaluar sistemas recomendadores mediante popularidad, filtrado basado en contenido, filtrado colaborativo e híbrido, utilizando MovieLens Latest Small.

## Tecnologías

- Python 3.12 y `uv`
- pandas, NumPy y scikit-learn
- pytest
- Streamlit
- Git y GitHub

## Configuración y ejecución

```bash
uv python install 3.12
uv sync
uv run pytest -q

# Descargar y auditar los datos
uv run python scripts/download_data.py
uv run python scripts/audit_data.py

# LAB08: recomendación por contenido
uv run python scripts/lab08_content.py

# LAB09: modelo híbrido seleccionado
uv run python scripts/lab09_hybrid.py --factors 20 --epochs 12 --alpha 0.75

# Comparación: mayor influencia del contenido
uv run python scripts/lab09_hybrid.py --factors 20 --epochs 12 --alpha 0.25

# Interfaz web
uv run streamlit run app/streamlit_app.py
```

**Nota:** durante el desarrollo se identificaron problemas de conectividad asociados a Zscaler y se sustituyó `np.matrix` por `np.asarray` para mejorar la compatibilidad con scikit-learn.

## Resultados

| Métrica | Alpha 0.75 | Alpha 0.25 |
|---|---:|---:|
| HitRate@10 | **3.74 %** | 3.23 % |
| Cobertura | 7.75 % | **10.64 %** |

El modelo seleccionado utiliza **20 factores y 12 épocas**, con un RMSE aproximado de **1.026** y un tiempo de entrenamiento de **13.8 segundos**.

La configuración `alpha = 0.75` obtuvo el mejor HitRate@10, mientras que `alpha = 0.25` ofreció mayor cobertura del catálogo.

En la comparación de eficiencia, el modelo de 10 factores obtuvo un HitRate@10 de 3.06 % y una cobertura de 5.77 %, con un ahorro de entrenamiento de aproximadamente 0.3 segundos. Por ello, se seleccionó el modelo de 20 factores.

## Conclusiones

- La popularidad sirve como alternativa general ante la falta de historial.
- El filtrado por contenido identifica películas con características similares, pero puede reducir la diversidad.
- El filtrado híbrido combina preferencias colaborativas y características de las películas.
- El mejor modelo depende del equilibrio entre relevancia, cobertura y costo computacional.

## Uso de Inteligencia Artificial

Se utilizó asistencia de IA para diagnosticar problemas de conectividad, resolver incompatibilidades entre NumPy y scikit-learn, y apoyar la documentación del proyecto.

## Reproducibilidad

Se recomienda conservar `pyproject.toml` y `uv.lock`, ejecutar las pruebas y documentar los parámetros y resultados obtenidos.
