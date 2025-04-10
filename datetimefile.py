# Import the 'datetime' module to work with date and time
import datetime
from time import tzname


# Get the current date and time
now = datetime.datetime.now()

# Create a datetime object representing the current date and time

# Display a message indicating what is being printed
# Print the current date and time in a specific format
print("Current date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))

print("time zone: ", tzname)