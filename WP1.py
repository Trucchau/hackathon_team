N = (["không", 0], ["một", 1], ["hai", 2], ["ba", 3], ["bốn", 4], ["năm", 5], ["sáu", 6], ["bảy", 7], ["tám", 8],
     ["chín", 9], ["mười", 10])

#Nhập số n:
n = int(input("Enter n :"))

#Đếm số chữ số của n:
def count_number(n):
    i = 10
    s = 1
    while i <= 1000000000000:
        a = n // i
        if a == 0:
            sochuso = s
            break
        s += 1
        i *= 10
    return sochuso

#Đọc số có 2 chữ số:
def read_2(N, n):
    ans = []
    sodautien = n // 10
    sothu2 = n % 10
    if sodautien == 1:
        if sothu2 == 5:
            ans = "mười lăm"
        elif sothu2 != 0:
            ans = "mười " + N[sothu2][0]
        else:
            ans = "mười"
    else:
        if sothu2 == 5:
            ans = N[sodautien][0] + " mươi lăm"
        elif sothu2 == 1:
            ans = N[sodautien][0] + " mươi mốt"
        elif sothu2 != 0:
            ans = N[sodautien][0] + " mươi " + N[sothu2][0]
        else:
            ans = N[sodautien][0] + " mươi"
    return ans

#Đọc số có 3 chữ số (trường hợp số bé hơn 1000)
def read_3_1(N, n):
    ans = []
    sodautien = n // 100
    sothu2 = (n % 100) // 10
    sohangchuc = n % 100
    sothu3 = (n % 100) % 10
    if sohangchuc == 0:
        ans = N[sodautien][0] + " trăm"
    elif sothu2 == 0:
        ans = N[sodautien][0] + " trăm linh " + N[sothu3][0]
    else:
        ans = N[sodautien][0] + " trăm " + read_2(N, sohangchuc)
    return ans

#Đọc số có 3 chữ số (trường hợp số ở vị trí hàng trăm trong số n > 1000)
def read_3_2(N, n):
    ans = []
    sodautien = n // 100
    sothu2 = (n % 100) // 10
    sohangchuc = n % 100
    sothu3 = (n % 100) % 10
    if sodautien == 0 and sothu2 != 0:
        ans = "không trăm " + read_2(N, sohangchuc)
    elif sodautien == 0 and sothu2 == 0 and sothu3 != 0:
        ans = "không trăm linh " + N[sothu3][0]
    elif sodautien != 0:
        ans = read_3_1(N, n)
    elif sodautien == 0 and sothu2 == 0 and sothu3 == 0:
        ans = ""
    return ans

#Đọc số hàng ngàn:
def read_thousand(N, n):
    ans = []
    sohangngan = n // 1000
    sohangtram = n % 1000
    if count_number(sohangngan) == 2:
        ans = read_2(N, sohangngan) + " nghìn " + read_3_2(N, sohangtram)
    elif count_number(sohangngan) == 3:
        ans = read_3_1(N, sohangngan) + " nghìn " + read_3_2(N, sohangtram)
    elif sohangngan < 10 and sohangngan > 0:
        ans = N[sohangngan][0] + " nghìn " + read_3_2(N, sohangtram)
    elif sohangngan == 0:
        ans = read_3_2(N, sohangtram)
    return ans

def read_thousand_2(N, n):
    ans = []
    sohangngan = n // 1000
    sohangtram = n % 1000
    if sohangngan < 100:
        ans = read_3_2(N, sohangngan) + " nghìn " + read_3_2(N, sohangtram)
    elif sohangngan < 10:
        ans = read_3_2(N, sohangngan) + "nghìn" + read_3_2(N, sohangtram)
    elif sohangngan == 0:
        ans = read_3_2(N, sohangtram)
    return ans

#Đọc số hàng triệu:
def read_million(N, n):
    ans = []
    sohangtrieu = n // 1000000
    sohangngan = n % 1000000
    if count_number(sohangtrieu) == 2:
        ans = read_2(N, sohangtrieu) + " triệu " + read_thousand_2(N, sohangngan)
    elif count_number(sohangtrieu) == 3:
        ans = read_3_1(N, sohangtrieu) + " triệu " + read_thousand_2(N, sohangngan)
    elif sohangtrieu < 10 and sohangtrieu > 0:
        ans = N[sohangtrieu][0] + " triệu " + read_thousand_2(N, sohangngan)
    elif sohangtrieu == 0:
        ans = read_thousand(N, sohangngan)
    return ans

def read_million_2(N, n):
    ans = []
    sohangtrieu = n // 1000000
    sohangngan = n % 1000000
    if sohangtrieu < 100:
        ans = read_3_2(N, sohangtrieu) + " triệu " + read_thousand_2(N, sohangngan)
    elif sohangngan < 10:
        ans = read_3_2(N, sohangtrieu) + " triệu " + read_thousand_2(N, sohangngan)
    elif sohangngan == 0:
        ans = read_thousand(N, sohangngan)
    return ans


#Đọc số hàng tỉ:
def read_billion(N, n):
    ans = []
    sohangty = n // 1000000000
    sohangtrieu = n % 1000000000
    if count_number(sohangty) == 2:
        ans = read_2(N, sohangty) + " tỉ " + read_million_2(N, sohangtrieu)
    elif count_number(sohangty) == 3:
        ans = read_3_1(N, sohangty) + " tỉ " + read_million_2(N, sohangtrieu)
    elif sohangty < 10 and sohangty > 0:
        ans = N[sohangty][0] + " tỉ " + read_million_2(N, sohangtrieu)
    elif sohangty == 0:
        ans = read_million(N, sohangtrieu)
    return ans

#Hàm tổng:
def integer_to_vietnamese_numeral(n):
    if not isinstance(n, int):
        raise TypeError("Not an integer.")
    if n < 0:
        raise ValueError("Not positive integer.")
    if n > 999999999999:
        raise OverflowError
    if n <= 10:
        result = N[n][0]
    elif n > 10 and n <= 100:
        result = read_2(N,n)
    else:
        result = read_billion(N, n)
    return result 

print(integer_to_vietnamese_numeral(n))