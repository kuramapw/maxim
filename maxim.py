import speech_recognition as sr

rec=sr.Recognizer()
micro = sr.Microphone()

with micro as source:
    while(s.lower()!="закрыть"):
        audio = rec.listen(source)
        try:
            s = rec.recognize_google(audio, language = "ru-RU")
            if s.lower() == "максим":
                print(s)
        except sr.RequestError as e:
            a="Плохое соединение с интернетом"
        except:
            a="Плохо распознается"
