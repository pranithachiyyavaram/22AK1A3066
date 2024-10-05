def classify_number(n):
    if n <= 0:
        return "Invalid input. Number must be greater than 0."
    divisors = [i for i in range(1, n) if n % i == 0]
    sum_of_divisors = sum(divisors)
    if sum_of_divisors > n:
        return "Abundant"
    elif sum_of_divisors < n:
        return "Deficient"
    else:
        return "Perfect"
def main():
    try:
        number = int(input("Enter a number: "))
        result = classify_number(number)
        print(f"The number {number} is {result}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    main()
