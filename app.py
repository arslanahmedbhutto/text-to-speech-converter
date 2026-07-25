import streamlit as st
import io
from gtts import gTTS

st.title("Text to Speech Converter")

st.write("Type text below and convert it into speech (audio).")

text = st.text_area("Enter your text here")

language = st.selectbox("Select language", ["en", "ur", "hi", "ar", "fr", "es"])

if st.button("Convert to Speech"):
    if text:
        tts = gTTS(text=text, lang=language)

        # Save audio to memory instead of a file on disk
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)

        st.subheader("Generated Audio")
        st.audio(audio_buffer, format="audio/mp3")

        st.download_button(
            label="Download Audio",
            data=audio_buffer,
            file_name="speech.mp3",
            mime="audio/mp3"
        )
    else:
        st.write("Please enter some text first.")




