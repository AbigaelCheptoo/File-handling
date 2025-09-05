

def modify_content(content: str) -> str:
    
    return content.upper()


def main():
    
    input_filename = input("Enter the name of the file to read: ")

    try:
        e
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified = modify_content(content)

        # Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, "w") as outfile:
            outfile.write(modified)

        print(f"Modified content has been written to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()