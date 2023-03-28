actyear = 2023
myyear = 1992

Actage = actyear - myyear

name = input("What's your name? ")
age = int(input("How old are you? "))

print ("Hello", name)
print ("Call me Linderinn. I'm ", Actage, "year's old")

if age > Actage:
    print("You're older than me by", (age - Actage), "years.")

else:
    print ("You're younger than me by", (Actage - age), "years.")
