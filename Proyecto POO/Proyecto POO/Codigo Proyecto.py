from tkinter import *
from tkinter import messagebox
import os
from PIL import ImageTk, Image

# Defino las rutas 
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "imagen")
carpeta_fondo = os.path.join(carpeta_imagenes, "fondo")

# Diccionario y variables de autenticación
codigo_a_nombre = {
    "123456789": "Mendoza Callata Alejandro Sebastián",
    "987654321": "Vallejos Perez Felix Marcelo Jesus",
    "456789123": "Ramos Manrique Yamile",
    "321654987": "Ayala Hernandez Gerardo"
}

contrasenas_correctas = {
    "123456789": "AlianzaLima",
    "987654321": "Grone1901",
    "456789123": "Yamile",
    "321654987": "Gerardo"
}

# Defino la función evaluar
def evaluar():
    codigo = codigo_entry.get().strip()
    contrasena = contrasena_entry.get().strip()

    if not codigo or not contrasena:
        messagebox.showerror("Error", "Por favor ingrese su código y contraseña.")
        return

    nombre = codigo_a_nombre.get(codigo)
    contrasena_correcta = contrasenas_correctas.get(codigo)

    if not nombre:
        messagebox.showerror("Error", "Código incorrecto. Por favor intente de nuevo.")
        return

    if contrasena != contrasena_correcta:
        messagebox.showerror("Error", "Contraseña incorrecta. Por favor intente de nuevo.")
        return

    total_puntos = sum(respuesta.get() for respuesta in respuestas)
    max_puntos = 80  
    promedio = 40  

    recomendaciones = []

    if total_puntos <= promedio / 2:
        nivel_mental = "Muy bajo"
        recomendaciones.extend([
            "- Establece una rutina de sueño regular y ejercicios de relajación para reducir el estrés.",
            "- Considera hablar con un profesional para explorar tus emociones más profundas.",
            "- Participa en actividades que fomenten la introspección y el autoconocimiento, como la meditación o el yoga.",
            "- Revisa tus expectativas y metas personales para evitar sentirte abrumado/a."
        ])
        mensaje_motivacional = "Es importante que busques apoyo y tomes medidas concretas para mejorar tu bienestar emocional. Tómate el tiempo necesario para cuidarte y hacer actividades que te hagan sentir mejor. Recuerda que no estás solo/a."

    elif total_puntos <= promedio:
        nivel_mental = "Bajo"
        recomendaciones.extend([
            "- Establece una rutina de sueño regular y asegúrate de descansar lo suficiente cada noche.",
            "- Considera hablar con una persona de confianza sobre tus preocupaciones.",
            "- Dedica tiempo a actividades que te relajen y te ayuden a desconectar del estrés diario.",
            "- Organiza tus responsabilidades académicas de manera que te permitan tener tiempo libre para ti."
        ])
        mensaje_motivacional = "Recuerda que es normal sentirse abrumado/a en momentos de alta carga académica. Mantén una actitud positiva y busca pequeñas maneras de relajarte y encontrar equilibrio en tu día a día."

    elif total_puntos <= promedio * 1.5:
        nivel_mental = "Regular"
        recomendaciones.extend([
            "- Establece una rutina de sueño regular para mejorar tu descanso y rendimiento académico.",
            "- Busca actividades recreativas que te motiven y te permitan disfrutar de tu tiempo libre.",
            "- Habla con una persona de confianza sobre cómo te sientes.",
            "- Identifica tus fortalezas y utilízalas para superar los desafíos académicos."
        ])
        mensaje_motivacional = "Cada día es una nueva oportunidad para mejorar tu bienestar emocional. Aprovecha tus recursos y habilidades para enfrentar cualquier desafío con confianza."

    else:
        nivel_mental = "Alto"
        recomendaciones.extend([
            "- Continúa cuidando tu bienestar emocional y físico.",
            "- Establece metas desafiantes pero alcanzables para mantenerte motivado/a.",
            "- Comparte tus éxitos y logros con amigos y familiares para reforzar tu autoestima.",
            "- Considera explorar nuevas áreas de interés y crecimiento personal."
        ])
        mensaje_motivacional = "Es excelente ver que estás cuidando tu bienestar emocional. Continúa manteniendo una actitud positiva y busca oportunidades para crecer y aprender."

    mensaje_recomendaciones = "\n".join(recomendaciones)
    messagebox.showinfo("Resultado", f"Nombre: {nombre}\n\nTu puntaje total es: {total_puntos} de {max_puntos}\n\nTu estado mental ha sido evaluado como {nivel_mental}\n\nRecomendaciones:\n{mensaje_recomendaciones}\n\n{mensaje_motivacional}")

