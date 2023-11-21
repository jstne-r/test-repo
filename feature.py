import datetime

# Get the current time
current_time = datetime.datetime.now()

# Extract the current hour
current_hour = current_time.hour

# Determine the appropriate greeting based on the current hour
if current_hour < 12:
    greeting = "Good morning!"
elif current_hour < 18:
    greeting = "Good afternoon!"
else:
    greeting = "Good evening!"

# Print the greeting
print(greeting)
