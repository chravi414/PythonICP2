def string_alternate(text):
    output = ''
    for index, char in enumerate(text, start=1):
        if index % 2 != 0:
            output += char
    return output


if __name__ == "__main__":
    text = input('Enter the string :\n')
    result = string_alternate(text)
    print(result)
