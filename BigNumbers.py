print("Please enter four integers of your choice :")
 
# Use a loop to get the numbers
for i in range(1, 5):
    num = int(input(f"Enter number {i}: "))
    
total = sum(numbers)

# Calculate the average
average = total / 4

# Calculate the product
product = 1
for num in numbers:
    product *= num

print("Sum:", total)
print("Average:", average)
print("Product:", product)
