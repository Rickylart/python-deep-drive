# using a for loop to calculate a student height
studentHeights = [180, 124, 165, 173, 189, 169, 146]

for x in range(0, len(studentHeights)):
    studentHeights[x] = int(studentHeights[x])
    print(studentHeights)


# other way of doing it
total_height = 0

for height in studentHeights:
    total_height += height

total_length = 0
for length in studentHeights:
    total_length += 1
print(total_height)
print(total_length)

print(f"Other way of doing it : {round(total_height/total_length)}")

# this works too
totalHeight = sum(studentHeights) # total number of students height
totalLength = len(studentHeights) # total number of students

# calculating the average
average = round(totalHeight/totalLength)

print(f"The average height is : {average}")
