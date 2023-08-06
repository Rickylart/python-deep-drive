# studentScore = [78, 65, 89, 55, 91, 64, 89]

studentScore = input("Enter your score, split each score with a comma :\n ").split(",")

print(studentScore)

highestScore = 0
for score in studentScore:
    if int(score) > highestScore:
        highestScore = int(score)
print(highestScore)