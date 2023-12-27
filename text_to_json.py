import json

# Function to read a text file and convert it to a JSON file
def text_to_json(input_file, output_file):
    questions = []

    with open(input_file, 'r') as file:
        for line in file:
            # Remove leading and trailing whitespace from each line
            line = line.strip()
            if line:
                # Replace '\u2019' with a single quote
                line = line.replace('\u2019', "'")
                questions.append(line)

    data = {"questions": questions}

    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    import sys

    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python text_to_json.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert the text file to a JSON file
    try:
        text_to_json(input_file, output_file)
        print(f"Text converted to JSON and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)
