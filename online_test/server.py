import random

import pandas as pd
from flask import Flask, render_template, request, Response
import datetime
from flask import send_file


app = Flask(__name__)

print(__name__)


@app.route('/')
def index():
     return render_template('Online_Test_html.html')


@app.route('/complete', methods =['POST'])
def button_Complete():


     name = request.form.get('name')

     # True or False radio buttons
     radio_1 = int(request.form.get('rd_1'))
     radio_2 = int(request.form.get('rd_2'))
     radio_3 = int(request.form.get('rd_3'))
     radio_4 = int(request.form.get('rd_4'))
     radio_5 = int(request.form.get('rd_5'))
     radio_6 = int(request.form.get('rd_6'))
     radio_7 = int(request.form.get('rd_7'))
     radio_8 = int(request.form.get('rd_8'))
     radio_9 = int(request.form.get('rd_9'))
     radio_10 = int(request.form.get('rd_10'))
     if radio_1 == 1:
         rd1 = "True"
         rs01 = "O"
     else:
         rd1 = "False"
         rs01 = "X"
     if radio_2 == 1:
         rd2 = "True"
         rs02 = "O"
     else:
         rd2 = "False"
         rs02 = "X"
     if radio_3 == 1:
         rd3 = "True"
         rs03 = "O"
     else:
         rd3 = "False"
         rs03 = "X"
     if radio_4 == 1:
         rd4 = "True"
         rs04 = "O"
     else:
         rd4 = "False"
         rs04 = "X"
     if radio_5 == 1:
         rd5 = "True"
         rs05 = "O"
     else:
         rd5 = "False"
         rs05 = "X"
     if radio_6 == 1:
         rd6 = "True"
         rs06 = "O"
     else:
         rd6 = "False"
         rs06 = "X"
     if radio_7 == 1:
         rd7 = "True"
         rs07 = "O"
     else:
         rd7 = "False"
         rs07 = "X"
     if radio_8 == 1:
         rd8 = "True"
         rs08 = "O"
     else:
         rd8 = "False"
         rs08 = "X"
     if radio_9 == 1:
         rd9 = "True"
         rs09 = "O"
     else:
         rd9 = "False"
         rs09 = "X"
     if radio_10 == 1:
         rd10 = "True"
         rs10 = "O"
     else:
         rd10 = "False"
         rs10 = "X"
         
         

     # multiple questions radio buttons
     mrv1 = str(request.form.get('rdm_1'))
     mrv2 = str(request.form.get('rdm_2'))
     mrv3 = str(request.form.get('rdm_3'))
     mrv4 = str(request.form.get('rdm_4'))
     mrv5 = str(request.form.get('rdm_5'))
     
     
     
     if mrv1 == 'header 태그':
         mradio_1 = 5
         rs11 = "O"
     else :
         mradio_1 = 0
         rs11 = "X"
     if mrv2 == 'alt':
         mradio_2 = 5
         rs12 = "O"
     else :
         mradio_2 = 0
         rs12 = "X"
     if mrv3 == '#':
         mradio_3 = 5
         rs13 = "O"
     else :
         mradio_3 = 0
         rs13 = "X"
     if mrv4 == 'option 태그':
         mradio_4 = 5
         rs14 = "O"
     else :
         mradio_4 = 0
         rs14 = "X"
     if mrv5 == 'head 태그':
         mradio_5 = 5
         rs15 = "O"
     else :
         mradio_5 = 0
         rs15 = "X"
      
     
     

     #Sentence Completion Question 1
     textN_1 = request.form.get('q1_t1')
     textN_2 = request.form.get('q1_t2')
     if textN_1 == '인라인' :
          textA_1 = 5
          rs16 = "O"
     else :
          textA_1 = 0
          rs16 = "X"

     if textN_2 == '블록' :
          textA_2 = 5
          rs17 = "O"
     else :
          textA_2 = 0
          rs17 = "X"

     # Sentence Completion Question 2
     textN_3 = request.form.get('q2_t1')
     textN_4 = request.form.get('q2_t2')
     textN_5 = request.form.get('q2_t3')
     textN_6 = request.form.get('q2_t4')
     if textN_3 == 'post' or 'POST':
          textA_3 = 5
          rs18 = "O"
     else :
          textA_3 = 0
          rs18 = "X"
     if textN_4 == 'text-align' :
          textA_4 = 5
          rs19 = "O"
     else :
          textA_4 = 0
          rs19 = "X"
     if textN_5 == '&nbsp' :
          textA_5 = 5
          rs20 = "O"
     else :
          textA_5 = 0
          rs20 = "X"
     if textN_6 == 'display' :
          textA_6 = 5
          rs21 = "O"
     else :
          textA_6 = 0
          rs21 = "X"

     # Total score
     # data 리스트에 USER가 입력한 정답들을 계산하여 percentage로 출력
     data = [radio_1, radio_2, radio_3, radio_4, radio_5, radio_6, radio_7, radio_8, radio_9, radio_10,
             mradio_1, mradio_2, mradio_3, mradio_4, mradio_5, textA_1, textA_2,textA_3,textA_4,textA_5,textA_6]
     result = sum(data)

     percent_score = int((result/65) *100)

     # HighChart에 들어가는 data list 생성 ( 1~65점 까지의 총 100명의 점수)
     # data에 당신의 점수 append
     # sort()를 통해서 정렬
     bell_data = []
     for i in range(0, 99):
         n = random.randint(1, 65)
         bell_data.append(n)

     bell_data.append(result)
     bell_data.sort()

     grade =''
     if percent_score >=90:
          grade = 'A'
     elif percent_score >= 80:
          grade = 'B'
     elif percent_score >=70:
          grade = 'C'
     else :
          grade = 'FAIL'

     #pandas를 통해 USER가 HTML에 입력한 값을 Excel data로 저장
     ans_sheet = pd.DataFrame(
          {'Answer': ['True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True', 'True',
                      'header태그','alt', '#', 'option태그','head태그','인라인','블록','post or POST','text-align','&nbsp','display','흭득한 점수', '등급'],
           
           
           'Your_Answer': [rd1, rd2, rd3, rd4, rd5, rd6, rd7, rd8, rd9, rd10,
                         mrv1, mrv2, mrv3, mrv4, mrv5, textN_1, textN_2,textN_3,textN_4,textN_5,textN_6, percent_score, grade],
           '정오표': [rs01, rs02, rs03, rs04, rs05, rs06, rs07, rs08, rs09, rs10, rs11, rs12, rs13, rs14, rs15, rs16, rs17, rs18, rs19, rs20, rs21, '', ''],
                         
                         
           '흭득 점수': [radio_1, radio_2, radio_3, radio_4, radio_5, radio_6, radio_7, radio_8, radio_9, radio_10,
                         mradio_1, mradio_2, mradio_3, mradio_4, mradio_5, textA_1, textA_2,textA_3,textA_4,textA_5,textA_6,'', '']
           
           })

     suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
     filename = "_".join([name, suffix, ".xlsx"])
     ans_sheet.to_excel(filename, index=False)

                     
     return render_template('score_board.html', resultHtml=result, dataHtml= percent_score, nameHtml=name, gradeHtml=grade, filenameHtml=filename) + render_template('bellcurve.html', bellHtml=bell_data)




     #return send_file(filename, mimetype='text/csv', attachment_filename='result.csv', as_attachment=True)
 #send_file(filename, mimetype='text/csv', attachment_filename = 'result.csv', as_attachment=True) # 이걸 연결만 하면 되는데..
    
#@app.route("/file_download")
#def hello():
#    return '''
#    <a href="/csv_file_download_with_file">Click me.</a>
#    
#    <form method="get" action="csv_file_download_with_file">
#        <button type="submit">Download!</button>
#    </form>
#    '''
# html 버튼을 그냥 코드로 리턴?



# @app.route('/csv_file_download_with_file')
# def csv_file_download_with_file():

#     return send_file(request.form.get(filenameHtml),
#                      mimetype='text/csv',
#                      attachment_filename='result.csv',# 다운받아지는 파일 이름. 
#                      as_attachment=True)



	









if __name__ == '__main__':
     app.debug = True
     app.run()