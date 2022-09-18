a = [4,1,2,[5,8,[9,7],3],6]
#출력 ==> 9
# print(a[3][2][0])

#리스트의 연산들(+,*)
a = [1,2,3,4]
b = [5,6,7,8]
# 리스트 + 리스트
c = a + b
# print(c)
# 리스트 * 정수
# print(b * 2)

# 길이 구하는 함수
# print(len(a))

# 튜플
# t1 = (1,2,3)
# t2 = [1,2,3]
# print(type(t1))
# 튜플과 리스트의 차이점 == 튜플은 수정, 삭제가 불가능하다.

#딕셔너리
# d1 = {}
# d1 = {"A": 1, "B": 2,"C":3}
# 딕셔너리에 key - value 추가
# d1["A"] = 1
# d1["B"] = 2
# d1["C"] = 3
# d1 = {"A": 4, "B": 5,"C":6}
# 딕셔너리의 value값 수정
# d1["A"] = 4
# d1["B"] = 5
# d1["C"] = 6
# {'A': 4, 'B': 5}
#딕셔너리의 key - value 삭제
# del d1["C"]
# print(d1)
# d1 = {"A": 1, "B": 2,"C":3}
#딕셔너리 멤버 메서드
#딕셔너리의 키값들의 모음
# key = d1.keys()
#딕셔너리의 벨류값들의
# value = d1.values()
#딕셔너리의 (키, 벨류)들의 모음
# item = d1.items()
# print(f"키 = {key}\n벨류 = {value}\n키, 벨류 = {item}\n")
# 해당 값이 딕셔너리에 존재하는지 확인
# 문자 A가 d1의 벨류값으로 존재하는지 확인
# print("A" in d1.values())
#Key값을 중복해서 사용한다면, 마지막 Key값의 value값이 사용된다.
#Key값에 변할 수 있는 자료형을 사용할 경우 에러 발생

# 집합(set)
# s1 = {1,2,3,4}
# print(type(s1))
# 집합의 특징
# A = {1,3,4,5,7}
# B = {2,5,6,7,8}

# 합집합  shift + \ => | 파이프
# hap = A | B
# 차집합 -
# cha = A - B
# 교집합  shift + 7 => & 엠퍼센트
# gyo = A & B
# print(f"합집합 = {hap}\n차집합 = {cha}\n교집합 = {gyo}")

#unpacking(언패킹)
# t1 = (1,2,3)
# a,b,c = t1
# print(f"a = {a}, b = {b}, c = {c}")

# keys = ("apple","pear","peach","mango")
# vals = (300,250,400,500 )
# z = list(zip(keys,vals))
# print(z)


#입력
# a,b = input().split()   # "7 3"
# a = int(a)
# b = int(b)
# print("%d + %d = %d" %(a, b, a+b))
# print("{} - {} = {}".format(a, b, a-b))
# print(f"{a} * {b} = {a*b}")
# print("%d / %d = %f" %(a, b, a/b))
# print("%d // %d = %d" %(a, b, a//b))
# print("%d %% %d = %d" %(a, b, a%b))
# % - formatting, format 메서드, f -string
# 출력 형태
# 7 + 3 = 10
# 7 - 3 = 4
# 7 * 3 = 21
# 7 / 3 = 2.33333
# 7 // 3 = 2
# 7 % 3 = 1

# s = input()
# print(s+"??!")