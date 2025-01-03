import os

def get_path(__file__):
    """Return the path of the file."""
    import pdb; pdb.set_trace()
    head, tail = os.path.split(__file__)
    for char in tail:
        pass #check __file__ char
    return head

    filename = fname
    filename_path =get_path(filename)
    print(f'path = {filename_path}')