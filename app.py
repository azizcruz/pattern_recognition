from PatternRecognition import PatternRecognition

data = [
  "A-1012331/9",
  "A-1231141/2",
  "A-1291141/4",
  "A-1533441/2",
  "S-1231141/11"  # <-- This ID might be considered erroneous.
  "A-1012331/1",
  "A-1237141/7",  
 ]

pr = PatternRecognition(data)

# Available methods.
# pr.get_pattern() => to get the predicted pattern.
# pr.get_formatted_list() => to get the current list. (returns a list)
# pr.print_formatted_list() => to print the whole list of data with showing where the data is dirty.
# pr.get_matches() => to print total number of matches with the pattern in the list. (still need some optimizations)
# pr.get_mismatches() => same as get_matches(), instead it returns mismatches.
# pr.get_message() => returns a message that display if everything is fine.
# pr.get_status() => returns a number [1 => list is ok, 5 => list is corrupted]

print(pr.get_pattern())
