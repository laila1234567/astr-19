import numpy as np

#Creating and printing the table of sin(x) vs. x
def generate_sin_table():
    #1000 points for x from 0 to 2pi
    x_values = np.linspace(0, 2 * np.pi, 1000)
    
    
    print("x (radians) sin(x)")
    print("-" * 30)

    #Finding sin(x) for each x value and printing the results
    for x in x_values:
        sin_x = np.sin(x)  
        print(x, sin_x) #Printing x and sin(x) 

# Main function
def main():
    generate_sin_table()

#Call the main function to run 
if __name__ == "__main__":
    main()
