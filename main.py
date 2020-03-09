from selenium import webdriver
from DBSetting import DBHelper as Db
import datetime

from programList import programs

#프로그램 사이트 확인 (일단 cntv 먼저 확인)
main_url = 'http://www.cntv.co.kr/index.php?mid=CN_TVguide'
channel_name = 'CNTV'

#프로그램 정보 담는 프로그램 리스트
program_lists = []
search_program_name_list = ['이산','김영철']

#db
db = Db()

#사이트 접근

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(main_url)

#프로그램 리스트 불러오기
programBox = driver.find_elements_by_css_selector('.scheduler>table>tbody>tr')

for li in programBox:

    print('프로그램명 :', li.find_element_by_css_selector('.program').text)
    print('시작시간 :', li.find_element_by_css_selector('.airTime').text)
    print('방송시간 :', li.find_element_by_css_selector('.runningTime').text)

    start_time = li.find_element_by_css_selector('.airTime').text
    running_time = li.find_element_by_css_selector('.runningTime').text

    a = start_time.split(':')[0]
    b = start_time.split(':')[1]

    change_time = datetime.datetime(100,1,1,int(a),int(b))

    sum_time = change_time + datetime.timedelta(minutes=int(running_time))

    sum_time_final = sum_time.time()
    sss = str(sum_time_final)
    sss1 = sss[:-3]
   
    #특정 검색어만 저장 되도록 설정
    for lists in search_program_name_list:
        print ('검색어 : ', lists)
        program_nm = li.find_element_by_css_selector('.program').text
        if lists in program_nm:

            #출력된 데이터를 리스트에 삽입
            obj = programs(
                li.find_element_by_css_selector('.program').text,
                start_time,
                sss1,
                channel_name
            )
            program_lists.append(obj)
            #db에 프로그램 리스트 입력

            db.db_insertCrawlingData(obj.program_name, obj.program_start_time, obj.program_end_time, obj.program_channel)
    
    print('---------------------------------------------------')



#프로그램 종료
print( program_lists , len(program_lists))

driver.close()
driver.quit()
import sys
sys.exit()