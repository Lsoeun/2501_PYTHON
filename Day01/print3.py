# 파이썬에서는 문장과 숫자를 연산하는 것이 불가능합니다.
print('안' + 10) # 오류 발생

# 이런 경우에는 형 변환이 필요합니다.
# 형 변환(casting) : 다른 데이터 타입으로 형을 변환시키는 것

# 문장형 -> 숫자형
# int() : Integer(정수)의 약자
print(int('10') + int('10')) # 문장이 숫자형으로 형 변환 되어서 20이 출력됩니다.

# 숫자형 -> 문장형
# str() : String(문장)의 약자
print(str(9) + '월') # 9월이 출력됩니다.