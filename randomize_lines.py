import random

# Function to randomize the lines of a text file
def randomize_lines(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        random.shuffle(lines)

    with open(input_file, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    import sys

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python randomize_lines.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Randomize the lines of the input file
    try:
        randomize_lines(input_file)
        print(f"Lines randomized and saved to {input_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)
