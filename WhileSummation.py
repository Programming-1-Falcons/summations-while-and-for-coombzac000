user_number = int(input("Input a number: "))    
total_sum = 0  # Initialize total_sum to 0  
current_number = 1  # Start counting from 1  
  

while current_number <= user_number:    
    total_sum += current_number  
    current_number += 1  
   
print("The Sum of numbers 1 to", user_number, "is:", total_sum)  
