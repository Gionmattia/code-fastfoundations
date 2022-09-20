def reading_wagata():
    with open("wagata.txt", encoding = "utf-32") as f:
        print(f.read())

reading_wagata()

def print_number_rows(file_name, n):
    with open(file_name) as f:
        readlines = f.readlines()  # select something, then left click, refactor and "introduce variable"
        print(readlines[:n + 1])

#print_number_rows("paradoxical.txt", 100)

def print_to_1000():
    i = -12
    sum = 0
    while True:
        print(sum)
        sum += i
        if sum > 1000:
            break
        i += 1

print_to_1000()



