# from google.cloud import translate_v2 as translate
# translate_client = translate.Client()

# if isinstance(text, six.binary_type):
#     text = text.decode('utf-8')

# result = translate_client.translate(
#     text, target_language=target)

# print(u'Text: {}'.format(result['input']))
# print(u'Translation: {}'.format(result['translatedText']))
# print(u'Detected source language: {}'.format(
#     result['detectedSourceLanguage']))

import re
from googletrans import Translator

translator = Translator()

f = open("./ko-scripts/test-audio/script.txt", 'w')
f.close()

with open ("./en-scripts/test-audio/script.txt", "r", -1, "utf-8") as readFile:
    data = readFile.readlines()
    print("Waiting for translation...")
    for d in data:
        sentence = d.replace("\n", "")
        with open("./ko-scripts/test-audio/script.txt", "a", -1, "utf-8") as writeFile:
            result = translator.translate(sentence, dest="ko")
            writeFile.write(result.text + "\n")
            print(result.text)