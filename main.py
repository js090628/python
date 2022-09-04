#71번
# my_variable = ()
# print(type(my_variable))

#72번
# movie_rank = ('닥터 스트레인지','스플릿','럭키')

#73번
# a = (1,)

#74번
# t = (1, 2, 3)
# t[0] = 'a'

#75번
# t = 1,2,3,4
# print(type(t))

#76번
# t = ('a', 'b', 'c')
# t = ('A','b','c')
# print(t)

#77번
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# data = list(interest)
# print(data)

#78번
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# data = tuple(interest)
# print(data)

#79번
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

#80번
# data = tuple(range(2,100,2))
# print(data)
# # [시작 값 : 끝 인덱스 -1 : 스텝]

# a, b, *c = (0, 1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4, 5]


#81번
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# # *vaild_score,a,b = scores
# *vaild_score,_,_ = scores
# print(vaild_score)

#82번
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,b,*vaild_score = scores
# print(vaild_score)

#83번
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, *valid_score, b = scores
# print(valid_score)

# #84번
# temp = { }
# print(type(temp))

# #85번
# ice = {'메로나':1000,'폴라포':1200,'빵빠레':1800}

# #86번
# ice['죠스바'] = 1200
# ice['월드콘'] = 1500

#87번
# ice = {'메로나': 1000, '폴로포': 1200, '빵빠레': 1800, '죠스바': 1200, '월드콘': 1500}
# print('메로나 가격:',ice['메로나'])

#88번
# ice['메로나'] = 1300

#89번
# del ice['메로나']
# print(ice)

#90번
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']    # 딕셔너리에 없는 값을 사용해서 인덱싱하면 에러가 발생한다.

#집합(Set)
#집합은 중복을 허용하지 않으며 순서가 없는 자료형이다. 만들 때에는 set()을 사용하여 집합을 만들어 줄 수 있다.
# s1 = set([1,2,3,4])
# s2 = set([3,4,5])
# s3 = set([6,7,8])
#합집합
# print(s1 | s2)
# print(s2 | s3)

#교집합
# print(s1 & s2)
# print(s2 & s3)

#차집합
# print(s1-s2)
# print(s2-s3)


#91번
inventory = {'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}

#92번
print(inventory['메로나'][0],'원')

#93번
print(inventory['메로나'][1],'개')

#94번
# inventory['월드콘'] = [500,7]
# print(inventory)

#95번
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# keys = list(icecream.keys())
# print(keys)

#96번
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# values = list(icecream.values())
# print(values)

#97번
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(sum(icecream.values()))

#98번
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)
# print(icecream)

#99번
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys,vals))
# print(result)

#100번
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date,close_price))
# print(close_table)