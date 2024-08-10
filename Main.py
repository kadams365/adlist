import os
import re
import random

import test

# Define the directory containing your files
directory = 'adlists'
unfiltered_file = 'master.txt'
filtered_file = 'filtered_file.txt'


def get_unique_lines(directory, unfiltered_file):
    """Collect unique lines from all files in the directory and save them to unfiltered_file."""
    unique_lines = set()

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Ensure it's a file before reading
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    unique_lines.add(line.strip())

    # Write the unique lines to the output file
    with open(unfiltered_file, 'w', encoding='utf-8') as output:
        for line in sorted(unique_lines):
            output.write(line + '\n')

    print(f'Merged file created: {unfiltered_file}')


def randomly_delete_lines(input_file, output_file, keep_percentage):
    """Randomly delete lines from input_file based on keep_percentage and save to output_file."""
    if not (0 <= keep_percentage <= 100):
        raise ValueError("keep_percentage must be between 0 and 100")

    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    num_lines = len(lines)
    num_to_keep = int(num_lines * keep_percentage / 100)

    lines_to_keep = random.sample(lines, min(num_to_keep, len(lines)))

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(lines_to_keep)

    print(f'Randomly deleted lines. Processed file created: {output_file}')


def process_line(line):
    """Process each line to remove unwanted characters and content."""
    line = re.sub(r'[\[\]]', '', line)  # Remove square brackets
    line = line.replace('127.0.0.1', '')  # Remove specific IP address
    line = line.replace('0.0.0.0', '')  # Remove specific IP address
    line = line.replace('#', '')  # Remove hash symbol
    line = line.replace(' ', '')  # Remove spaces

    # Remove anything past the word 'Issue', including 'Issue'
    if 'Issue' in line:
        line = line.split('Issue')[0].strip()

    # Return the line if it contains a period
    if '.' in line:
        return line

    return None


def main():
    test.main()

    # Step 1: Get unique lines from files in the directory
    get_unique_lines(directory, unfiltered_file)

    # Step 2: Randomly delete lines from the generated file
    randomly_delete_lines('malware.txt', 'adlists/lite_malware.txt', 55)

    # Step 3: Process lines from the unfiltered file and write to filtered file
    with open(unfiltered_file, 'r', encoding='utf-8') as infile, open(filtered_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            processed_line = process_line(line.strip())
            if processed_line:
                outfile.write(processed_line + '\n')

    print(f'Filtered file created: {filtered_file}')


if __name__ == "__main__":
    main()
