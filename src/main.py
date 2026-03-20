from fast_module import fast_add  # this will be the pybind11 module

def main():
    a, b = 3, 5
    result = fast_add(a, b)
    print(f"{a} + {b} = {result}")

if __name__ == "__main__":
    main()