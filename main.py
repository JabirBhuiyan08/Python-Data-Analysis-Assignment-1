# 1. ভ্যারিয়েবল ও ডাটা টাইপ:
Name = "Jabir Bhuiyan"
Age = 24
is_Student = True

# 2. অ্যারিথমেটিক অপারেশন:
print("Name:", Name, "Age:", Age, "Student:", is_Student)
print(type(Name), type(Age), type(is_Student))


# 3. কম্পারিজন অপারেটর:
multiple = Age*2
plus = Age+3
minus = Age-5
print("Multiple:", multiple, "Plus:", plus, "Minus:", minus)

# 4. লজিক্যাল অপারেটর:
print(Age >= 18)
print(Age >= 18 and Age == 30)

# 5. অ্যাসাইনমেন্ট অপারেটর:
has_student_id = True

print("Has ID and student?", is_Student and has_student_id)
print("Has ID or permission?", has_student_id or is_Student)
print("Not a student?", not is_Student)

# 6. আইডেন্টিটি অপারেটর:
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

# 7. মেম্বারশিপ অপারেটর:
map=["Dhaka", "Chittagong", "Khulna", "Rajshahi", "Noakhali"]
print("Dhaka" in map)
print("Khulna" in map)
print("Borishal" in map)
print("Noakhali" in map)
print("Dhaka" not in map)
