#Make a list, gets numbers divisible by 4 or 6 ONLY
divisibleByFourOrSix = [n ** 2 for n in range (1, 100) if n % 4 == 0 or n % 6 == 0]

print (divisibleByFourOrSix)