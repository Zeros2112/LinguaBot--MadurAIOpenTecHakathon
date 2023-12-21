def flatten(matrix):
    # Initialize an empty list to store the flattened elements of the matrix
    flat_list = []

    # Iterate over each row in the matrix
    for row in matrix:
        # Extend the flat_list with the elements of the current row
        flat_list += row

    # Return the flattened list
    return flat_list
