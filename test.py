import datetime

#############텍스트 포함 값 확인 

# test_text1 = ['이산수 - 123123','삼겹살스 - 123545','돼지 - 453234','엉덩이 = 344']

# print (test_text1)
# if '이산' in test_text1:
#     print('있음')
# else:
#     print('없음')

# search_text = ['이산','삼겹살']
# for li in test_text1:
#     for li2 in search_text:
#         print(li2, li)
#         if li2 in li:
#             print('있음')
#         else:
#             print('없음')



#########시간 값 확인

time1 = '15:50'

runtime = '40'

print(time1.split(':')[1])

sttime = datetime.time(15,30)
edtime = datetime.time(0,40)

sttime1 = datetime.datetime(100,1,1,15,30)
edtime1 = datetime.time(0,40)

b = sttime1 + datetime.timedelta(minutes=40)

print(sttime1.time())
print(b.time())
