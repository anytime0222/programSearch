from selenium import webdriver
from DBSetting import DBHelper as Db

from programList import programs

#프로그램 사이트 확인 (일단 cntv 먼저 확인)
main_url = 'http://www.cntv.co.kr/index.php?mid=CN_TVguide'
channel_name = 'CNTV'

#프로그램 정보 담는 프로그램 리스트
program_lists = []

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
    print('---------------------------------------------------')

    #출력된 데이터를 리스트에 삽입

    obj = programs(
        li.find_element_by_css_selector('.program').text,
        li.find_element_by_css_selector('.airTime').text,
        li.find_element_by_css_selector('.runningTime').text,
        channel_name
    )
    program_lists.append(obj)


#db에 프로그램 리스트 입력
    db.db_insertCrawlingData(obj.program_name, obj.program_start_time, obj.program_end_time, obj.program_channel)

#프로그램 
print( program_lists , len(program_lists))

driver.close()
driver.quit()
import sys
sys.exit()