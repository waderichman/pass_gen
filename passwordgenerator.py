import random
from collections import defaultdict

symbols = list("!@#$%&*123456789_")
passwords_dict = defaultdict(list)


# helper function to insert random values into string
def insert_str(keyword, str_to_insert, index):
    return keyword[:index] + str_to_insert + keyword[index:]


# arbitrary rank system to give values to passwords
def rank_password(password, keyword):
    value = 0.0
    for char in password:
        if char in symbols:  # if special characters are in
            value += 3
        else:
            value += 1
        if password.count(char) > 1:  # if duplicate symbols present
            value -= 4
        else:
            value -= 3
        if keyword in password:  # if the keyword is word for word in the password
            value -= 20
            break
        if password.find(keyword[:2]) != -1:
            value -= 3
        else:
            value += 3
        if password.find(keyword[1:3]) != -1:
            value -= 3
        else:
            value += 3
    if keyword[0:1] == password[0:1]:  # checks for matching first character
        value += 15
    else:
        value -= 15
    if keyword[len(keyword) - 1:len(keyword)] == password[len(password) - 1:len(
            password)]:  # checks for matching last character
        value += 15
    else:
        value -= 15

    return value


def generate_dict(keyword, length):
    spaces_to_fill = length - len(keyword)  # number of random characters to fill

    if len(keyword) >= length:
        return -1
    else:
        for x in range(100000):  # generates 100k passwords
            password = keyword
            for y in range(spaces_to_fill):
                random_int = random.randint(0, length - 1)  # random number between indices of password
                random_char = random.choice(symbols)  # random symbol
                password = insert_str(password, random_char, random_int)
            rank = rank_password(password, keyword)  # gets rank value
            passwords_dict[rank].append(password)  # loads password and rank into dictionary

        return passwords_dict

# def generate_list(keyword, length):
#     spaces_to_fill = length - len(keyword)
#     passwords_list = [[]]
#
#     if len(keyword) >= length:
#         return -1
#     else:
#         for x in range(100000):
#             password = keyword
#             for y in range(spaces_to_fill):
#                 random_int = random.randint(0, length - 1)
#                 random_char = random.choice(symbols)
#                 password = insert_str(password, random_char, random_int)
#             rank = rank_password(password, keyword)
#             passwords_list.append([rank, password])
#
#         return passwords_list
