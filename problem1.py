session_dict = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

star_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
}


# Convert number of stars from text to number
def text_to_num(stars):
    return star_dict[stars]


# Convert number of sessions from number to text
def num_to_text(sessions):
    return session_dict[sessions]


if __name__ == "__main__":
    input_str = 'I completed 2 sessions and I rated my expert five stars'
    input_str_lst = input_str.split(' ')
    number_of_sessions = num_to_text(input_str_lst[2])
    number_of_stars = text_to_num(input_str_lst[-2])

    converted_str = 'I completed %s sessions and I rated my expert %ds stars'


    print('Original string : %s' % input_str)
    print('Converted string: %s' % converted_str
          % (number_of_sessions, number_of_stars))



