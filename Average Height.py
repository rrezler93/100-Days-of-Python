student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

how_many = 0
how_much = 0
for i in student_heights:
    how_many +=1
    how_much += i
sum = round(how_much / how_many)
print(sum)


