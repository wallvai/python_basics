import unicodecsv 
from datetime import datetime as dt

with open("enrollments.csv", "rb") as file:
  reader = unicodecsv.DictReader(file)
  
