#프로그램의 정보를 담는 클래스

class programs:
    #멤버 변수 생성
    program_name = ''
    program_start_time = ''
    program_end_time = ''
    program_channel = ''

    #생성자
    def __init__(self, program_name,program_start_time,program_end_time,program_channel):
        self.program_name = program_name
        self.program_start_time = program_start_time
        self.program_end_time = program_end_time
        self.program_channel = program_channel
    

