import speech_recognition as sr
import subprocess
import os


def ogg_to_wav(voice_path: str) -> None:
    """ ogg file convert to wav, because google recognize work only with wav files """
    try:
        os.remove('new_voice.wav')
    except FileNotFoundError:
        pass

    subprocess.run(['ffmpeg', '-i', voice_path, 'new_voice.wav'])


def voice_to_str(voice_path='downloads/voice.ogg') -> str:
    """conver voice to str, return str"""
    ogg_to_wav(voice_path)
    r = sr.Recognizer()
    with sr.WavFile("new_voice.wav") as source:  # use "test.wav" as the audio source
        audio = r.record(source)
        try:
            return r.recognize_google(audio, language='ru')
        except:
            return 'Нихуя не понял, но было очень интересно.'
