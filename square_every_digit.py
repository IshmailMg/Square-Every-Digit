def square_digits(num):
    # initialised an empty string
    result = ""
    #looped through a string number
    for number in str(num):
        result += str(int(number) ** 2)
    return int(result)