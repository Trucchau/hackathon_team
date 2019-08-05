N = (["khong", 0], ["mot", 1], ["hai", 2], ["ba", 3], ["bon", 4], ["nam", 5], ["sau", 6], ["bay", 7], ["tam", 8],
     ["chin", 9], ["muoi`", 10])
n = int(input("Enter n :"))


def count_number(n):
    i = 10
    s = 1
    while i <= 1000000:
        a = n // i
        if a == 0:
            sochuso = s
            break
        s += 1
        i *= 10
    return sochuso


def read_2(N, n):
    ans = []
    sodautien = n // 10
    sothu2 = n % 10
    if sodautien == 1:
        if sothu2 == 5:
            ans = "Muoi` lam"
        elif sothu2 != 0:
            ans = "Muoi`" + N[sothu2][0]
        else:
            ans = "Muoi`"
    else:
        if sothu2 == 5:
            ans = N[sodautien][0] + " " + "muoi lam"
        if sothu2 == 1:
            ans = N[sodautien][0] + " " + "muoi mot' "
        elif sothu2 != 0:
            ans = N[sodautien][0] + " " + "muoi" + " " + N[sothu2][0]
        else:
            ans = N[sodautien][0] + " " + "muoi"
    return ans


def read_3_1(N, n):
    ans = []
    sodautien = n // 100
    sothu2 = (n % 100) // 10
    sohangchuc = n % 100
    sothu3 = (n % 100) % 10
    if sohangchuc == 0:
        ans = N[sodautien][0] + " tram"
    elif sothu2 == 0:
        ans = N[sodautien][0] + " tram " + "linh " + N[sothu3][0]
    else:
        ans = N[sodautien][0] + " tram " + read_2(N, sohangchuc)
    return ans


def read_3_2(N, n):
    ans = []
    sodautien = n // 100
    sothu2 = (n % 100) // 10
    sohangchuc = n % 100
    sothu3 = (n % 100) % 10
    if sodautien == 0 and sothu2 != 0:
        ans = "khong tram " + read_2(N, sohangchuc)
    elif sodautien == 0 and sothu2 == 0 and sothu3 != 0:
        ans = "khong tram linh " + N[sothu3][0]
    elif sodautien != 0:
        ans = read_3_1(N, n)
    elif sodautien == 0 and sothu2 == 0 and sothu3 == 0:
        ans = ""
    return ans


def read_thousand(N, n):
    ans = []
    sohangngan = n // 1000
    sohangtram = n % 1000
    if count_number(sohangngan) == 2:
        ans = read_2(N, sohangngan) + " nghin " + read_3_2(N, sohangtram)
    elif count_number(sohangngan) == 3:
        ans = read_3_1(N, sohangngan) + " nghin " + read_3_2(N, sohangtram)
    elif sohangngan < 10 and sohangngan > 0:
        ans = N[sohangngan][0] + " nghin " + read_3_2(N, sohangtram)
    elif sohangngan == 0:
        ans = read_3_2(N, sohangtram)
    return ans


def read_million(N, n):
    ans = []
    sohangtrieu = n // 1000000
    sohangnghin = n % 1000000
    if count_number(sohangtrieu) == 2:
        ans = read_2(N, sohangtrieu) + " trieu " + read_thousand(N, sohangnghin)
    elif count_number(sohangtrieu) == 3:
        ans = read_3_1(N, sohangtrieu) + " trieu " + read_thousand(N, sohangnghin)
    elif sohangtrieu < 10 and sohangtrieu > 0:
        ans = N[sohangtrieu][0] + " trieu " + read_thousand(N, sohangnghin)
    elif sohangtrieu == 0:
        ans = read_thousand(N, sohangnghin)
    return ans


def read_billion(N, n):
    ans = []
    sohangty = n // 1000000000
    sohangtrieu = n % 1000000000
    if count_number(sohangty) == 2:
        ans = read_2(N, sohangty) + " ty " + read_million(N, sohangtrieu)
    elif count_number(sohangty) == 3:
        ans = read_3_1(N, sohangty) + " ty " + read_million(N, sohangtrieu)
    elif sohangty < 10 and sohangty > 0:
        ans = N[sohangty][0] + " ty " + read_million(N, sohangtrieu)
    elif sohangty == 0:
        ans = read_million(N, sohangtrieu)
    return ans


print(read_billion(N, n))