# 문자열(str)
# a = "Hello World"

# 인덱싱, 슬라이싱 = 인덱스번호를 사용해서 하나 또는 범위를 집어내는 행위
# print(a[0])     # H
# print(a[2:5])   # llo

# 문자열 연산(+,*)
# b = "Hello"
# c = "Python"
# print(b +' '+ c)
# print(b * 3)

# 문자열 특징 = immutable(불변의, 변하지 않는)
# print(a.replace("He","De"))
# print(a)

# 리스트(list)
# l = [[1,2,3],[4,5,6]]
# print(l[1][0])
# 3 -> 5
# l = [1,2,3,4]
# l[2] = 5
# print(l)
# 4 삭제
# del l[3]
# print(l)
# 리스트 연산(+,*)

# tuple(튜플)
# t = 1,2,3,4
# print(type(t))

# 딕셔너리(dictionary)
# d = {"key":"value"}
# print(d["key"])
# 추가 삭제 수정
# apple : 사과 추가
# d['apple'] = "사과"
# apple = 파인애플 벨류 수정
# d['apple'] = "파인애플"
# apple : 파인애플 삭제
# del d['apple']
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())

#set 집합
# s = set("Hello")
# print(s)
# 집합의 특징
# 1) 중복된 값을 제거한다
# 2) 순서가 없다 => 인덱스 번호를 사용할 수 없다

# a = True
# b = False
# print(type(a))
# print(type(b))
# 자료형들의 참과 거짓
# print(bool("Python"), bool(''))    # 문자열

# print(bool([1,2,3]), bool([]))    # 리스트
# print(bool((1,2,3)), bool(()))    # 튜플
# print(bool({'a':1}), bool({}))    # 딕셔너리
#                             # 값이 있으면 참, 없으면 거짓
# print(bool(-8), bool(0))    # 정수  0을 제외한 모든 숫자는 참, 0만 거짓
# print(bool(None))           # None

# 조건문
# a = 4
# if a == 1:
    #print('a')
# elif a == 2:
    #print('b')
# elif a == 3:
    #print('c')
# elif a == 4:
    #print('d')
# else:
    #print('e')

# 비교 연산자 (A 비교연사자 B)
# A > B => A가 B보다 크다
# A < B => A가 B보다 작다
# A == B => A와 B는 같다.
# A != B => A와 B는 다르다.
# A >= B => A는 B보다 크거나 같다.
# A <= B => A는 B보다 작거나 같다.

# 논리 연산자 (and, or, not)
a,b,c,d = [3,4,5,3]
# if a == d or b > c:
    #print(True)
# else:
    #print(False)
# if not a:
    #print(True)
# else:
    #print(False)

# in ~안에 있는
# L1 = ['a','b','c','d']
# var = 1
# if var not in l1:
    #print(True)
# else:
    #print(False))

#111번
# s = input()
# print(s*2)

#112번
# i = int(input('숫자를 입력하세요:'))
# print(i+10)

#113번

# i = int(input('숫자를 입력하세요:'))
# # 짝수인지 판별 == i % 2 ==> 0
# if i % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# % 나머지를 구하는 연산자
# // 몫을 구하는 연산자

# 114번
# i = int(input("숫자를 입력하시오:"))
# #20을 더한값이 255를 초과하면 255 출력, 아니면 20 더한값 출력
# i += 20
# if i > 255:
#     print(255)
# else:
#     print(i)

# 115번
# i = int(input("숫자를 입력하시오:"))
# 20을 뺀 값이 0보다 작으면 0출력, 255보다 크면 255출력, 그게 아니면
# 20을 뺀 값 출력
# i -= 20
# if i > 255:
#     print(255)
# elif i < 0:
#     print(0)
# else:
#     print(i)

#116번
# time = input('현재 시간을 입력하세요:')  # 02:00
# if time[-2:] == '00':       #서로 같은 자료형끼리 비교를 해주어야 한다.
#     print("정각 입니다")
# else:
#     print("정각이 아닙니다")

# 117번
# fruit = ["사과","포도","홍시"]
# f = input("과일을 입력하세요:")
# if f in fruit:
#     print("정답입니다")
# else:
#     print("정답이 아닙니다")

# 119번
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# s = input("계절을 입력하세요:")
# if s in fruit:
#     print("정답입니다")
# else:
#     print("정답이 아닙니다")

# 120번
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# s = input("과일을 입력하세요:")
# if s in fruit.values():
#     print("정답입니다")
# else:
#     print("정답이 아닙니다")
