

# -----------------------------
# 1. Check whitespace in input
# -----------------------------
text = input("Enter a sentence or word: ")

if " " in text:
    print("Whitespace found")
else:
    print("No whitespace found")


# -----------------------------
# 2. Items, price and discount
# -----------------------------
item1 = input("Enter item 1: ")
price1 = float(input("Enter price of item 1: "))

item2 = input("Enter item 2: ")
price2 = float(input("Enter price of item 2: "))

discount = float(input("Enter discount (%): "))

total = price1 + price2
discount_amount = (discount / 100) * total
final_bill = total - discount_amount

print("Total price:", total)
print("Discount amount:", discount_amount)
print("Final bill to pay:", final_bill)


# -----------------------------
# 3. Email domain check
# -----------------------------
email = input("Enter your email: ")

if email.endswith(".pk"):
    print("Pakistani domain")
else:
    print("Other domain")


# -----------------------------
# 4. Remove max and min (6 numbers)
# -----------------------------
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
n5 = int(input("Enter number 5: "))
n6 = int(input("Enter number 6: "))

largest = n1
smallest = n1

if n2 > largest:
    largest = n2
if n3 > largest:
    largest = n3
if n4 > largest:
    largest = n4
if n5 > largest:
    largest = n5
if n6 > largest:
    largest = n6

if n2 < smallest:
    smallest = n2
if n3 < smallest:
    smallest = n3
if n4 < smallest:
    smallest = n4
if n5 < smallest:
    smallest = n5
if n6 < smallest:
    smallest = n6

print("Largest number:", largest)
print("Smallest number:", smallest)


# -----------------------------
# 5. Marks, percentage, grade
# -----------------------------
marks1 = float(input("Enter marks of subject 1: "))
marks2 = float(input("Enter marks of subject 2: "))
marks3 = float(input("Enter marks of subject 3: "))

total = marks1 + marks2 + marks3
percentage = (total / 300) * 100

print("Percentage:", percentage)

if percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")
