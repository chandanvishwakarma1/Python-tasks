def count_words(input_file: str, output_file: str):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
        
        # Split the text into words and count them
        word_count = len(text.split())
        
        with open(output_file, 'w') as file:
            file.write(f'The number of words in the file is: {word_count}')
        
        print(f'Word count written to {output_file}')
    
    except FileNotFoundError:
        print(f'The file {input_file} does not exist.')

# Example usage
input_file = r'files-fileHandling\input.txt'
output_file = r'files-fileHandling\output.txt'
count_words(input_file, output_file)
