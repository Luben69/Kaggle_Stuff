from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex5 import *
print('Setup complete.')
# TODO: Edit the function
def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth

# Do not change: Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Do not change: Should return .036
print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7))

# Do not change: Check your answer
q5.check()