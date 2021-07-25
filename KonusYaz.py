# -- coding: utf-8 --

import sys

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")

import os
import datetime

import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
  print("\nLütfen Yazıya Dönüştürmek İstediğiniz Metni Yüksek Sesle Konuşun")
  audio = r.listen(source)
  voice = r.recognize_google(audio, language='tr-TR')
  now = datetime.datetime.now()
  time = now.strftime('(Tarih:  %X       Saat:  %x)')
  file2 = open("KonusYaz.txt","a",encoding="utf-8")
  file2.write("\n\n" + time + "\n\n" + voice + "\n")
  file2.close()

  with open("KonusYaz.txt", "r") as file:
     file.read()
     os.startfile("KonusYaz.txt")

