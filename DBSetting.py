#db 데이터 삽입

import pymysql

class DBHelper:
    '''
    멤버변수 : 커넥션
    '''
    conn = None

    '''
    생성자
    '''
    def __init__(self):
        self.db_init()
    '''
    멤버함수
    '''
    def db_init(self):
        self.conn = pymysql.connect(
                        host='localhost',
                        user='root',
                        password='1234',
                        db='program_saver',
                        charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor)
        
    def db_free(self):
        if self.conn:
            self.conn.close()

    def db_insertCrawlingData(self, program_name,program_start_time,program_end_time,program_channel):
        with self.conn.cursor() as cursor:
            sql = '''
            insert into  `program_list`
            (program_name,program_start_time,program_end_time,program_channel)
            values( %s,%s,%s,%s )
            '''
            cursor.execute(sql, (program_name,program_start_time,program_end_time,program_channel))
        self.conn.commit()


#단독으로 수행시에만 작동함 > 테스트 코드 삽입하여 사용
if __name__ =='__main__':
    db = DBHelper()
    print(db.db_insertCrawlingData('1','2','3','4' ) )

    db.db_free()
