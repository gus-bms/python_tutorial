###############################################################################################
"""
#ex001
print("Hello World")

#ex002
print("Mary's cosmetics")

#ex003
print("신씨가 소리질렀다. \"도둑이야\".")

#ex004
print('"C:\Windows"')

#ex005
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n은 줄바꿈 역할을하며 \t는 탭의 역할을 한다. \는 뒤에오는 특정문자가 기능을하게함

#ex006
print('오늘은',"금요일")

#ex007
print("naver","kakao","sk","samsung",sep=";")

#ex008
print("naver","kakao","sk","samsung",sep="/")

#ex009
print("first",end="");print("second")

#ex010
print(5/3)

###############################################################################################

#ex011
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

#ex012
시가총액 = 298 * 1000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

#ex013
s = "hello"
t = "python"
print(s+"!",t)

#ex014
print(2+2*3)

#ex015
a = 132
print(type(a))

#ex016
num_str = "720"
num_str = int(num_str)
print(num_str, type(num_str))

#ex017
num = 100
num = str(num)
print(num, type(num))

#ex018
str1 = "15.79"
str1 = float(str1)
print(str1, type(str1))

#ex019
year = "2020"
year = int(year)
print(year-3, year-2, year-1)

#ex020
aircon = 48584
totalP = aircon * 36
print(totalP)

###############################################################################################

#ex021
letters = 'python'
print(letters[0],letters[2])

#ex022
license_plate = "24가 2210"
print(license_plate[-4:])
# python에서 문자열의 특정 자리를 슬라이싱 가능함, 뒷자리는 음수로 시작을하고 -1부터 시작이다.
# : 를 붙이면 몇번째부터 끝까지 라는 뜻을의미

#ex023
string = "홀짝홀짝홀짝"
print(string[::2])
# []는 시작idx, 끝idx, stride를 지정할 수 있다. stride은 뛰어넘는 간격이 얼마나 되는지를 의미
# offset은 문자열에서의 주소를 의미하고 offset을 사용하여 데이터를 추출하는 것을 인덱싱이라 함.

#ex024
string = "python"
print(string[::-1])

#ex025
ph_num = "010-1111-2222"
ph_num = ph_num.replace("-", " ")
print(ph_num)

#ex026
ph_num = ph_num.replace(" ","")
print(ph_num)

#ex027
url = "http://sharebook.kr"
split = url.split('.')
print(url[-2:])
print(split[-1])

#ex028
# lang = 'python'
# lang[0] = 'P'
# print(lang)
# 파이썬에서 문자열은 수정 불가함

#ex029
str2 = 'aekjfal13avajlsd1D3ea'
upper = str2.replace('a', 'A')
print(upper)

#ex030
str3 = 'abcd'
str3.replace('b','B')
print(str3)

###############################################################################################

#ex031
a = "3"
b = "4"
print (a+b)

#ex032
print ("hi" * 3)

#ex033
print('-' * 90)

#ex034
t1 = 'python'
t2 = 'java'
print((t1+' '+t2+' ') *4)

#ex035
name1 = "김민수"
age1  = 10
name2 = "이철희"
age2  = 13
print("이름:", name1, "나이:",age1, "\n이름:",name2, "나이:", age2)
print("이름: %s 나이: %d \n이름: %s 나이: %d" % (name1, age1, name2, age2))

#ex036
print("이름: {} 나이: {}\n이름: {} 나이: {}".format(name1,age1,name2,age2))

#ex037
print(f"이름: {name1} 나이: {age1}\n이름: {name2} 나이: {age2}")

#ex038
cnt = "5,969,782,550"
cnt = int(cnt.replace(",",""))
print(cnt, type(cnt))

#ex039
quarter = "2020/03(E) (IFRS연결)"
quarter = quarter[:7]
print(quarter)

#ex040
data = "   삼성전자   "
print(data.replace("   ",""))
print(data.strip())
#strip method는 문자열 좌우 공백을 지워줌
"""
#ex041
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)

#ex042
tiker = ticker.lower()
print(tiker)

#ex043
str4 = "hello"
str4 = str4.capitalize()
print(str4)

#ex044
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
# endswith는 문자열 마지막이 어떻게 끝나는지 확인할 수 있으며, 문자/문자열 둘다 가능하다

#ex045
print(file_name.endswith(("xlsx","xls")))
# endswith의 인자값은 튜플형식도 가능하다.

#ex046
file_name2 = "2020_보고서.xlsx"
print(file_name2.startswith("2020"))

#ex047
a = "hello python"
print(a.split(" "))

#ex048
ticker = "btc_krw"
print(ticker.split("_"))

#ex049
date = "2022-01-14"
year = date.split("-")[0]
month = date.split("-")[1]
day = date.split("-")[-1]
print(year,month,day)

#ex050
data = " 0301391    "
print(data.rstrip())


def add(a,b) :
    return a,b
r,b = add("(1,21)",2)
print(type(r))