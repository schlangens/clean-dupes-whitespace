def clean_whitespace(text):
    # Remove duplicated whitespaces with a single whitespace
    cleaned_text = " ".join(text.split())
    return cleaned_text

def remove_duplicates(entries):
    # Use a set to remove duplicates while preserving order
    seen = set()
    unique_entries = []
    for entry in entries:
        if entry not in seen:
            seen.add(entry)
            unique_entries.append(entry)
    return unique_entries

def main():
    input_filename = 'input.txt'  # Replace 'input.txt' with your actual input file name
    output_filename = 'output.txt'  # The cleaned data will be saved here
    output2_filename = 'output2.txt'  # Additional cleaned data will be saved here

    with open(input_filename, 'r') as file:
        data = file.read()

    # Clean whitespace and remove duplicates from the input data
    cleaned_data = clean_whitespace(data)
    entries = cleaned_data.split()

    # Remove duplicates from the entries list
    unique_entries = remove_duplicates(entries)

    # Save the cleaned data without filtering to output2.txt with each entry on its own line
    with open(output2_filename, 'w') as file:
        file.write('\n'.join(unique_entries))

    # Save the cleaned data without filtering to output.txt
    with open(output_filename, 'w') as file:
        file.write(cleaned_data)

if __name__ == "__main__":
    main()
