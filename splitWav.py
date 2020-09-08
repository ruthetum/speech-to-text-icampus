def splitAudio(filename):
    import os
    from pydub import AudioSegment
    sound = AudioSegment.from_wav("./audio/"+ str(filename) +".wav")

    try:
        if not(os.path.isdir("./splitedAudio/"+ str(filename))):
            os.makedirs(os.path.join("./splitedAudio/"+ str(filename)))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory.")
            raise

    split_point = len(sound) // 9

    for i in range(0,9):
        part = sound[i*split_point:(i+1)*split_point]
        part.export("./splitedAudio/"+ str(filename) +"/part" + str(i+1) + ".wav", format="wav")
