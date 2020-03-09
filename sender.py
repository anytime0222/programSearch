from DBSetting import DBHelper as Db
import requests

db = Db()


programData = db.db_programListGetter()

todaysMenu = ''
for row in programData:
    print( '프로그램명 :', row['program_name'], '시작시간 :',row['program_start_time'],'종료시간:',row['program_end_time'])
    todaysMenu = ('프로그램명 :'+ row['program_name'] + '\n시작시간 :' + row['program_start_time'] + '\n종료시간:' + row['program_end_time'])


    print("--텔레그램 메신저 전송 시작--")

    teleurl = 'https://api.telegram.org/bot1105491661:AAEDkxKmYx9vzVP9ZA6JbtEejcrECqfnIIA/sendMessage'

    params = {'chat_id' : '1042377150', 'text' : todaysMenu}

    res = requests.get(teleurl,params=params)