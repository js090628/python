# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])
# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])
# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0])
# print(interest[2])
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(' '.join(interest))
# print('\n'.join(interest))
# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest)
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

# 투플(Tuple)
# 튜플은 리스트와 몇 가지를 제외하면 리스트와 매우 유사하다.
# t1 = ()     #비어있는 튜플
# t2 = (2,)   # 값이 하나 있는 튜플 = 원소 뒤에 콤마를 붙혀서 Tuple로 인식시킨다.
# print(type(t2))
# t3 = (1,2,3) #값이 여러개 있는 튜플

# s1 = "ABC"
# l1 = list(s1)
# print(l1)
# l2 = [1,2,3]
# t4 = tuple(l2)
# print(t4,type(t4))

# tuple은 값의 생성, 수정, 삭제가 불가능한 immutable한 자료형이다.
# t1 = (1,2,3,4)
# t1 = list(t1)
# t1[2] = 7
# t1 = tuple(t1)
# print(t1)

# t1[2] = 7
# print(t1)

# s1 = "1234"
# s1[2] = 7
# print(s1)

# del l1[2]
# print(t1)

# l1 = [1,2,3,4]
# 리스트의 수정
# l1의 2번째 값을 7로 변경
# l1[2] = 7
# print(l1)

# 리스트와 튜플의 공통점
# t1 = (1,2,3,4,5)
# t2 = (6,7,8)
# 1. 인덱싱, 슬라이싱
# print(t1[3])    #출력값 4
# print(t1[1:3])  #출력값 (2, 3)

#슬라이싱
# 변수[x:y] == 변수의 x번째 index부터 u-1 index까지 범위를 잘라낸다.

# 2. 덧셈 곱셈 연산
# t3 = t1 + t2
# print(t3)
# t4 = t2 * 2
# print(t4)

# print(len(t4))  #길이 == 원소의 개수

#71번
# my_variable = ()

#72번
# movie_rank = ("닥터 스트레인지" ,"스플릿", "럭키")

#73번
# t1 = (1,)   #튜플에 원소가 하나 있을경우 꼭 콤마(,)를 붙혀줘야 한다.
# print(type(t1))

#74번
# t = (1, 2, 3)
# t[0] = 'a'  #tuple은 immutable한 자료형이기 때문에 원소의 변경이 불가능하다.

#75번
# t = 1, 2, 3, 4      #소괄호 ()가 없어도 원소를 나열하면 tuple로 인식한다.
# print(type(t))

#76번
# t = ('a', 'b', 'c')
# # t를 ('A', 'b', 'c')로 변경
# t = ('A', 'b', 'c')

#77번 튜플 => 리스트  자료형의 변환(형변환)
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# l_inter = list(interest)
# # print(l_inter)

#78번 리스트 => 튜플
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# t_inter = tuple(interest)
# print(t_inter, type(t_inter))

#79번 언팩킹(unpacking) == 묶여있는 원소들을 풀어해친다.
#unpacking을 하기 위해서는 원소를 받아줄 변수가 원소의 개수와 동일하게 있어야 한다.
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print("a = %s, b = %s, c = %s" %(a,b,c))

#80번    range(시작인덱스, 끝인덱스, step) => 함수 사용 방법은 슬라이싱과 매우 유사하다.
# t1 = tuple(range(2,100,2))
# print(t1)

#딕셔너리 생성
# d1 = {"key":"value"}
# a = ["Hello"]
# b = ["Python"]
# d2 = dict(zip(a,b))
# print(d1["key"])

# d1 = {"apple":"사과","banana":"바나나"}
# 딕셔너리 value의 수정
# d1["apple"] = "파인애플"
# 딕셔너리 key:value 삭제
# del d1['banana']
# 딕셔너리 key:value 추가
# d1["mango"] = "망고"
# print(d1)

# d1 = {"A" : 1,"A":2}
# print(d1["A"])
#Key값에 mutable 자료형을 사용할 경우
# d2 = {[1,2,3]: "숫자"}
# d3 = {(1,2,3): "숫자"}

# print(d3[(1,2,3)])

# d1 = {"A" : 1,"B" : 2,"C" : 3}
# key값들만 모은 변수 keys
# keys = list(d1.keys())
# values = list(d1.values())
# items = list(d1.items())
# print(items[0])
# print(1 in d1.values())