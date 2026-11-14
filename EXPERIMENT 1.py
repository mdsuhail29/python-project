name =input("Enter student name:")
n=int(input("enter no.of subjects:"))
total=0
for i in range(1,n+1):
    mark=float(input("Enter mark for the subject{i}:"))
    total+=mark
percentage=total/n
if percentage >=90:
    grade ="A+"
    performance="outstanding"
elif percentage >=80:
    grade ="A"
    performance="excellent"
elif percentage >=70:
    grade ="B"
    performance="very good"
elif percentage >=60:
    grade ="C"
    performance="good"
elif percentage >=50:
    grade ="D"
    performance="average"
else:
    grade="F"
    performance="need improvement"
print("\n---ACADEMIC PERFORMANCE---")
print("STUDENT NAME: ",name)
print("TOTAL MARKS:",total)
print("PERCENTAGE:",round(percentage,2),"%")
print("GRADE:",grade)
print("PERFORMANCE:",performance)
    
    
