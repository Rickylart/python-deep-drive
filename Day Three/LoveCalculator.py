print("Welcome to the Love Calculator")

first_name = input("Enter only your name ? ").lower()
second_name = input("Enter only your the name of your partner ? ").lower()
combined_names = first_name+second_name

# counting the true word characters
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true = t + r + u + e

# counting the love word characters
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score > 39 and love_score < 51:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")


print(love_score)
