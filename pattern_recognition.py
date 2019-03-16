import re

class PatternRecognition(object):
    """ Generate a regex pattern based on a list of data """

    def __init__(self, data_list):
        # Initialize the needed vars.
        self.data = data_list
        self.current_pattern = ""
        self.matches = 0
        self.mismatches = 0
        self.pattern = ""
        self.message = False
        self.timeout_rounds = 0
        self.formatted_list = []

        # To help developers to use the library.
        self.status_code = 0

        # Analyse the data to recognize the pattern.
        for d in self.data:
            for l in d:
                # l => current value of a string row
                # Check if the current value is a digit
                if l.isdigit():
                    self.current_pattern += '\d'
                else:
                    self.current_pattern += l
        
            # Check if the current pattern matches with most of list of data.
            for c in self.data:
                if re.compile(r'^{}$'.format(self.current_pattern)).search(c):
                    self.matches += 1
                    self.formatted_list.append(f'{c}') 
                else:
                    self.mismatches += 1
                    self.formatted_list.append(f'{c} <== this is currupted')

            self.timeout_rounds += 1

            # If it matches most of them then this pattern is the final pattern.
            if self.matches > self.mismatches:
                self.pattern = self.current_pattern
                self.message = 'OK'
                self.status_code = 1 # 1 => the code that will make you happy :)

                # Sometimes if the dirty data comes as the first index the program will get confused in the beginning, so it will make another round until it gets the pattern, thats why it checks how many rounds it made so it can determine which message to show.
                if 8 > self.timeout_rounds > 1:
                    self.message = '''Because your first index of the data is dirty, the progam struggled a little to get the correct pattern, you may understand what happened when you use print_formatted_list(), but at the end the pattern was generated.'''
                    self.status_code = 2 # 2 => Pattern is generated but there is a warning message.

                # Stop searching further just to make the performance faster.
                break
                
            #  If there are a lot of mismatches, then the data is corrupted.
            else:
                self.pattern = ""
                self.message = 'most of the data is dirty'
                self.status_code = 5 # 5 => there is a problem in the data

            # Sometimes in some cases there are a lot of corrupted data which will make the program round looping in terms of rounds, this is like a timeout here.
            if self.timeout_rounds > 15:
                self.timeout_rounds = 0
                self.status_code = 5
                break
            self.current_pattern = ""

    def get_pattern(self):
        return f'r"^{self.pattern}$"'

    def print_formatted_list(self):
        for i, data in enumerate(self.formatted_list, 1):
            print(i, '=> ', data)
            
    def get_formatted_list(self):
        return self.formatted_list

    def get_matches(self):
        return self.matches
    
    def get_mismatches(self):
        return self.mismatches

    def get_message(self):
        return self.message

    def get_status_code(self):
        return self.status_code
