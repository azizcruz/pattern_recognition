from pdb import set_trace
from pattern_recognition import PatternRecognition

data = [
"hjsuua",
  "A-1012331/14",
  "A-1231141/22",
  "A-1231141/12",
  "A-1233441/23",
  "s-1231141/11" # <-- This ID might be considered erroneous.
]

pr = PatternRecognition(data)

print(pr.get_message())
print(pr.get_pattern())
print(pr.get_status_code())
print(pr.get_mismatches())
