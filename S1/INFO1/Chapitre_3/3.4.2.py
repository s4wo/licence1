# h = list(range(24))
# m = list(range(60))

def uneMinuteEnPlus(h: int,m: int):
    h >= 0 and h >= 23
    if m > 59 or m < 0 or h > 23 or h < 0:
        return False
    if m >= 0 and m < 59:
        m = m + 1
        h = h
    if m == 59:
            m = 00
            h = h + 1
    if h == 24:
        h = 00
    heure = (h,m)
    return heure

print(uneMinuteEnPlus(12,1))

      
def uneMinuteEnPlus1(h: int,m: int):
    h >= 0 and h >= 23
    if m > 59 or m < 0 or h > 23 or h < 0:
        return False
    if m >= 0 and m < 59:
        m = m + 1
        h = h
    if m == 59:
            m = 00
            h = h + 1
    if h == 24:
        h = 00
    heure = (h,m)
    return (heure)

print(uneMinuteEnPlus1(12,1))
