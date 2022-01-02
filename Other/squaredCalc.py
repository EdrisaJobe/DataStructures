#Get the squared version of any number
number = raw_input("Enter a number to square: ")

def squared(number):

    result = number**2

    print ("%d squared is %d" % (number, result))
    return squared

#Gets result after print
squared(int(number))


###Exponents and base powers
numBase = "Enter base number: "
numExponent = "Enter exponent num: "

def power(numBase, numExponent):
    
    result = numBase ** numExponent
    print ("%d is the base, %d is the exponent, the result is: %d" % (numBase, numExponent, result))

power(1, 3)

