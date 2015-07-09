import logging

logging.basicConfig(filename='starter.log', level=logging.DEBUG)
# levels: Critical = 50, error = 40, warning = 30, info = 20, debug = 10, notset = 0

# Add a docstring to Treehouse.student.
# It should say "Gives a pleasant message about the student."

class Treehouse:
    def student(self, name):
        """Gives a pleasant message about the student."""
        return '{} is a great Treehouse student!'.format(name)
