# Get the limit from the user
limit = int(input("Enter a limit: "))

# Generate a list of even numbers up to the limit
even_numbers = [num for num in range(2, limit + 1, 2)]

# Display the list of even numbers
print("Even numbers up to", limit, "are:", even_numbers)
