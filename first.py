from video2audio import v2a
from splitWav import splitAudio

def main():

    # Video 파일명 입력 Ex. sample.mp4
    filename = "sample"

    # Video to Audio
    v2a(filename)

    # Split audio file
    splitAudio(filename)