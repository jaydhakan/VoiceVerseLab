import streamlit as st
from libs.utils.speechRecognition.helpers import (
    convert_speech_to_text,
    generate_audio_file_from_text
)


# TODO: Work in progress
def main():
    st.title('Voice Assistant')

    st.sidebar.title('Voice Assistant Options')
    st.sidebar.write(
        'Upload an audio file to convert speech to text or enter text to '
        'convert to speech.'
    )

    audio_file = st.sidebar.file_uploader(
        "Upload an audio file",
        type=["wav", "mp3"]
    )
    if audio_file:
        print('audio_file')
        st.sidebar.write("Processing audio file...")
        text = convert_speech_to_text(audio_file)
        st.sidebar.write("Text from audio:")
        st.sidebar.write(text)

    text_input = st.sidebar.text_area("Enter text to convert to speech")
    if st.sidebar.button("Convert to Speech"):
        if text_input:
            st.sidebar.write("Converting text to speech...")
            audio_file_path = generate_audio_file_from_text(text_input)
            st.sidebar.write("Playing the audio file...")
            st.audio(audio_file_path)
        else:
            st.sidebar.write("Please enter some text to convert to speech.")


if __name__ == '__main__':
    main()
