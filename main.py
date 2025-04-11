# 1. Variable and Data Type:
Name = "Jabir Bhuiyan"
Age = 24
is_Student = True

# 2. Arithmetic Operations:
print("Name:", Name, "Age:", Age, "Student:", is_Student)
print(type(Name), type(Age), type(is_Student))


# 3. Comparison Oparetor:
multiple = Age*2
plus = Age+3
minus = Age-5

print("Multiple:", multiple, "Plus:", plus, "Minus:", minus)

# 4. Logical Operator:
print(Age >= 18)
print(Age >= 18 and Age == 30)

# 5. Assignment Operator:
has_student_id = True

print("Has ID and student?", is_Student and has_student_id)
print("Has ID or permission?", has_student_id or is_Student)
print("Not a student?", not is_Student)

# 6. Identity Operator:
assignment_mark = 50
print(assignment_mark)

assignment_mark += 10
print(assignment_mark)

assignment_mark -= 5
print(assignment_mark)

assignment_mark *= 2
print(assignment_mark)

assignment_mark **= 2
print(assignment_mark)

assignment_mark //= 2
print(assignment_mark)

assignment_mark /= 2
print(assignment_mark)

assignment_mark %= 3
print(assignment_mark)

# 7. Membership Operator:
map=["Dhaka", "Chittagong", "Khulna", "Rajshahi", "Noakhali"]
print("Dhaka" in map)
print("Khulna" in map)
print("Borishal" in map)
print("Noakhali" in map)
print("Dhaka" not in map)
