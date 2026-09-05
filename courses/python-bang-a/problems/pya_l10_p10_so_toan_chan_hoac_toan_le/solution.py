n = int(input())
toan_chan = True
toan_le = True
while n > 0:
    d = n % 10
    if d % 2 == 0:
        toan_le = False
    else:
        toan_chan = False
    n = n // 10
if toan_chan:
    print("TOAN CHAN")
elif toan_le:
    print("TOAN LE")
else:
    print("BINH THUONG")
