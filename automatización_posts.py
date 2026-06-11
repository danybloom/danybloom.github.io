from datetime import datetime
import os

def generar_entrada_blog(titulo, categoria, contenido_texto):
    # 1. Obtener la fecha actual en los formatos que Jekyll necesita
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    fecha_completa = datetime.now().strftime("%Y-%m-%d %H:%M:%S -0600")
    
    # 2. Convertir el título en formato de archivo
    titulo_limpio = titulo.lower().replace(" ", "-")
    nombre_archivo = f"{fecha_hoy}-{titulo_limpio}.md"
    ruta_final = f"_posts/{nombre_archivo}"
    
    # 3. Validar si la carpeta _posts existe
    if not os.path.exists("_posts"):
        print("Error: No se encontró la carpeta _posts.")
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

    # 5. Escribir el archivo final .md
    with open(ruta_final, "w", encoding="utf-8") as archivo:
        archivo.write(plantilla_markdown)
        
    print(f"🚀 ¡Éxito! Post creado en: {ruta_final}")


# ========================================================
# 🎯 NUEVA SECCIÓN: LEVANTAR ARCHIVO TEXTO
# ========================================================
print("=== CREADOR DE POSTS DESDE ARCHIVO LOCAL ===")

mi_titulo = input("✍️  Escribe el título de tu nuevo post: ")
mi_categoria = input("📁 Escribe la categoría: ")
nombre_nota = input("📄 Escribe el nombre de tu archivo (ej. nota.txt): ")

# Intentamos abrir el archivo que nos indicaste
try:
    with open(nombre_nota, "r", encoding="utf-8") as archivo_origen:
        # Leemos todo el bloc de notas completo y lo guardamos en la variable
        mi_contenido = archivo_origen.read()
    
    # Si todo sale bien, la función fabrica el post del blog
    generar_entrada_blog(mi_titulo, mi_categoria, mi_contenido)

except FileNotFoundError:
    print(f"❌ Error: No se encontró el archivo '{nombre_nota}'. Asegúrate de que esté en la misma carpeta que este script.")