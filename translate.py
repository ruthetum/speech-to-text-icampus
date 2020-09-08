def translateScript(fileName):
    import re
    from googletrans import Translator

    translator = Translator()

    f = open("./ko-scripts/"+ str(fileName) +"/script.txt", 'w')
    f.close()

    with open ("./en-scripts/"+ str(fileName) +"/script.txt", "r", -1, "utf-8") as readFile:
        data = readFile.readlines()
        print("Waiting for translation...")
        for d in data:
            sentence = d.replace("\n", "")
            with open("./ko-scripts/"+ str(fileName) +"/script.txt", "a", -1, "utf-8") as writeFile:
                result = translator.translate(sentence, dest="ko")
                writeFile.write(result.text + "\n")
                print(result.text)