def main():
    # sets do not allow duplicate elements
    a = set("We're gonna learn Python")
    b = set("Python is very difficult")

    print_set(a) #diff value everytime
    print_set(sorted(b)) #same result everytime

    print_set(a - b) #prints elements not available in both

def print_set(o):
    print('{',end='')
    for x in o:
        print(x,end='')
    print('}')

if __name__ == "__main__":main()