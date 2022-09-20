import random


def reading_wagata():
    with open("wagata.txt", encoding = "utf-32") as f:
        print(f.read())

#reading_wagata()

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

# print_to_1000()


def parsing_text_files():
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:   # gene transfer sormat, is a text-based and tab-delimited file format.
        for row in f:  # files are iterators
            print(row.strip())  # remove trailing \n
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:
            cols = row.strip().split("\t")
            print(cols)

#parsing_text_files()

x = """In the example on writing lines the resulting file has all lines merged into one. 
Write a function that creates the file from scratch but writes each line to a row."""
def writing_to_text_files():
    lines_of_text = [
        "Knowledge is power.",
        "Power to do evil... or power to do good.",
        "Power itself is not evil.",
        "So knowledge itself is not evil.",
        "― Veronica Roth, Allegiant",
    ]
    with open("power_quote.txt", 'w') as f:
        for each in lines_of_text:   # You can use map() as well!
            f.write(each + "\n")
    with open("power_quote.txt") as f:
        print(f.readlines())

# writing_to_text_files()

x = "create a directory into day2/dir1/dir3 called dir5 and insert a file with some random text"
def create_new_directory_with_random_txt():
    import pathlib
    my_path = pathlib.Path("dir1/dir3/dir5")
    # print("smthing")
    print(f"{str(my_path.absolute()):{100}}: {my_path.exists() = }")
    if my_path.exists() == False:
        my_path.parent.mkdir()
    else:
        print("It already exists")
    with open("dir1/dir3/dir5/task2_file.txt", 'w') as f:
        f.write("Screaming cowboys floating in the sky are watching you")

# create_new_directory_with_random_txt()

x = "write a function to parse the GTF file for Homo sapiens ab initio. Exclude header rows (start with #), filter exons only, add extra col for exon size"

def third_task_function():
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:
            if row.startswith("#"):
                continue
            cols = row.strip().split("\t")
            if cols[2] != "exon":
                continue
            cols.append(int(cols[4]) - int(cols[3]))
            print(cols)

# third_task_function()

def third_task_functionv2():  # This should be a bit more efficient, computationally speaking, because I am not splitting right away, but removing the strings without "exon".
    # Technically, this should save me some time, if I am right. Would be interesting to check the execution time and compare.
    with open("Homo_sapiens.GRCh38.107.abinitio.gtf") as f:
        for row in f:
            if row.startswith("#"):
                continue
            if "exon" not in row:
                continue
            cols = row.strip().split("\t")
            cols.append(int(cols[4]) - int(cols[3]))
            print(cols)

# third_task_functionv2()


def troubleshoot_task():
    data = range(10)
    with open("file.txt", "w") as f:
        for d in data:
            f.write(str(d) + "\n")

# troubleshoot_task()

x = """You are provided with fully annotated GTF file Homo_sapiens.GRCh38.107.shuffled_and_truncated.gtf. 
Write a function for each of the following analyses:
split into separate files by chromosome [DONE]
aggregate by gene_id or transcript_id (choose one or both)
compile exons for gene_id or transcript_id and find the longest gene/transcript by exon length and by number of exons"""

def split_by_chromosome():
    with open("Homo_sapiens.GRCh38.107.shuffled_and_truncated.gtf") as f:
        ch_set = set()
        cols_list = []
        for row in f:
            cols = row.strip().split("\t")
            ch_set.add(cols[0])
            cols_list.append(cols)
        for each in ch_set:
            # create file with name of chromosome here
            name = "dir1/dir3/dir5/" + each + ".txt"
            with open(name, 'w') as f:
                for every in cols_list:
                    if each == every[0]:
                        # append every to file with chrome name here
                        f.write(str(every) + "\n")


#split_by_chromosome()

def zip_zap_zop():
    import gzip    # BELOW: open the original fine, then create the compressed file. For every line of the original, compress it and write it to the compressed file.
    with open ("/home/gionmattia/Desktop/code-fastfoundations/day2/Homo_sapiens.GRCh38.107.shuffled_and_truncated.gtf") as f, gzip.open("Homo_sapiens.GRCh38.107.shuffled_and_truncated.gz", "wb") as g:
        for rows in f:
            g.write(rows.encode("utf-8"))

# zip_zap_zop()

x = "Write a function to write a stream of 1000 random integers between 0 and 200 followed by 1000 random floating between 0 and 1 to a file."

def random_numbers():
    import random
    numbs = []
    for each in range(1000):
        numbs.append(random.randint(0,200))
    for each in range(1000):
        numbs.append(1/random.randint(1,200))
    print(numbs)

# random_numbers()
def find_it():
    import subprocess
    import shlex
    process = subprocess.run(shlex.split("find . -name ‘*paradoxical.*’ -type f"))
    print(f"{process = }")
    print(f"{process.returncode = }")

# find_it()

map()