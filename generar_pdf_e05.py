import sys
import subprocess

def install_fpdf():
    try:
        import fpdf
    except ImportError:
        print("Instalando fpdf2...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf2"])

install_fpdf()
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 10, 'INF-8239 Ciencia de Datos II - Ejercicio 05', align='C', new_x="LMARGIN", new_y="NEXT")
        self.set_font('Helvetica', 'I', 11)
        self.cell(0, 8, 'Motor Recomendador Reproducible', align='C', new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}/{{nb}}', align='C')

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 8, title, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def chapter_body(self, text):
        self.set_font('Helvetica', '', 11)
        self.multi_cell(0, 6, text)
        self.ln(4)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font('Helvetica', 'B', 11)
pdf.cell(0, 6, 'Estudiante: Kendy Baez Santos', new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 6, 'Repositorio: https://github.com/kendyb18-dotcom/INF8239_U03_Recomendadores_Proyecto_Base_uv.git', new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

pdf.chapter_title('1. Datos, Auditoria y Corte Temporal')
pdf.chapter_body(
    "Se utilizo el dataset MovieLens Latest Small, respetando su licencia de uso (sin redistribuir "
    "los archivos directamente). Los datos fueron obtenidos superando las restricciones de red "
    "(Zscaler). Se verifico la integridad mediante el hash SHA-256. El corte temporal se realizo "
    "ocultando la ultima valoracion de cada usuario elegible para separar entrenamiento (pasado) "
    "de evaluacion (futuro)."
)

pdf.chapter_title('2. Popularidad, Contenido y Factorizacion')
pdf.chapter_body(
    "Se implemento un baseline de popularidad suavizada (por cantidad y media) para resolver el cold start. "
    "Ademas, se utilizo similitud coseno sobre vectores TF-IDF de los generos para el filtrado por contenido. "
    "La factorizacion de matrices redujo el error predictivo (RMSE), pero esto no garantizo un buen "
    "ordenamiento (ranking)."
)

pdf.chapter_title('3. Ranking, Cobertura y Usuarios Frios')
pdf.chapter_body(
    "Se uso HitRate@10 para evaluar el ranking. Se observo un trade-off entre acierto y cobertura: "
    "mayor precision en el ranking tendio a reducir el catalogo explorado. Para los usuarios frios, la senal "
    "colaborativa es nula, por lo que se aplico el fallback devolviendo recomendaciones basadas en popularidad."
)

pdf.chapter_title('4. Modelo Hibrido y Decision Pareto (Green AI)')
pdf.chapter_body(
    "Se combino la puntuacion colaborativa con la senal de contenido:\n"
    "- Alpha 0.75 (Colaborativo dominante): HitRate 3.74%, Cobertura 7.75%, Tiempo ~13.8s.\n"
    "- Alpha 0.25 (Contenido dominante): HitRate 3.23%, Cobertura 10.64%, Tiempo ~14.3s.\n\n"
    "Se selecciono Alpha 0.75 por maximizar la precision. En Pareto, se descarto el modelo de 10 factores: "
    "el ahorro fue de ~0.3s pero con perdida real de utilidad. El modelo elegido usa 20 factores."
)

pdf.chapter_title('5. Declaracion de Uso de Herramientas de IA')
pdf.chapter_body(
    "Asistencia de IA utilizada para:\n"
    "1. Diagnostico del bloqueo de red (Zscaler) durante descargas de archivos y resolucion mediante hotspot.\n"
    "2. Resolucion del error 'TypeError: np.matrix is not supported' actualizando lab09_hybrid.py a np.asarray.\n"
    
)

output_file = 'U03_E05_KendyBaez.pdf'
pdf.output(output_file)
print(f"PDF generado: {output_file}")