marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
