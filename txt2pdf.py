from fpdf import FPDF 
   
# pdf 클래스 선언
pdf = FPDF()    
   
# 페이지 추가
pdf.add_page() 

# 폰트 추가
pdf.add_font('nsb', '', r"C:\Users\DELL\Desktop\ForNaWab\font\nsb.ttf", uni=True)

# pdf에 추가 
# 제목
pdf.set_font("nsb", size = 15) # 폰트, 크기 설정
pdf.cell(200, 10, txt = "Test Script", ln = 1, align = 'C')
pdf.cell(200, 10, txt = "", ln =2 , align='C')

# 텍스트 파일 열기
textFile = open("./ko-scripts/test-audio/script.txt", "r", encoding='UTF-8')

# 스크립트 내용
pdf.set_font("nsb", size = 12) # 폰트, 크기 설정
for t in textFile:
    itt = len(t) // 60
    for i in range(0, itt+1):
        if i == itt:
            pdf.cell(200, 10, txt = t[i*60:], ln = 3, align = 'L')
        else:
            pdf.cell(200, 10, txt = t[i*60:(i+1)*60], ln = 3, align = 'L')
   
# 저장
pdf.output("./pdf/test-audio/script.pdf")