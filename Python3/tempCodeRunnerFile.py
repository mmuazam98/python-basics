def main():
    # sets do not allow duplicate elements
    a = set("We're gonna learn Python")
    b = set("python is very difficult")

    print_set(a)
    print_set(b)

    # print_set(a - b)

def print_set(o):
    print('{',end='')
    for x in o:
        print(x,end='')
    print('}')

if __name__ == "__main__":main()