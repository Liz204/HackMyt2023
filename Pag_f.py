import streamlit as st
import openai

# Configuración de OpenAI
openai.api_key = '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'

def obtener_info_medicamento(medicamento):
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Proporciona información sobre el medicamento {medicamento}.",
        max_tokens=150
    )
    return respuesta.choices[0].text.strip()

def main():
    st.image("Logg.png", use_column_width=False, width=300)
    st.title('SmartPill')

    if 'medicamentos' not in st.session_state:
        st.session_state.medicamentos = []

    container1 = st.container()
    container2 = st.container()

    with container1:
        if 'finalizar' not in st.session_state or not st.session_state.finalizar:
            col1, col2 = st.columns(2)
            with col1:
                medicamento = st.text_input("Medicamento:", key=str(st.session_state.get('input_key', '')))
            with col2:
                siguiente = st.button("Siguiente")
                finalizar = st.button("Finalizar")

            if medicamento and siguiente:
                frecuencia = st.radio(
                    "Selecciona la frecuencia con la que tomarás el medicamento:",
                    ("c/d 8", "c/d 12", "c/d 24")
                )

            if siguiente and medicamento:  
                if medicamento not in st.session_state.medicamentos:
                    st.session_state.medicamentos.append(medicamento)
                    st.success(f"Medicamento '{medicamento}' añadido.")
                else:
                    st.warning(f"El medicamento '{medicamento}' ya fue añadido.")
                st.session_state['input_key'] = str(hash(medicamento))

            if finalizar:
                container1.empty()
                st.session_state['finalizar'] = True

    with container2:
        if 'finalizar' in st.session_state and st.session_state.finalizar:
            medicamento_seleccionado = st.selectbox(
                "Elige un medicamento para obtener información:", st.session_state.medicamentos)
            col1, col2 = st.columns(2)
            with col1:
                actualizar = st.button("Actualizar")
            with col2:
                eliminar = st.button("Eliminar")

            if actualizar:
                st.session_state['mostrar_dialogo'] = True

            if 'mostrar_dialogo' in st.session_state and st.session_state.mostrar_dialogo:
                st.write("¿Seguro que deseas continuar? Se perderán todos los datos.")
                if st.button("Aceptar"):
                    container1.empty()
                    container2.empty()
                    st.session_state['finalizar'] = False
                    st.session_state['medicamentos'] = []
                    st.session_state['mostrar_dialogo'] = False
                if st.button("Cancelar"):
                    st.session_state['mostrar_dialogo'] = False

            if eliminar:
                container1.empty()
                container2.empty()
                st.session_state['finalizar'] = False
                st.session_state['medicamentos'] = []

            if medicamento_seleccionado:
                info = obtener_info_medicamento(medicamento_seleccionado)
                st.write(info)

    st.subheader("Cuentale a nuestra IA tus dudas con tus medicamentos:")
    st.write("¡Hola! 👋 Bienvenidos a nuestro asistente virtual.")
    pregunta = st.text_input("¿Qué te gustaría saber?", key='pregunta')

    if st.button("Preguntar a la IA"):
        respuesta = obtener_info_medicamento(pregunta)
        st.write(f"Respuesta: {respuesta}")

    st.write(
        """
        En este link se pueden hacer donacioes para apoyar
        al desarrollo del producto :)
             
            """)
    st.image("QRRR.png", use_column_width=False, width=300)

     # Pie de página
    st.markdown("---")  
    st.markdown(
        """
        SmartPill
        German Andres Magallon Corona
        Vicente Ivan Ruiz Garcia
        Lizette Cruz Rodriguez
        Leobardo Mora Castillo
        """
    )

if __name__ == "__main__":
    main()
