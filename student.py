name = input("Enter your name: ")
m1 = int(input("Enter Python marks : "))
m2 = int(input("Enter Sql marks : "))
m3 = int(input("Enter Excel marks : "))

total = m1 + m2 + m3

percentage = total/3 * 100
print(f"student name {name} \n total marks: {total} \n Percentage: {percentage}")
