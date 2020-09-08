def audio_recognize(storage_uri, fileName, TYPE, index):
    import os
    from google.cloud import speech_v1
    from google.cloud.speech_v1 import enums

    credential_path = "C:/Users/DELL/Desktop/Develop/fornawab-33fb30199582.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

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
        with open("./ko-scripts/"+ str(fileName) +"/script.txt", "a") as sc:
                sc.write(script)
    else:
        with open("./en-scripts/"+ str(fileName) +"/script.txt", "a") as sc:
                sc.write(script)

def s2t(fileName, TYPE):
    import os
    try:
        if not(os.path.isdir("./en-scripts/"+ str(fileName))):
            os.makedirs(os.path.join("./en-scripts/"+ str(fileName)))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory.")
            raise
    try:
        if not(os.path.isdir("./ko-scripts/"+ str(fileName))):
            os.makedirs(os.path.join("./ko-scripts/"+ str(fileName)))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory.")
            raise

    if TYPE == 1:
        f = open("./ko-scripts/"+ str(fileName) +"/script.txt", 'w')
    else:
        f = open("./en-scripts/"+ str(fileName) +"/script.txt", 'w')
    f.close()
    
    for i in range(1,10):
        audio_recognize("gs://fornawab/"+ str(fileName) +"/part" + str(i) +".wav", fileName, TYPE, i*10)