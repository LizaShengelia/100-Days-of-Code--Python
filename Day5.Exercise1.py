student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

num = 0
count = 0

for studentt in student_heights:
  num += studentt
  count = count + 1
print (round(num / count))

