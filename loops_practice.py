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


# Simple and a bit more elegant with in line...

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [num for num in heights if num > 161]
print(can_ride_coaster)
