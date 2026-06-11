from datetime import datetime
import os

def generar_entrada_blog(titulo, categoria, contenido_texto):
    # 1. Obtener la fecha actual en los formatos que Jekyll necesita
    fecha_hoy = datetime.now().strftime("%Y-%m-%d") # Ej: 2026-06-11
    fecha_completa = datetime.now().strftime("%Y-%m-%d %H:%M:%S -0600")
    
    # 2. Convertir el título en formato de archivo (Minúsculas y con guiones)
    # Ejemplo: "Mi Post Increíble" -> "mi-post-increible"
    titulo_limpio = titulo.lower().replace(" ", "-")
    nombre_archivo = f"{fecha_hoy}-{titulo_limpio}.md"
    ruta_final = f"_posts/{nombre_archivo}"
    
    # 3. Validar si la carpeta _posts existe por seguridad
    if not os.path.exists("_posts"):
        print("Error: No se encontró la carpeta _posts. Asegúrate de ejecutar el script en la raíz de tu blog.")
        return

    # 4. Estructura Front Matter (YAML) + Contenido
    plantilla_markdown = f"""---
title: "{titulo}"
date: {fecha_completa}
categories: [General, {categoria}]
tags: [Automatizado]
---

{contenido_texto}
"""

    # 5. Escribir el archivo en el disco duro
    with open(ruta_final, "w", encoding="utf-8") as archivo:
        archivo.write(plantilla_markdown)
        
    print(f"🚀 ¡Éxito! Post creado en: {ruta_final}")

# ==========================================
# 🎯 PRUEBA DE LA MÁQUINA: Escribe aquí tu contenido
# ==========================================
mi_titulo = "Entrada creada desde Python"
mi_categoria = "Programación"
mi_contenido = """¡Hola! Este es un experimento genial. 
Acabo de crear este post ejecutando un script de Python que genera el archivo Markdown automáticamente.

Pronto seré un estudiante de Ingeniería en Tecnologías de la Información e Innovación Digital y esto es solo el comienzo."""

# Llamamos a la función
generar_entrada_blog(mi_titulo, mi_categoria, mi_contenido)