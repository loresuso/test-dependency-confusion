def create_file(f):
    """
    Create a file
    """
    with open(f, "w") as file:
        file.write("Hello, World!")