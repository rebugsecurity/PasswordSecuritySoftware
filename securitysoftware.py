import getpass
import re

# Let's define the password policy function

def validate_password(password):

    # Also create a regular expression for said password policy.
    regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    # now let's check whether the provided password(s) matches the policy provided.
    if re.match(regex, password):
        print("Password is strong!")
    else:
        print("Password is too weak, please make it stronger!")

# Get the user input for the password
password = getpass.getpass(prompt="Enter your password: ")

# Now call the password policy function to check the strength of the password provided.
validate_password(password)