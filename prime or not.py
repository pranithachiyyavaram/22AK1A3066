def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def next_palindrome(num):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    num += 1  # Start checking from the next number
    while not is_palindrome(num):
        num += 1
    return num
def main():
    try:
        number = int(input("Enter a number: "))
        if is_prime(number):
            print(f"Next palindrome after {number} is {next_palindrome(number)}")
        else:
            print("Not prime")
    except ValueError:
        print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    main()
