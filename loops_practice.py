# print("This can be so much easier with loops!")
# print("This can be so much easier with loops!")
# print("This can be so much easier with loops!")
# print("This can be so much easier with loops!")
# print("This can be so much easier with loops!")
# print("This can be so much easier with loops!")
# print("This can be so much easier with loops!")
# print("This can be so much easier with loops!")
# print("This can be so much easier with loops!")
# print("This can be so much easier with loops!")

string = "This can be so much easier with loops!"

for i in range(10):
    print(string + " " + str(i))


# Modifying Lists Elegantly
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)
