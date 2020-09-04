from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

def audio_recognize(storage_uri, index):

    client = speech_v1.SpeechClient()

    # 인코딩한 hertz 따라 값 변경
    # sample_rate_hertz = 44100
    
    language_code = "en-US"
    # language_code = "en-IN"
    
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    # 오디오 채널 옵션은 영상에 따라 유무 선택
    config = {
        # "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        "encoding": encoding,
        "audio_channel_count" : 2,
    }
    audio = {"uri": storage_uri}

    print(u"[ "+ str(index) +"% ]Waiting for operation to complete...")

    operation = client.long_running_recognize(config, audio)
    response = operation.result()

    script = ""
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
        script = script + alternative.transcript + "\n"
    
    with open("./en-scripts/test-audio/script.txt", "a") as sc:
            sc.write(script)

def main():
    f = open("./en-scripts/test-audio/script.txt", 'w')
    f.close()
    for i in range(1,10):
        audio_recognize("gs://fornawab/test-audio/part" + str(i) +".wav", i*10)

main()
