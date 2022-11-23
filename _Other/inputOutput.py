#there are 10 carrots
carrot = 10
carrot_price = 24.30
total_price = carrot * carrot_price

#calculation
print(total_price)

#calculation2
cucumbers = 100 #float(100) needed to get decimal
num_people = 6
whole_cucumbers_per_person = cucumbers / num_people
float_cucumbers_per_person = float(cucumbers) / num_people

#Does not round or get decimal just gets first place number
print(whole_cucumbers_per_person)
#Gets the full decimal postion and numbers
print(float_cucumbers_per_person)

#True or False inputs
answer = "Left"

if answer == "Left":
    print("It is correct!")

if 1 > 2:
    print("\nThat is correct")
else:
    print("\nThat is wrong")
