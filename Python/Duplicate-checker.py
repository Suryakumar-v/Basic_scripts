def compare_files(file_a, file_b, output_file):
    # Open and read the contents of file_a
    with open(file_a, 'r') as f_a:
        lines_a = set(f_a.readlines())  # Read all lines and store in a set

    # Open and read the contents of file_b
    with open(file_b, 'r') as f_b:
        lines_b = set(f_b.readlines())  # Read all lines and store in a set

    # Find lines in a but not in b
    diff_lines = lines_a - lines_b

    # Write the lines that are in file_a but not in file_b to the output file
    with open(output_file, 'w') as out_file:
        for line in diff_lines:
            out_file.write(line)  # Write each line to the output file

    print(f"The differing lines have been written to {output_file}")

# Example usage
file_a = 'file_a.txt'  # Replace with your file path
file_b = 'file_b.txt'  # Replace with your file path
output_file = 'output.txt'  # Output file where differing lines will be written
compare_files(file_a, file_b, output_file)
