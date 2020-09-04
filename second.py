import stt
from stt import s2t
from translate import translateScript
from txt2pdf import t2p

def main():

    # Video 파일명 입력 Ex. sample.mp4
    filename = "sample"

    # 일반 강의 : 1 / 국제어 강의 : 2
    TYPE = 2

    # Speech to Text
    s2t(filename, TYPE)

    # Translate
    if TYPE == 2:
        translateScript(filename)

    # Textfile to PDF
    t2p(filename)