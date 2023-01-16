import speech_recognition as sr
sr.__version__
r=sr.Recognizaer()

salu2 = sr.AudioFile('saludos.wav')
with salu2 as source:
    audio=r.record(source)