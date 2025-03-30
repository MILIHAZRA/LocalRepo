subject_taken=input("How many subject you have taken in IIT?")
print(subject_taken)
subject_1=input("enter the marks of subject 1:")
print(subject_1)

subject_2=input("enter the marks of subject 2:")
print(subject_2)

subject_3=input("enter the marks of subject 3:")
print(subject_3)
import numpy
average_marks=[90,78,67]
avg=numpy.mean(average_marks)
print(avg)

print(f"enter your average marks:{avg}")

if avg > 40:
    print("ypu are pass")
else:
    print("you are fail")