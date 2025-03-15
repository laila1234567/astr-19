import math

def print_sin_table():
    x_values = [i * (2 / 999) for i in range(1000)] 

    print(f"{'x':<10}{'sin(x)'}")
    print("-" * 20)
    
    #looping through the x values and calculating sin(x)
    for x in x_values:
        sin_x = math.sin(x)
        print(f"{x:<10.5f}{sin_x:.5f}")

def main():
    print_sin_table()

if __name__ == "__main__":
    main()
