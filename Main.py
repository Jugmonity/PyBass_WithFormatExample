import PyBass.bass as bass
import os
import ctypes
import sys
from time import sleep
class UTF8_Convert:
    def Convert(text : str):
        return bytes("{}.mp3".format(text), "utf-8")
def Main():
    bass.BASS_INIT(device=-1, freq=44800, flags=0, win=0, dsguid=0)
    bass.BASS_START()
    stream = bass.BASS_StreamCreateFile(mem=0, filename=UTF8_Convert.Convert("AstralStep"), offset=0, length=0, flags=0x4)
    bass.BASS_ChannelPlay(stream, False)
    while True:
        sleep(5000)

if __name__ == "__main__":
    Main()