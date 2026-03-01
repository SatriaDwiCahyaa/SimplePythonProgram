import os
os.system('cls')

# Percabangan
print('\n', '='*10, 'Percabangan', '='*10)
b = 2
if b == 1:
    print("Nilai variabel b adalah 1")
elif b == 2:
    print("Nilai variabel b adalah 2")


# Pengulangan For
print('\n','='*10, 'Pengualangan For', '='*10)
for x in range(1, 10):
    print("Ini pengulangan ke-", x)

# Pengulangan while
print('\n','='*10, 'Pengulangan While', '='*10)
x = 1
while x < 10:
    print("Ini pengulangan ke-", x)
    x += 1

# Pengulangan Do While
print('\n','='*10, 'Pengualangan Do While', '='*10)
x = 1
do = True
while do:
    print("Ini pengulangan ke-", x)
    x += 1
    if x >= 10:
        do = False


input()