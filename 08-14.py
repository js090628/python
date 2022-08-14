#a = "Hello Python"

#문자열은 immutable한 자료형이다. 변하지않는, 불변의
#print(a.count('o')) #출력값 => 2
#print(a.find('o')) #출력갑 => 2 없는값을 찾을경우 -1
#print(a.index('x'))#출력값 => 2 없는값을 찾을경우 에러 발생
#print(','.join(a)) #출력값 => H,e,l,l,o, ,P,y,t,h,o,n
#print(a.replace('Py','MY')) #출력값 => Hello Mython
#print(a.split()) #출력값 => ['Hello', 'Python']
#print(a.upper()) #출력값 => HELLO PYTHON
#print(a.lower()) #출력값 => hello python
#print(a)#함수를 실행해도 a의 원본 데이터는 변하지 않는다.

#a = 128
#print(type(a)) #int = 정수(양의정수, 음의정수, 0)
#num_str = '720'
#print(type(num_str)) # str = 문자열

#num = int(num_str)
#print(type(num))

#num = 100
#num_str = str(num) #형변환 int -> str
#print(type(num_str))  # <class 'str'>

#21번
#letters = 'python'
#print(letters[0], letters[2])

#22번
#license_plate = "24가 2210"
#print(license_plate[-4:])

#23번
#string = "홀짝홀짝홀짝"
#print(string[::2])

#24번
#string = "PYTHON"
#print(string[::-1])

#25번
#phone_number = "010-1111-2222"
#print(phone_number.replace('-',' '))

#26번
#phone_number = "010-1111-2222"
#print(phone_number.replace('-',''))

#27번
#url = "http://sharebook.kr"
#print(url.split('.')[-1])

#28번
#lang = 'python'
#lang[0] = 'p'
#print(lang) #문자열은 수정할 수 없다.

#29번
#string = 'abcdef2a354a32a'
#print(string.replace('a','A'))

#30번
#string = 'abcd'
#string.replace('b','B')
#print(string) #abcd가 그대로 출력된다.

#31번
a = "3"
b = "4"
print(a+b) #34

#32번
print("Hi" * 3) #HiHiHi

#33번
print('-' * 80)

#34번
t1 = 'python'
t2 = 'java'
print((t1+' '+t2+' ') * 4)

#출력방식
#35번 %formatting
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름:",name1,"나이:",age1)
print("이름: %s 나이: %d" %(name1,age1))
# %s = 문자열 값, %d = 정수 값, %f = 실수, %c = 문자 값
#36번 format() 메써드
print("이름: {0} 나이: {1}".format(name1,age1))
#37번 f-string
print(f"이름: {name1} 나이: {age1}")

#38번
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(',','')
상장주식수 = int(상장주식수)
print(type(상장주식수))
#39번 문자열 슬라이싱
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])
# print(분기[:7]) #0번 인덱스 부터 6번 인덱스까지 범위를 보겠다.
#40번 strip 메서드
data = "   삼성.전자   "
print(data.lstrip('.')) #왼쪽에서부터 연속되는 문자열 지우기
print(data.strip('.')) #양쪽에서부터 연속되는 문자열 지우기
print(data.rstrip('.')) #오른쪽에서부터 연속되는 문자열 지우기