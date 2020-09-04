def splitAudio(filename):
    from pydub import AudioSegment
    sound = AudioSegment.from_wav("./audio/"+ str(filename) +".wav")

    split_point = len(sound) // 9

    for i in range(0,9):
        part = sound[i*split_point:(i+1)*split_point]
        part.export("./splitedAudio/"+ str(filename) +"/part" + str(i+1) + ".wav", format="wav")
