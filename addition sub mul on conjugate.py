def main():
    real = float(input("Enter the real part: "))
    imag = float(input("Enter the imaginary part: "))
    complex_num = complex(real, imag)
    conjugate = complex_num.conjugate()
    addition = complex_num + conjugate
    subtraction = complex_num - conjugate
    multiplication = complex_num * conjugate
    print(f"Complex Number: {complex_num}")
    print(f"Conjugate: {conjugate}")
    print(f"Addition with Conjugate: {addition}")
    print(f"Subtraction with Conjugate: {subtraction}")
    print(f"Multiplication with Conjugate: {multiplication}")
if __name__ == "__main__":
    main()
