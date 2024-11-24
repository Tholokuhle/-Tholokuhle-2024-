class NumberMachine:
    def __init__(self, number):
        self.number = number     #Initialize with a number or a given number
    
    def reverse_number(self):
        reversed_num = 0     # Initialize the reversed number to 0
        temp = self.number  
        while temp > 0:     # Loop until all digits are processed
            reversed_num = reversed_num * 10 + temp % 10   
            temp //= 10   
        return reversed_num
    
    def sum_of_digits(self):
        sum_digits = 0       # Initialize the sum of digits to 0
        temp = self.number  
        # Loop until all digits are processed
        while temp > 0:
            sum_digits += temp % 10
            temp //= 10
        return sum_digits
    
    def add_one_to_each_digit(self):
        new_number = 0
        temp = self.number
        multiplier = 1
        while temp > 0:
            digit = (temp % 10 + 1) % 10
            new_number = digit * multiplier + new_number
            multiplier *= 10
            temp //= 10
        return new_number

# Example usage
number = 12391
machine = NumberMachine(number)   # Create an instance of NumberMachine with the given number


reversed_num = machine.reverse_number()  # Reverse the number
sum_digits = machine.sum_of_digits()   # Calculate the sum of the digits
new_number = machine.add_one_to_each_digit()   # Generate a new number by adding one to each digit

# Print the results
print(f"Original number: {number}")
print(f"Reversed number: {reversed_num}")
print(f"Sum of digits: {sum_digits}")
print(f"New number with each digit incremented by one: {new_number}")