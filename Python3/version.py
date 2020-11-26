import platform

def main():
    message()

def message():
    print('This is version {}' . format( platform.python_version() ) )
    if True:
        print("true")
    else:
        print("false")    

if __name__ == "__main__":
    main()