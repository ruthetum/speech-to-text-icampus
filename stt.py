def audio_recognize(storage_uri, filename, TYPE, index):
    from google.cloud import speech_v1
    from google.cloud.speech_v1 import enums

    client = speech_v1.SpeechClient()

    # 인코딩한 hertz 따라 값 변경
    # wav 파일은 따로 sample rate 지정 안 해줘도 config에서 알아서 설정
    # sample_rate_hertz = 44100
    
    if TYPE == 1:
        language_code = "ko-KR"
    else:
        language_code = "en-US"
    # language_code = "en-IN" #india
    
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
        alternative = result.alternatives[0]
        # print(u"Transcript: {}".format(alternative.transcript))
        script = script + alternative.transcript + "\n"
    
    if TYPE == 1:
        with open("./ko-scripts/"+ str(filename) +"/script.txt", "a") as sc:
                sc.write(script)
    else:
        with open("./en-scripts/"+ str(filename) +"/script.txt", "a") as sc:
                sc.write(script)

def s2t(filename, TYPE):
    if TYPE == 1:
        f = open("./ko-scripts/"+ str(filename) +"/script.txt", 'w')
    else:
        f = open("./en-scripts/"+ str(filename) +"/script.txt", 'w')
    f.close()
    
    for i in range(1,10):
        audio_recognize("gs://fornawab/"+ str(filename) +"/part" + str(i) +".wav", filename, TYPE, i*10)
