
def Ex14():
    initial_number = 3 # this number must be odd, cause if it's even n/2 create a longer chain
    max_chain = 0
    number_associated = 0
    while initial_number < 1000000:
        current_number = initial_number
        chain = 0
        while current_number != 1:
            if current_number%2 == 1: # Odd
                current_number = 3*current_number + 1
                chain += 1
            else:
                current_number = int(current_number/2)
                chain += 1
        if chain > max_chain:
            max_chain = chain
            number_associated = initial_number
        initial_number += 2
    return number_associated

print(Ex14())