# Number Machine

This project implements a number machine that performs three transformations on a five-digit number:
1. Reverses the number.
2. Calculates the sum of its digits.
3. Generates a new number by adding one to each of its digits.

## Features

- Reverse a five-digit number.
- Calculate the sum of the digits of a five-digit number.
- Generate a new number by adding one to each digit of a five-digit number.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/-Tholokuhle-2024-/project-4.git
    ```
2. Navigate to the project directory:
    ```sh
    cd project-4
    ```

## Usage

### Example Code

Here's an example of how to use the `NumberMachine` class:

```python
class NumberMachine:
    def __init__(self, number):
        self.number = number  # Initialize with a given number
    
    def reverse_number(self):
        reversed_num = 0  # Initialize the reversed number to 0
        temp = self.number
        while temp > 0:  # Loop until all digits are processed
            reversed_num = reversed_num * 10 + temp % 10
            temp //= 10
        return reversed_num
    
    def sum_of_digits(self):
        sum_digits = 0  # Initialize the sum of digits to 0
        temp = self.number
        while temp > 0:  # Loop until all digits are processed
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
machine = NumberMachine(number)  # Create an instance of NumberMachine with the given number

reversed_num = machine.reverse_number()  # Reverse the number
sum_digits = machine.sum_of_digits()  # Calculate the sum of the digits
new_number = machine.add_one_to_each_digit()  # Generate a new number by adding one to each digit

# Print the results
print(f"Original number: {number}")
print(f"Reversed number: {reversed_num}")
print(f"Sum of digits: {sum_digits}")
print(f"New number with each digit incremented by one: {new_number}")
```

### Steps to Run

1. **Initialize the Class**: Create an instance of the `NumberMachine` class with a five-digit number.
    ```python
    machine = NumberMachine(12391)
    ```
2. **Reverse the Number**: Call the `reverse_number` method to reverse the number.
    ```python
    reversed_num = machine.reverse_number()
    print(f"Reversed number: {reversed_num}")
    ```
3. **Sum of Digits**: Call the `sum_of_digits` method to calculate the sum of the digits.
    ```python
    sum_digits = machine.sum_of_digits()
    print(f"Sum of digits: {sum_digits}")
    ```
4. **Add One to Each Digit**: Call the `add_one_to_each_digit` method to generate a new number by adding one to each digit.
    ```python
    new_number = machine.add_one_to_each_digit()
    print(f"New number with each digit incremented by one: {new_number}")
    ```

## Customization

- **Change Input Number**: You can change the input number by passing a different five-digit number when initializing the class.
    ```python
    machine = NumberMachine(54321)
    ```