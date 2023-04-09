my_name = "lado"
for char in my_name:
    print(char)
print("d" in "lado")
name1 = input("enter name1: ")
name2 = input("enter name2: ")
ammount_of_vowels_in_name1 = 0
ammount_of_vowels_in_name2 = 0
for char in name1:
    if char in "aeiou":
        ammount_of_vowels_in_name1 += 1
for char in name2:
    if char in "aeiou":
        ammount_of_vowels_in_name2 += 1
if ammount_of_vowels_in_name1 > ammount_of_vowels_in_name2:
    print("the ammount of vowels in name 1 is more and it contains {} vowels".format(ammount_of_vowels_in_name1))
elif ammount_of_vowels_in_name1 < ammount_of_vowels_in_name2:
    print("the ammount of vowels in name2 is more and it contains {} vowels".format(ammount_of_vowels_in_name2))
else:
    print("they have equal ammount of vowels")

my_txt = input("enter some txt: ")
ammount_of_a = 0
for char in my_txt:
    if char == "a":
        ammount_of_a += 1
print('there is {} "a" in my text'.format(ammount_of_a))