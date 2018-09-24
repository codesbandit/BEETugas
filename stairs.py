from __future__ import print_function

num = input("Masukan Jumlah anak tangga = ")

for x in range(1,num):
    for y in range(1,num):
        if (x==y):
            print(" |_", end=" ")
        else:
            print(" ", end="")
    print()
