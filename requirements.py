input_file_path = "code.py"
output_file_path = "requirements.txt"

with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    for line in input_file:
        if "import" in line:
            output_file.write(line)

print(f"Lines containing 'import' have been saved to {output_file_path}")