# Configuro la ventana principal de Tkinter
root = Tk()
root.title("Evaluación del Estado Mental del Estudiante Universitario")

ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
root.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

# Configuro el icono y la imagen de fondo
icon_path = os.path.join(carpeta_imagenes, "LOGO.ico")
fondo_path = os.path.join(carpeta_fondo, "UNAC1.png")

# Mensaje de depuración para verificar las rutas
print(f"Ruta del icono: {icon_path}")
print(f"Ruta de la imagen de fondo: {fondo_path}")

if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    messagebox.showwarning("Advertencia", f"No se encontró el ícono en la ruta: {icon_path}")

if os.path.exists(fondo_path):
    imagen_fondo = Image.open(fondo_path)
    imagen_fondo = imagen_fondo.resize((ancho_pantalla, alto_pantalla), Image.LANCZOS)
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
    fondo_label = Label(root, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    messagebox.showwarning("Advertencia", f"No se encontró la imagen de fondo en la ruta: {fondo_path}")

# Defino las preguntas y variables de respuestas
preguntas = [
    "¿Te sientes satisfecho/a con tus relaciones sociales?",
    "Te sientes apoyado/a por tu familia y amigos?",
    "¿Sientes que eres valorado/a por tus compañeros y profesores?",
    "¿Disfrutas de tu tiempo en la universidad?",
    "¿Encuentras tiempo para tus hobbies o intereses personales?",
    "¿Con qué frecuencia participas en actividades que te apasionan?",
    "¿Con qué frecuencia sientes que tienes suficiente energía para tus actividades diarias?",
    "¿Te resulta fácil concentrarte en tus estudios?",
    "¿Sientes que tu mente está clara y enfocada durante el estudio?",
    "¿Te sientes satisfecho/a con tus logros académicos?",
    "¿Te sientes optimista sobre tu futuro?",
    "¿Te preocupas por tu futuro profesional?",
    "¿Te tomas tiempo para cuidar tu salud física?",
    "¿Te sientes motivado/a para alcanzar tus metas?",
    "¿Te tomas tiempo para relajarte y descansar?",
    "¿Sientes que puedes manejar el estrés de manera efectiva?",
]

respuestas = []

# Configuro el estilo de la interfaz
bg_color = "alice blue"
fg_color = "black"
font_label = ("Helvetica", 12)
font_title = ("Helvetica", 16, "bold")
font_button = ("Helvetica", 12, "bold")

# Creo el título que tendrá la ventana
title = Label(root, text="Evaluación del Estado Mental del Estudiante Universitario", font=font_title, bg=bg_color)
title.pack(pady=(20, 10))

# Creo los campos de entrada para el código y la contraseña
frame_codigo = Frame(root, bg=bg_color)
frame_codigo.pack()
label_codigo = Label(frame_codigo, text="Código:", font=font_label, bg=bg_color, fg=fg_color)
label_codigo.pack(side="left", padx=(20, 10))
codigo_entry = Entry(frame_codigo, font=font_label)
codigo_entry.pack(side="left", padx=10)

frame_contrasena = Frame(root, bg=bg_color)
frame_contrasena.pack()
label_contrasena = Label(frame_contrasena, text="Contraseña:", font=font_label, bg=bg_color, fg=fg_color)
label_contrasena.pack(side="left", padx=(20, 10))
contrasena_entry = Entry(frame_contrasena, font=font_label, show="*")
contrasena_entry.pack(side="left", padx=10)

# Creo las instrucciones y preguntas
instrucciones = Label(root, text="Responde las siguientes preguntas del 1 al 5, donde 1 es 'NUNCA', 2 es 'CASI NUNCA', 3 es 'REGULAR', 4 es 'CASI SIEMPRE' y 5 es 'SIEMPRE' :", font=font_label, bg=bg_color, fg=fg_color)
instrucciones.pack(pady=10)

for pregunta in preguntas:
    frame = Frame(root, bg=bg_color)
    frame.pack()

    label = Label(frame, text=pregunta, font=font_label, bg=bg_color, fg=fg_color, wraplength=ancho_pantalla-100, justify="left")
    label.pack(side="left", padx=(20, 10), pady=5)

    variable = IntVar(value=1)  
    respuestas.append(variable)

    for valor in range(1, 6):
        rb = Radiobutton(frame, text=str(valor), variable=variable, value=valor, font=font_label, bg=bg_color, fg=fg_color)
        rb.pack(side="left", padx=5)

# Creo el botón de evaluación
boton = Button(root, text="Evaluar", command=evaluar, font=font_button, bg="RoyalBlue1", fg="white")
boton.pack(pady=20)   

root.mainloop()
