# ციკლში-ციკლი

for a in range(3):
    for b in range(2):
        print("lado")

#N2 , სადაც c,d არის საიტერაციო ცვლადი,ხოლო x არის საიკრემენტაციო 
x = 0
for c in range(4):
    for d in range(3):
        print(str(x) + "lado")
        x += 1
#N3
x = 0
for a in range(8):
    for b in range(5):
        for c in range(2):
            print(str(x) + " lado")
            x +=1

# while მეთოდი
total_price = 0
i = 0
while i < 7:
    age_of_user = int(input("enter users age: "))
    if age_of_user >= 5:
        total_price += 70
    i += 1
print(total_price)

#List - სია
#xinkali 2 lari
#mwvadi 20 lari
my_list = ["xinkali", "mwvadi"]
prices = [2,20]
print(my_list[0] + " " + str(prices[0]))
print(my_list[1] + " " + str(prices[1])) 