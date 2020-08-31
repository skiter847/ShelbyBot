import speech_recognition as sr
import subprocess
import os


def ogg_to_wav(voice_path):
    try:
        os.remove('new_voice.wav')
    except FileNotFoundError:
        pass

    subprocess.run(['ffmpeg', '-i', voice_path, 'new_voice.wav'])


def voice_to_str(voice_path='downloads/voice.ogg'):
    ogg_to_wav(voice_path)
    r = sr.Recognizer()
    with sr.WavFile("new_voice.wav") as source:  # use "test.wav" as the audio source
        audio = r.record(source)
        try:
            return r.recognize_google(audio, language='ru')
        except:
            return 'Нихуя не понял, но было очень интересно.'


