#hàm range nhận vào 3 tham số a,b,c với a là giá trị bắt đầu, b-1 là giá trị kết thúc, c là bước nhảy
for w in range(0,11,3):
    print(w)

tens = ["Toan", "Duy", "Vien", "Vu", "Tien", "Anh"]
for i in range(0,len(tens)):
    print(tens[i])

for t in tens:
    print(t)

for s in "toi la ton".split(" "):
    print(s)

#in ra những số chia hết cho 5 trong khoảng từ 1=>100
# Làm ít nhất 2 cách
for i in range(0,101):
    i = i+1
    if i%5 == 0:
        print(i)

for i in range(0,101,5):
    if i != 0:
        print(i)

#demo vong lap while

j = 1
while(j < 10): #kiểm tra j và tiếp tục chạy nội dung bên trong nếu điều kiện vẫn còn trả về True
    print(j)
    j += 1


