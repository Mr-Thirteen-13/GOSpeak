#~!~#
#python 3.7.X

from gtts import gTTS

print ("""
          ###############################
              GOOGLE VOICE DOWNLOADER
                Author : Bastian Saputra
          ###############################
""")

speak = input("Type something > ")
output = input("\nEx : example.mp3\nOutput audio save > ")
audio = gTTS(speak)
audio.save(output)
print("Saved " + output)
