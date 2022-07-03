def add(a, b):
    return  a+b;


def main():
    a = int(input("Enter the first number: "));
    b = int(input("Enter the second number: "));
    c = add(a, b);
    print(f"The sum of {a} and {b} is {c}");

if __name__ == "__main__":
    main()