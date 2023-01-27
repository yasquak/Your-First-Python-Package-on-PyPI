# Definition to get solution to programming exercises

# Record of Revisions
#
# Date            Programmers                         Descriptions of Change
# ====         ================                       ======================

# 27-Jan-23     Yasminh Quak                               Original code

# Modules
import warnings

# Definition


def cheat(exercise):
    """
    CHEAT tells the user the solution to one of the PIPS assignments
    :param exercise: the question the user wants a solution for
    :return: solution of input exercise
    """
    if exercise not in ["1.2P.1", "1.2P.2", "1.2P.3", "1.2P.4"]:
        warnings.warn("Input should be of format 1.2P.x with x in range 1:4")
    if exercise == "1.2P.1":
        print("array_of_zeros = np.zeros((2, 4, 6))")
    if exercise == "1.2P.2":
        print("another_array = np.zeros((2, 4, 6))")
        print("print(another_array[-1, :, :],  # Return the last element of the first dimension")
        print("another_array[:, 0, :],  # Return the first element of the second dimension")
        print("another_array[:, :, 2])")
    if exercise == "1.2P.3":
        print("another_array = np.zeros((2, 4, 6))")
        print("new_array = another_array.copy()")
        print("new_array[1, 2, 2] = 1")
        print("print(another_array[1, 2, 2])  # Check if another_array was not changed with new_array")
        print("print(new_array[1, 2, 2])")
        print("# By equating new_array to another_array, when new_array was changed,")
        print("# another_array was changed in the same way. That is, because the newly")
        print("# created new_array shares the reference of the original another_array.")
        print("# This is different from R, where new_array would have merely been")
        print("# assigned the current values of another_array, after which both arrays")
        print("# would have been two independent objects (if you change one, the other")
        print("# remains unchanged).")
    if exercise == "1.2P.4":
        print("# The %paste does not work in a python script,")
        print("# because magic commands are build into the iPython kernel")
        print("# and can thus only be used in a iPython environment such as the iPython terminal")
