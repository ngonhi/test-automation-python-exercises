from .enums import Session


class Step:
    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = Session.NUMBER_TO_TEXT_MAP(number_of_sessions)
        self.number_of_stars = Session.TEXT_TO_NUMBER_MAP(number_of_stars)

    def make_step(self):
        output_str = 'I completed %s sessions and I rated my expert %d stars' \
                        % (self.number_of_sessions, self.number_of_stars)
        return output_str
