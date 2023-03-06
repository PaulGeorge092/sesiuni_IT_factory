class CustomException(Exception):
    pass

#sa se scrie ofunctie care verifica daca o lista de nr intrgi contine nr negative
# daca da sa se arunce o exceptie specifica

class ContainsNumberException(Exception):
    pass


def negative_numbers(numbers):
    for i in numbers:
        if i < 0:
            raise ContainsNumberException(f" il contine pe {i}")

negative_numbers([1,2,3,-6,-7])