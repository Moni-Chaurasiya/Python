name="moni chaurasiya"
first_char= name[0]
print(first_char)

slice_name=name[5:]
print(slice_name)

num_list="123456789"
slice_num=num_list[3:] 
print(slice_num) # 456789

slice_num=num_list[:7]
print(slice_num) # 1234567

slice_num=num_list[:] 
print(slice_num) # 123456789

slice_num=num_list[0:7:2]  # 0 to 7 skipping by 2
print(slice_num) # 1357

print(name.lower()) 
print(name.strip())  # white space removed
print(name.replace("moni","soni"))

intro="My, name, is, Moni, Chaurasiya"
# print(intro.split(", "))
print(intro.split())

print(intro.find("Moni")) # -1 if not found in Sting

count="Moni Moni Chaurasiya"

nam="he sail, \"I live in mumbai\""
print(nam)
names="Moni\nChaurasiya"
print(names)
print(count.count("Moni"))  # Lower and upper letter will print in different way
print(name)

paths="rc:\\user\\pwd\\"
print(paths)

print("moni" in name)