def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")
        
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            # Read the content of the file
            content = infile.readlines()
        
        # Modify the content (e.g., add line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
        
        # Ask the user for the output filename
        output_filename = input("Enter the name of the file to write to: ")
        
        # Open the output file for writing
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    read_and_write_file()
