import random
import array


def Pass_generator():

    # maximum length of password needed
    # this can be changed to suit your password length
    MAX_LEN = 15

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
            '*', '(', ')', '<']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
            password = password + x
            

    # Store the generated password
    with open('user_info/gen_pass.txt', 'w') as f:
        f.write(password)


def Pass_Checker():

    # A utility function to check
    # whether a password is valid or not
    def isValid(password):

        # for checking if password length
        # is between 8 and 15
        if (len(password) < 8 or len(password) > 15):
            return False

        # to check space
        if (" " in password):
            return False

        if (True):
            count = 0

            # check digits from 0 to 9
            arr = ['0', '1', '2', '3',
                '4', '5', '6', '7', '8', '9']

            for i in password:
                if i in arr:
                    count = 1
                    break

            if count == 0:
                return False

        # for special characters
        if True:
            count = 0

            arr = ['@', '#', '!', '~', '$', '%', '^',
                '&', '*', '(', ',', '-', '+', '/',
                ':', '.', ',', '<', '>', '?', '|']

            for i in password:
                if i in arr:
                    count = 1
                    break
            if count == 0:
                return False

        if True:
            count = 0

            # checking capital letters
            for i in range(65, 91):

                if chr(i) in password:
                    count = 1

            if (count == 0):
                return False

        if (True):
            count = 0

            # checking small letters
            for i in range(90, 123):

                if chr(i) in password:
                    count = 1

            if (count == 0):
                return False

        # if all conditions fails
        return True

    # Get the Password
    with open("user_info/input_password.txt") as f:
        in_pass = f.read()

    # Driver code
    password = in_pass
    if (isValid([i for i in password])):
        # Write user password in file
        with open("user_info/user_password.txt", "w") as f:
            f.write(password)
    
        # Write valid if it is
        with open("user_info/password_validty.txt", "w") as f:
            f.write('valid')

    else:
        # Write not valid if it is
        with open("user_info/password_validty.txt", "w") as f:
            f.write('not valid')

    return


if __name__ == '__main__':
    Pass_generator()
