#binary to decimal and octal
binary=(input("enter the binary number:\n"))
binary=binary.strip()
power=len(binary)-1
decimal=0
for i in range (len(binary)):
    decimal+=int(binary[i])*(2**power)
    power-=1
octal=str(oct(decimal))
print('The number',binary,'in octal is ',octal[2:])
print('The number',binary,'in decimal is',decimal)
           
