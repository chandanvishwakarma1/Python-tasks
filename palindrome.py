
def check_palindrome(s: str): 
    # Normalize the string by removing non-alphanumeric characters and converting to lowercase 
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum()) 
    # Check if the cleaned string is equal to
    #  its reverse 
    if cleaned_string == cleaned_string[::-1]: 
        print("\nPalindrome") 
    else: print("\nNot Palindrome") 

str_input = input("\nEnter the string: ") 
check_palindrome(str_input)