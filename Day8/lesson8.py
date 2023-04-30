# ფუნქციონალური პროგრამირება - functional programming
def wish_a_good_day(name, day):
    print(name + " karg dges gisurveb " + str(day) + " octombers")
wish_a_good_day("lado",8)

# შევკრიბოთ მნიშვნელობები
def shekreba(num1,num2,num3):
    print(num1+num2+num3)
shekreba(8,15,44)

#N2
def pair_sum(arr1, arr2):
    for i in range(len(arr1)):
        print(arr1[i]+arr2[i])
pair_sum([10,15,5], [8,21,23])

# მაქსიმალური რიცხვის გამოსახვა while - მეთოდით
score=[7,10,30,77,15,8]
max_num=score[0]
i=0
while i < len(score):
    if score[i] > max_num:
        max_num=score[i]
    i += 1
print(max_num)