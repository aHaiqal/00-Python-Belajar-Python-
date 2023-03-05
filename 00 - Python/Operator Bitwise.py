# Operator Bilangan Biner (Operasi masing-masing bit)

a = 9
b = 5
# Bitwise R (|)
c = a | b
print('\n======OR=====')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('====================================(|)')
print('nilai :',c,' , binary :',format(c,'08b'))

# Bitwise and (&)
c = a & b
print('\n======AND=====')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('====================================(&)')
print('nilai :',c,' , binary :',format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b
print('\n======XOR=====')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('====================================(^)')
print('nilai :',c,' , binary :',format(c,'08b'))

# Bitwise Not (~)
c = ~a
print('\n======NOT=====')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('====================================(~)')
print('nilai :',c,' , binary :',format(c,'08b'))
print('------------------------------------(^)')
d = 0b00001001
e = 0b11111111
print('nilai :',e^d,' , binary :', format(e^d, '08b'))

# Shifting

# Shift Right
c = a >> 2
print('\n======>>=====')
print('nilai :',a,' , binary :',format(a,'08b'))
print('=====================================(>>)')
print('nilai :',b,' , binary :',format(b,'08b'))
print('=====================================(>>)')\

# Shift Left (<<)
c = a << 2
print('\n======<<=====')
print('nilai :',a,' , binary :',format(a,'08b'))
print('=====================================(<<)')
print('nilai :',b,' , binary :',format(b,'08b'))
print('=====================================(<<)')