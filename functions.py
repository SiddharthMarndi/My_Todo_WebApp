FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Reads the text file and returns a list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Writes the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__cli__":
    print("Hello")
    print(get_todos())
