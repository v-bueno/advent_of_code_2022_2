""" 
The goal of this program is to count the amount of valid password in passwords.txt.
The password file is designed as such: each line contains a password policy and a corresponding password.
A password is valid if it respects the given password policy.

Here is how the password policy works: in each password policy there is a target letter and two numbers,
the target letter must appeat at EXACTLY one of both number positions in the password.
/!\ The character numbers start from one in the password policy not from zero meaning 1 in "Hello" is 'H' not 'e'

Strategy : 
1) Explore each line of the file 
2) For each line, parse the line to extract the password policy and the given password
3) Fill up the variables : minimum_appearance, maximum_appearance, target letter and password using the results of the parsing
4) Check both positions in the password and increase nb_valid_pwd if exactly one of the position contains the target letter.
5) Go to next line.

Result : 
Print the number of valid passwords in the file.
"""

def open_password_file():
    password_file = open("passwords.txt","r")
    print(password_file)
    return password_file

def close_password_file(password_file):
    password_file.close()

def parse_and_store(line):
    """
    The format of a line is as follow : minimum_appearance-maximum_appearance target_letter: password
    """
    # Extract minimum_appearance
    partition = line.partition("-")
    first_index = int(partition[0])
    subline = partition[2]

    # Extract maximum_appearance
    partition = subline.partition(" ")
    second_index = int(partition[0])
    subline = partition[2]

    # Extract target_letter and password
    partition = subline.partition(": ")
    target_letter = partition[0]
    password = partition[2]

    return first_index, second_index, target_letter, password

def is_valid_password(first_index,second_index,target_letter,password):
    """
    Return true if the password respects the password policy
    /!\ Indexes are given starting from 1 not 0
    """
    if target_letter == password[first_index-1]:
        # If the first index contains the target letter then return True if the second index doesn't
        is_valid = target_letter != password[second_index-1]
    else :
        # If the first index doesn't contain the target letter then return True id the second index does contain the target
        is_valid = target_letter == password[second_index-1]
        
    return is_valid

def main():
    # First open the file
    password_file = open_password_file()
    
    # Read the first line
    line = password_file.readline()

    # Initialise the counter for valid passwords
    nb_valid_pwd = 0

    # Loop on the lines until line is an empty string, when EOF is reached, readline returns an empty string
    # We can use this as we know the file password.txt has no empty line so the only empty string we will get is EOF
    while line != "":
        # First parse and fill minimum_appearance, maximum_appearance, target_letter and password
        first_index,second_index,target_letter,password = parse_and_store(line)

        # Test if the password is valid
        if is_valid_password(first_index,second_index,target_letter,password):
            # If the password is valid increment nb_valid_pwd
            nb_valid_pwd += 1
        else:
            print ("Following line is not a valid password :",line)

        # Go to the next line
        line = password_file.readline()

    #Finally close the file
    close_password_file(password_file)

    print("There are : ",nb_valid_pwd," valid passwords.")
    return nb_valid_pwd

if __name__ == "__main__":
    main()