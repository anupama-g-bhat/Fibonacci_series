import matplotlib.pyplot as plt

n = int(input("Enter how many terms of the Fibonacci series you want to display: "))
a = 0
b = 1
fib_numbers = []

for i in range(n) :
    print(a, end=" ")
    fib_numbers.append(a)
    temp =  a + b # Calculate the sum and store it in a temporary variable
    a = b         # Update a with the value of b
    b = temp      # Update b with the sum (a + b)

# creating x_axis value
x = list(range(n))

#Visualization 
plt.scatter(x,fib_numbers, c="blue")
plt.title("Scatter Plot of Fibonacci Series")
plt.xlabel('Index')
plt.ylabel('Fibonacci Numbers')
plt.show()
    
   
