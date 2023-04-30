# # წაიშალოს ელემენტები სადაც მეორე ასო არის a
menu=["banani","yviteli","tetri"]
for food in menu:
    if food[1] == "a":
        menu.remove(food)
print(menu)

# დავალაგოთ რიცხვები ზრდადობის მიხედვით
scores=[8,62,21,23]
scores.sort()
print(scores)

# გავიგოთ რიცხვების მაქსიმალური და მინიმალური მნიშვნელობა
scores=[1,3,8,15,21,23]
print(scores[-1])
print(scores[0])

# სია ანბანის მიხედვით
students=["lado","gio","mari","ana"]
students.sort()
print(students)

# შევაბრუნოთ
students=["lado","gio","mari","ana"]
students.sort(reverse=True)
print(students)

# სიტყვის ჩამატება
list=["a","c","d"]
list.insert(1,"b")
print(list)