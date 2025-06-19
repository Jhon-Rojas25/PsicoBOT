
import streamlit as st
import time

# Título de la aplicación
st.set_page_config(page_title="DocenteZen - Apoyo Emocional", layout="centered")
st.title("🤖 DocenteZen - Tu Asistente Emocional 24/7")
st.markdown("""
Este chatbot ha sido creado para ofrecer apoyo emocional a los docentes de la UNMSM. Puedes expresarte libremente. Tu bienestar importa. 💙
""")

# Menú de opciones
opcion = st.selectbox("¿Cómo te gustaría comenzar hoy?", [
    "Selecciona una opción",
    "Hablar sobre cómo me siento",
    "Hacer un test rápido de estrés",
    "Recibir un consejo o ejercicio",
    "Solicitar ayuda profesional"
])

# Opciones del chatbot
if opcion == "Hablar sobre cómo me siento":
    emocion = st.text_input("¿Podrías describir cómo te sientes con una palabra?")
    if emocion:
        st.write(f"Gracias por compartirlo. Sentirse **{emocion}** es completamente válido.")
        st.write("¿Te gustaría realizar un ejercicio breve de respiración o recibir una frase de apoyo?")
        accion = st.radio("Elige una opción:", ["Ejercicio de respiración", "Frase de apoyo emocional"])

        if accion == "Ejercicio de respiración":
            st.write("🧘 Iniciando respiración guiada 4-7-8...")
            with st.spinner('Inhala profundamente (4s)...'):
                time.sleep(4)
            with st.spinner('Sostén el aire (7s)...'):
                time.sleep(7)
            with st.spinner('Exhala lentamente (8s)...'):
                time.sleep(8)
            st.success("Respiración completada. ¿Cómo te sientes ahora?")

        elif accion == "Frase de apoyo emocional":
            frases = [
                "Estás haciendo lo mejor que puedes. Y eso es suficiente.",
                "Respira. No tienes que hacerlo todo hoy.",
                "Tu bienestar es tan importante como tu trabajo.",
                "Eres valioso, incluso cuando estás cansado."
            ]
            st.success(frases[time.time_ns() % len(frases)])

elif opcion == "Hacer un test rápido de estrés":
    st.subheader("🧠 Test de Estrés (PSS modificado)")
    preguntas = [
        "¿Con qué frecuencia te has sentido nervioso o estresado en los últimos días?",
        "¿Con qué frecuencia has sentido que no podías controlar las cosas importantes de tu vida?",
        "¿Con qué frecuencia te has sentido abrumado por tus responsabilidades?",
        "¿Con qué frecuencia te has sentido que no podías afrontar todas las tareas del día?"
    ]
    puntuacion = 0
    opciones = {"Nunca": 0, "A veces": 1, "Frecuentemente": 2, "Siempre": 3}

    for p in preguntas:
        respuesta = st.radio(p, list(opciones.keys()), key=p)
        puntuacion += opciones[respuesta]

    if st.button("Evaluar nivel de estrés"):
        if puntuacion <= 3:
            st.success("Nivel de estrés bajo. ¡Sigue cuidando de ti mismo! 🌿")
        elif puntuacion <= 6:
            st.warning("Nivel de estrés moderado. Considera tomar pausas y ejercicios de autocuidado.")
        else:
            st.error("Alto nivel de estrés. Te sugerimos hablar con un profesional o realizar ejercicios guiados.")

elif opcion == "Recibir un consejo o ejercicio":
    st.write("✨ Aquí tienes una sugerencia para reducir el estrés:")
    consejos = [
        "Haz una pausa de 5 minutos y respira profundamente.",
        "Toma agua y da un pequeño paseo.",
        "Escribe 3 cosas por las que estás agradecido hoy.",
        "Escucha tu canción favorita y desconéctate por un momento."
    ]
    st.info(consejos[time.time_ns() % len(consejos)])

elif opcion == "Solicitar ayuda profesional":
    st.warning("📞 Si sientes que necesitas hablar con alguien, considera contactar al servicio psicológico de UNMSM o al 113 opción 5.")
    st.write("Puedes visitar el centro de apoyo psicológico de la universidad o contactar con un profesional certificado.")

st.markdown("---")
st.caption("Chatbot creado para fines educativos y de bienestar emocional. No reemplaza atención psicológica profesional en casos graves.")
