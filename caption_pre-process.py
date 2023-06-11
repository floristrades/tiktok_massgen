import re

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Strip lines starting with a number (including 0) and remove empty lines
    lines = [line.strip() for line in lines if not re.match(r'^\d', line.strip()) and line.strip()]

    with open(output_file, 'w') as file:
        file.write('\n'.join(lines))

    print("Processing complete. Stripped lines have been saved to", output_file)



# Example usage
input_filename = r'.\captions\raw_captions\1.txt'  # Replace with your input file name
output_filename = r'.\captions\processed_captions\1.txt'  # Replace with your output file name

process_file(input_filename, output_filename)
