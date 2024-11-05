user_number = int(input("Input a number: "))    
total_sum = 0  # Initialize total_sum to 0  
    
for current_number in range(1, user_number + 1):    
    total_sum += current_number  
  
print("The Sum of numbers 1 to", user_number, "is:", total_sum)  
