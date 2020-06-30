session_dict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

star_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5
}


def convert_stars_to_num(stars):
    return star_dict[stars]


def convert_sessions_to_text(sessions):
    return session_dict[sessions]


if __name__ == "__main__":
    input_str = "I completed 2 sessions and I rated my expert five stars"
    input_str_lst = input_str.split(" ")
    number_of_sessions = convert_sessions_to_text(input_str_lst[2])
    number_of_stars = convert_stars_to_num(input_str_lst[-2])

    converted_format_str = "I completed {} sessions and I rated my expert {} stars"

    print("Original string : {}".format(input_str))
    print("Converted string: {}".format(converted_format_str.format(number_of_sessions, number_of_stars)))
