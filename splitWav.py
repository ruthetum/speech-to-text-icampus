from pydub import AudioSegment
sound = AudioSegment.from_wav("./audio/test-audio.wav")

print(len(sound))
# split_point = len(sound) // 9

# for i in range(0,9):
#     part = sound[i*split_point:(i+1)*split_point]
#     part.export("./splitedAudio/test-audio/part" + str(i+1) + ".wav", format="wav")
