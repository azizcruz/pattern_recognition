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
        self.digit_pattern = ''
        self.repeated_times = 0

        # To help developers to use the library.
        self.status_code = 0

        # Analyse the data to recognize the pattern.
        self.analyse_pattern()


    def analyse_pattern(self):
        for d in self.data:
            for l in d:
                # l => current value of a string row
                # Check if the current value is a digit
                self.predict_the_current_character(l)

            self.current_pattern += self.digit_pattern
            self.digit_pattern = ''
        
            # Check if the current pattern matches with most of the list of data.
            for c in self.data:
                self.compare_current_string_with_current_pattern(c)
                
                # This will solve the bug if the dirty data comes first in the data list.
                if self.mismatches == len(self.data) - 1:
                    self.formatted_list = []
                    self.mismatches = 0
                    self.matches = 0
                    

            # Increase rounds of comparing
            self.timeout_rounds += 1

            # If it matches most of them then this pattern is the final pattern.
            if self.matches > self.mismatches:
                self.pattern = self.current_pattern
                self.message = 'OK'
                self.status_code = 1 # 1 => the code that will make you happy :)

                # Stop searching further to make the performance faster.
                break
                
            #  If there are a lot of mismatches, then the data is corrupted.
            else:
                self.pattern = ""
                self.message = 'Data is dirty.'
                self.status_code = 5 # 5 => there is a problem in the data

            # Sometimes in some cases there are a lot of corrupted data which will make the program round looping in terms of rounds, this is like a timeout here.
            if self.timeout_rounds > 15:
                self.timeout_rounds = 0
                self.message = 'Too much dirty data'
                self.status_code = 5
                break
            self.current_pattern = ''

    def compare_current_string_with_current_pattern(self, c):
        if re.compile(r'^{}$'.format(self.current_pattern)).search(c):
            self.matches += 1
            self.formatted_list.append(f'{c}') 
        else:
            self.mismatches += 1
            self.formatted_list.append(f'{c} <== this is currupted')

    def predict_the_current_character(self, l):
        if l.isdigit():
            self.repeated_times += 1
            self.digit_pattern = '\d{' + str(self.repeated_times) + '}'
        else:
            # Check if the previous element of the string was a digit and it was repeated then write the pattern with how many times it was repeated
            if self.repeated_times > 0:
                self.current_pattern += self.digit_pattern
                self.repeated_times = 0
                self.digit_pattern = ''
            
            # if it is not a digit just concatinate the string letter.
            self.current_pattern += l

    def get_pattern(self):
        print(self.timeout_rounds)
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
