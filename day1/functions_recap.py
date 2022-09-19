import sys


def calculate_geometric_series(a, r, n=10):
    """Calculate the sum of a geometric series"""
    if r == 1:
        return a * (n + 1)
    return a * (1 - r ** (n + 1)) / (1 - r)

def get_max(a_list):
# In my code, I was evaluating all the values in the list, so I had to consider cases such as
# len(list == 0 and len(list)== 1
# In his case, he is just processing each value inside the list, so he skips all of that.
# He uses booleans to determine if he saw the first element or not.
    maximum = None
    first = False
    for value in a_list:
        if not first: # This loop works only for the first time.
            maximum = value
            first = True
        if value > maximum:
            maximum = value
    return maximum

def main():
    a = int(input("a: "))
    r = float(input("r: "))
    n = int(input("n: "))
    print(f"s_n = {calculate_geometric_series(a, r, n)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
