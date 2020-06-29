from enums import Session
from error import InvalidValueException 


class Step:
    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def make_step(self):
        try:
            number_of_sessions = Session.NUMBER_TO_TEXT_MAP[self.number_of_sessions]
            number_of_stars = Session.TEXT_TO_NUMBER_MAP[self.number_of_stars]
            output_str = 'I completed %s sessions and I rated my expert %d stars' \
                         % (number_of_sessions, number_of_stars)
            return output_str
        except KeyError as e:
            if isinstance(e.args[0], int):
                return InvalidValueException("Invalid number of sessions")
            elif isinstance(e.args[0], str):
                return InvalidValueException("Invalid number of stars")
