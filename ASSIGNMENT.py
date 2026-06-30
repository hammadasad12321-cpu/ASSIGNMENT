
print("--- Question 1:A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.Ask user for their salary and year of service and print the net bonus amout. ---")
#Answer:
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))
if years > 5:
    bonus = salary * 0.05
    print("Bonus =", bonus)
else:
    print("No bonus")
print()
print("--- Question 2:Write a program to check whether a person is eligible for voting or not.(Accept age from user) if age is greater than 17 eligible otherwise not eligible. ---")
#Answer:
age = int(input("Enter age: "))
if age > 17:
    print("Eligible for voting")
else:
    print("Not eligible")
print()
print("--- Question 3:Write a program to check whether a number entered by user is even or odd. ---")
#Answer:
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
print()
print("--- Question 4:Write a program to check whether a number is divisible by 7 or not.Show Answer. ---")
#Answer:
num = int(input("Enter number: "))
if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")
print()
print("--- Question 5:Write a program to display 'Hello' if a number entered by user is a multiple of five,otherwise print 'bye'. ---")
#Answer:
num = int(input("Enter number: "))
if num % 5 == 0:
    print("Hello")
else:
    print("Bye")
print()
print("--- Question 6:Take values of length and breadth of a rectangle from user and print if it is sqaure or rectangle. ---")
#Answer:
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
if length == breadth:
    print("Square")
else:
    print("Rectangle")
print()
print("--- Question 7:Take two int values from user and print greatest among them. ---")
#Answer:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greatest =", a)
else:
    print("Greatest =", b)
print()
print("--- Question 8:A school has following rules for grading system: ---")
#grading system:--
print("--- a.Below 25 - F ---")
print("--- b.25 to 45 - E ---")
print("--- c.45 to 50 - D ---")
print("--- d.50 to 60 - C ---")
print("--- e.60 to 80 - B ---")
print("--- f.Above 80 - A ---")
#Answer:
marks = int(input("Enter marks: "))
if marks < 25:
    print("F")
elif marks <= 45:
    print("E")
elif marks <= 50:
    print("D")
elif marks <= 60:
    print("C")
elif marks <= 80:
    print("B")
else:
    print("A")
print()
print("--- Question 9:Ask to enter age,gender (M or F),marital status (Y or N) and then using following rules print their place or service. ---")
print("--- If employee is female, then she will work only in urban areas. ---")
print("--- If employee is male and age is in between 20 to 40 then he may work in anywhere. ---")
print("--- If employee is male and age is in between 40 to 60 then he will work in urban areas only. ---")
print("--- And any other input of age should print 'Error'. ---")
#Answer:
age_input = input("Enter age: ")
gender = input("Enter gender (m or F): ")
marital_status = input("Enter matiral status (Y or N): ")
try:
    age = int(age_input)
except ValueError:
    print("")
    exit()
if gender == 'F':
    if 20 <= age <60:
        print("Place of service: Urban areas")
    else:
        print("Error")
elif gender == 'M':
    if 20 <+ age < 40:
     print("Place of service: Anywhere")
    elif 40 <= age <= 60:
        print("Place of service: Urban areas")
    else:
     print("Error")
else:
    print("Error")