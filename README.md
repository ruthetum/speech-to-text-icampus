# iCampus 강의 좀 편하게 들어보자

### iCampus에서 스크립트 추출하기
### Google Cloud Platform & Storage 사용해서 Speech to Text 구현
### 

## 🍃 배경
- **아이캠퍼스는 자막이 없다...**
- **자막이 없다보니 청각이 좋지 않거나, 소음이 있거나 이어폰이 고장난 경우 시청하기 어렵다**
- **강의에 잡음이 섞이는 경우 의존할만한 자료가 없다**
- **수업 중간에 과제나 시험이 공지되는 경우**
- **그래서 내가 직접 쓸려고 만든 STT 스크립트 추출기**

## 🍃 사전 준비
- **Google Cloud Platform에서 프로젝트 생성 및 키 저장(JSON)**
- **Speech to Text API 사용 신청**
- **Google Cloud Storage 생성**
- **Google Cloud SDK 설치**

- GCP STT API를 사용하지 않고 speech recognition 라이브러리를 사용할 경우 긴 영상의 스크립트를 추출할 수 없다.
- 금액의 경우 90분 강의 기준 약 1800원 정도의 비용이 발생한다. 하지만 프리티어를 사용하는 경우 프로모션 크레딧이 35만원 정도 주어지니 걱정할 필요 없다.
- 음성 추출 서비스인 다글로(https://daglo.ai/)의 경우 1시간 기준 7200원 정도 금액이 발생하니 정확도는 떨어져도 가성비면에서 쏠쏠하다.


## 🍃 사용 방법
### 1. Clone

<code>git clone http://github.com/ruthetum/ForNaWab.git</code>

### 2. 환경 설정
- 터미널을 키고 앞서 발급받은 Key 파일의 경로를 다음 명령어와 같이 입력한다.

<code>set GOOGLE_APPLICATION_CREDENTIALS="C:\Users\DELL\Desktop\Develop\fornawab-33fb30199582.json"</code>

- 가상 환경을 활성화한 후 필요한 라이브러리를 설치한다. (가상 환경 설치 명령어는 하단에 별도 첨부)

  - Google Cloud Storage : <code>pip install --upgrade google-cloud-storage</code>

  - STT API : <code>pip install google-cloud-speech</code>

  - 마이크/스테레오 믹스 시 사용 : <code>pip install pyaudio</code> or <code>pip install pipwin</code> <code>pipwin install pyaudio</code>
  
  - 오디오 추출 : <code>pip install moviepy</code>

  - 오디오 분할 : <code>pip install pydub</code>

  - 번역 : <code>pip install googletrans</code>

  - PDF 파일 저장 : <code>pip install fpdf</code>

- 설치가 완료되었으면 발급받은 Key 파일의 경로를 다음의 명령어로 등록한다.

<code>gcloud auth activate-service-account --key-file="C:\Users\DELL\Desktop\Develop\fornawab-33fb30199582.json"</code> 

### 3. 강의 동영상을 다운로드한다.

편하게 크롬 확장프로그램 iCampus downloader를 사용하여 강의를 다운 받는다.

![image](https://user-images.githubusercontent.com/59307414/92278898-2025b700-ef31-11ea-8610-d4f20b3091c1.png)

### 4. 다운받은 동영상을 video 폴더에 위치시킨다.

폴더가 없는 경우 first.py가 존재하는 디렉토리에 video 폴더를 생성하고 해당 폴더에 mp4파일(아이캠퍼스는 mp4파일)을 위치시킨다.

### 5. first.py에서 filename을 mp4파일의 이름으로 설정한 후 first.py를 실행한다.  <code>python first.py</code>

![image](https://user-images.githubusercontent.com/59307414/92283291-8e22ac00-ef3a-11ea-96bf-f925ab94812b.png)


### 6. splitedAudio 폴더에 생성된 9개의 wav 파일을 Google Cloud Storage에 업로드한다.

storage를 생성하고 mp4 파일과 같은 이름의 폴더를 생성한 후 해당 폴더에 9개의 wav 파일을 업로드한다.

![image](https://user-images.githubusercontent.com/59307414/92283573-228d0e80-ef3b-11ea-8e0e-0f2525b1f55d.png)

이후 stt.py 파일에서 아래의 드래그된 부분에 본인이 생성한 storage 이름으로 수정한다.

![image](https://user-images.githubusercontent.com/59307414/92283866-d0002200-ef3b-11ea-8858-bec2bccb5124.png)

### 7. second.py에서 filename을 mp4파일의 이름으로 설정하고 일반/국제어 강의에 따라 TYPE 변수의 값을 설정한다. 

![image](https://user-images.githubusercontent.com/59307414/92284010-1b1a3500-ef3c-11ea-9d74-0749583f84bd.png)

### 8. PDF용 폰트의 경로를 본인의 상황에 알맞게 수정해준 후 second.py를 실행한다. <code>python second.py</code>

![image](https://user-images.githubusercontent.com/59307414/92284690-7dc00080-ef3d-11ea-9373-5cc1a7942f5c.png)



### 9. txt 파일과 PDF 파일이 생성된다.

![image](https://user-images.githubusercontent.com/59307414/92284182-7cda9f00-ef3c-11ea-8011-d690de865dc2.png)

![image](https://user-images.githubusercontent.com/59307414/92284208-8d8b1500-ef3c-11ea-9285-cc93dd7b3b4b.png)

- 아! 물론 정확도는 좋지 않다.
- 스크립트에 너무 의존적이라면 부정적이겠지만 수업 교안과 함께 본 스크립트를 참고한다면 보다 긍정적인 효과를 야기할 것으로 예상된다.

## 🍃 생성 폴더 설명
- audio : wav 파일
- splitedAudio : 9분할 된 wav 파일
- ko-scripts / en-scripts : 한글/영어 스크립트 txt 파일
- pdf : PDF 파일

## 🍃 가상 환경
- **가상환경 설치**

<code>pip install virtualenv</code>

<code>pip install virtualenvwrapper-win</code>

- **가상환경 생성 및 활성화**

<code>virtualenv env</code>

<code>.\env\Scripts\activate</code>

- **가상 환경을 사용하는 이유**

같은 모듈을 사용한다고 하더라도 다른 버전을 필요로 한다거나, Python 프로그램을 실행하기 위한 최소한의 환경을 마련하고자 할 때 사용

