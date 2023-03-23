#사용자에계 입력
length=float(input("length:"))
width=float(input("width:"))
height=float(input("height:"))

#부피계산
volume=length*width*height

# 부피출력
print("Volume:",volume)
#요금계산
total_length=length+width+height

#제주도지역 아닌 지역으로 택배요금
#    80cm이하:5000
#80cm~100cm:8000
# 100cm~120cm=10000
# 120cm~160cm=13000
#160cm이상:뱍송불가
if total_length<=80: #80이하
    charge=5000
elif total_length<=100: #100cm이하
    charge=8000
elif total_length<=120:
     charge=10000
elif total_length<=160:
     charge=13000
else:
     charge="unavailable"

print("Total length:",total_length)
print("Charge:",charge)
