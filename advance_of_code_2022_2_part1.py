""" 
The goal of this program is to count the amount of valid password in passwords.txt.
The password file is designed as such: each line contains a password policy and a corresponding password.
A password is valid if it respects the given password policy.

Here is how the password policy works: in each password policy there is a target letter and two numbers,
the amount of appearance of the target letter must be higher or equal than the first number and lower or
equal than the second number.

Strategy : 
1) Explore each line of the file 
2) For each line, parse the line to extract the password policy and the given password
3) Fill up the variables : minimum_appearance, maximum_appearance, target letter and password using the results of the parsing
4) Explore the password, if the target letter appears more then maximum_appearance times then reject, else after exploring the
password, if the target letter appears less then minimum_appearance then reject else increase nb_valid_pwd.
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
    minimum_appearance = int(partition[0])
    subline = partition[2]

    # Extract maximum_appearance
    partition = subline.partition(" ")
    maximum_appearance = int(partition[0])
    subline = partition[2]

    # Extract target_letter and password
    partition = subline.partition(": ")
    target_letter = partition[0]
    password = partition[2]

    return minimum_appearance, maximum_appearance, target_letter, password

def is_valid_password(minimum_appearance,maximum_appearance,target_letter,password):
    """
    Return true if the password respects the password policy
    """
    #Initialize target appearance counter and character_index counter and to_much_appearance boolean
    target_appearance = 0
    character_index = 0
    to_much_appearance = False
    # Explore the password until the target_letter is counted to much times or we reach the end of the string
    while not(to_much_appearance or character_index == len(password)):
        # If the studied letter is the target letter increase the appearance counter and check if the target appeared to often
        if target_letter == password[character_index]:
            target_appearance += 1
            to_much_appearance = target_appearance > maximum_appearance
        # Then increase the character_index to go to the next letter
        character_index += 1
    # Finaly return true if the target letter appeared at least minimum_appearance times and not to often
    return not(to_much_appearance) and target_appearance >= minimum_appearance

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
        minimum_appearance,maximum_appearance,target_letter,password = parse_and_store(line)

        # Test if the password is valid
        if is_valid_password(minimum_appearance,maximum_appearance,target_letter,password):
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