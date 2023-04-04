

my_name="lado"
my_surname="talakvadze"
my_age=23
my_sentence="aa {0} bb {1} cc {2}".format(my_name, my_surname, my_age)
print(my_sentence)


my_name="lado"
if "k" in my_name:
    print("sheicavs k-s")
else:
    print("ar sheicavs k-s")
          


my_name = input("enter your name: ")
print("chemi saxelia " + my_name)


my_age = 23
my_age += 7
print(my_age)


my_age = input("enter your age: ")
my_name = input("enter your name: ")
my_surname = input("enter your surname: ")
print("my name is {} my surname is {} my age is {}".format(my_name, my_surname, my_age))
year = input("enter years")
new_age = int(my_age) + int(year)
print("after {} years i am now {} years old".format(year, new_age))



num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
product = num1 * num2

if product > 100:
    print(product)
else:
    print("you lose")


num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

#sainkrementacio cvladi
my_sum = 0
#11, 15, 8
if num1 % 2 == 1:
    my_sum += num1
if num2 % 2 == 1:
    my_sum += num2
if num3 % 2 == 1:
    my_sum += num3

print("the sum of add number is {}".format(my_sum))





  
