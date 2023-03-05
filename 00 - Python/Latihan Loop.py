# Latihan loop membuat segitiga

sisi = 10

# Menggunakan for
print("\n"+"FOR"+"\n")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

# Menggunakan while
print("\n"+"WHILE"+"\n")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

# Menggunkan continue
# Hanya ganjil saja
print("\n"+"Ganjil Saja"+"\n")

count = 1
while True:
    if (count%2):
        # Print jika ganjil
         print("*"*count)
         count += 1
    else:
        # Akan kembali ke atas jika ganjil
        count += 1
        continue
   
# Akan break jika count melebihi sisi
    if count > sisi:
        break

print("Cukuup")

# Segitiga sama sisi
print("\n"+"Sama sisi"+"\n")
spasi = int(sisi/2)
count = 1

while True:
    if (count%2):
        # Print jika ganjil
         print(" "*spasi,"+"*count)
         spasi -= 1
         count += 1
    else:
        # Akan kembali ke atas jika ganjil
        count += 1
        continue
   
# Akan break jika count melebihi sisi
    if count > sisi:
        break

print("Cukuup")