from os import remove
from time import time

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment

from libs.utils.logger.src.customLogger import logger


def mp3_to_wav(mp3_file_path):
    audio = AudioSegment.from_mp3(mp3_file_path)
    remove(mp3_file_path)
    wav_file_path = mp3_file_path.replace('.mp3', '.wav')
    audio.export(wav_file_path, format='wav')
    logger.info(f'Converted {mp3_file_path} to {wav_file_path}')
    return wav_file_path


def convert_speech_to_text(audio_file):
    start_time = time()
    if not audio_file.endswith('.wav'):
        audio_file = mp3_to_wav(audio_file)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_whisper(audio)
    end_time = time()
    logger.info(
        f'  Successfully converted audio file to text in '
        f'{(end_time - start_time):.2f} seconds'
    )
    # remove(audio_file)
    return text


def generate_audio_file_from_text(text):
    tts = gTTS(text=text, lang='hi', timeout=20)
    mp3_file_path = 'tmp/audio_files/output.mp3'
    tts.save(mp3_file_path)
    print(f'Text has been converted to {mp3_file_path}')
    return mp3_file_path

def play_audio_file(audio_file_path):
    playsound(audio_file_path)

if __name__ == '__main__':
    voice_file_path = 'sample_audio_files/1-at-home-1.wav'
    print(convert_speech_to_text(voice_file_path))
    # play_('नमस्ते, आप कैसे हैं? मुझे उम्मीद है कि आप अच्छे होंगे। आज का दिन कैसा रहा?')
