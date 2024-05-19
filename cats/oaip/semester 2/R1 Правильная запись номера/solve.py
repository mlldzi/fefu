import re


def reading():
    with open("input.txt") as file:
        number = file.readline()
        return number


def writing(number):
    with open("output.txt", "w") as file:
        file.write(str(number))
        return number


def replace(number):
    number = re.sub(r'[()\-\s+]', ' ', number)
    number = re.sub(r'\s+', ' ', number)
    return number.strip()


def check_length(region_code, local_number):
    if len(region_code) == 3:
        local_number = f'{local_number[0:3]}-{local_number[3:5]}-{local_number[5:]}'
    elif len(region_code) == 4:
        local_number = f'{local_number[0:2]}-{local_number[2:4]}-{local_number[4:]}'
    elif len(region_code) == 5:
        local_number = f'{local_number[0]}-{local_number[1:3]}-{local_number[3:]}'
    else:
        local_number = f'{local_number[0:2]}-{local_number[2:]}'
    return f"+7 {region_code} {local_number}"


def main():
    number = reading()
    number = replace(number)
    number = number.split(' ')
    region_code = number[1]
    local_number = ''.join(number[2:])
    result = check_length(region_code, local_number)
    writing(result)


if __name__ == "__main__":
    main()
