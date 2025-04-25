n = int(input("Enter how many terms of the Fibonacci series you want to display: "))
a = 0
b = 1

for i in range(n) :
    print(a, end=" ")
    temp =  a + b # Calculate the sum and store it in a temporary variable
    a = b         # Update a with the value of b
    b = temp      # Update b with the sum (a + b)
    
    
   