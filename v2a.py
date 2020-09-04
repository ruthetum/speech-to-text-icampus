import sys
import os
import moviepy
import moviepy.editor

# curPath = os.getcwd()
# print(curPath)
# os.chdir('gdrive/My Drive/Colab Notebooks/extract-script/testfile')
# curPath = os.getcwd()
# print(curPath)

video = moviepy.editor.VideoFileClip("./video/ssmovie.mp4")

audio = video.audio

audio.write_audiofile("./audio/ssmovie.wav")