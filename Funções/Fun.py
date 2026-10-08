import os
import tempfile

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

import speech_recognition as sr
import google.generativeai as genai

from gtts import gTTS
import pygame

# =====================================
# CONFIGURAÇÃO
# =====================================

api_key = "SUA_API_KEY_AQUI"
modelo = genai.GenerativeModel("gemini-2.5-flash")

pygame.mixer.init()

# =====================================
# FALAR
# =====================================

def falar(texto):
    print("IA:", texto)

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    ) as temp:
        arquivo = temp.name

    tts = gTTS(
        text=texto,
        lang="pt-br"
    )

    tts.save(arquivo)

    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()

    try:
        os.remove(arquivo)
    except:
        pass

# =====================================
# OUVIR
# =====================================

def ouvir():

    arquivo = "audio.wav"

    fs = 44100
    duracao = 5

    print("Fale agora...")

    audio = sd.rec(
        int(duracao * fs),
        samplerate=fs,
        channels=1,
        dtype=np.int16  # IMPORTANTE
    )

    sd.wait()

    write(
        arquivo,
        fs,
        audio
    )

    recognizer = sr.Recognizer()

    try:

        with sr.AudioFile(arquivo) as source:
            audio_data = recognizer.record(source)

        texto = recognizer.recognize_google(
            audio_data,
            language="pt-BR"
        )

        print("Você:", texto)

        return texto

    except Exception as erro:

        print("Erro:", erro)

        return None

# =====================================
# IA
# =====================================

def responder(pergunta):

    try:

        resposta = modelo.generate_content(
            pergunta
        )

        return resposta.text

    except Exception as erro:

        print("Erro Gemini:", erro)

        return "Ocorreu um erro ao gerar a resposta."

# =====================================
# INÍCIO
# =====================================

falar("Olá. Como posso ajudar?")

while True:

    comando = ouvir()

    if not comando:
        continue

    if comando.lower() in [
        "sair",
        "encerrar",
        "desligar"
    ]:

        falar("Até logo.")
        break

    resposta = responder(comando)

    falar(resposta)