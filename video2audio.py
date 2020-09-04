def v2a(filename):
    import sys
    import os
    import moviepy
    import moviepy.editor

    video = moviepy.editor.VideoFileClip("./video/"+ str(filename) +".mp4")

    audio = video.audio

    audio.write_audiofile("./audio/"+ str(filename) +".wav")