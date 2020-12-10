# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill =0
if size == "S":
  print(" one small")
  bill += 15
elif size == " M ":
  print("thats a mediun")
  bill += 20
else:
  print(" that's a large")
  bill += 25

if add_pepperoni == "Y":
  bill += 3
else:
  bill +=0

if extra_cheese == "Y":
  print(" ohhh extra for extra fatty")
  bill += 1

print(f" your bill is {bill} ")   
