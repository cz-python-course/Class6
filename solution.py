#1. Create a program that reads the number of students in a class, and stores the name of every student
totalStudents = int(input('How many students? '))
students = []
for x in range(totalStudents):
    answer = input("student's name: ")
    students.append(answer)

#2. Implement a program that calculates the sum of 5 numbers,then prints the numbers and the total sum.
numbers = []
totalSum = 0
for _ in range(5):
    answer = int(input("type a number: "))
    numbers.append(answer)
    totalSum  = totalSum + answer

for number in numbers:
    print(number)
print("Sum: " + str(totalSum))
