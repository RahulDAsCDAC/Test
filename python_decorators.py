def outer_function(func):
    def wrapper(arg):
        res = func(arg)
        if isinstance(res, dict):
            print("Checked that the output is a dictionary")
            return res
    return wrapper

@outer_function
def give_dictionary(arg):
    return {"program": arg}

print(give_dictionary("python"))