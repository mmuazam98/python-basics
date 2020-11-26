def main():
    # for i in range(10): prints 0-9
    # for i in inclusive_range(10): prints 0-10

    for i in inclusive_range(1,10,2):
        print(i, end=' ')
    print()
 
def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    if numargs < 1:
        raise TypeError(f'expected atleast 1 argument {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start,stop) = args
    elif numargs == 3:
        (start,stop,step) = args
    else:
        raise TypeError(f'expected atmost 3 arguments {numargs}')

    # generator 
    i = start
    while i<=stop:
        yield i
        i = i + step

if __name__ == "__main__":
    main()
          