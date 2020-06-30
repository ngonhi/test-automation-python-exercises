from enums import Session
from error import InvalidValueException


class Step:
    def __init__(self, number_of_sessions, number_of_stars):
        try:
            self.number_of_sessions = Session.NUMBER_TO_TEXT_MAP[number_of_sessions]
        except KeyError:
            raise InvalidValueException("Invalid number of sessions")

        try:
            self.number_of_stars = Session.TEXT_TO_NUMBER_MAP[number_of_stars]
        except KeyError:
            raise InvalidValueException("Invalid number of stars")

    def make_step(self):
        output_str = "I completed {} sessions and I rated my expert {} stars" \
                     .format(self.number_of_sessions, self.number_of_stars)
        return output_str
