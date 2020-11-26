def main():
    # try:
    #     x = int("Hello")
    # except:
    #     print("ERROR: Don't add string to int")
    try:
        x = 5/0
    except ValueError:
        print("ERROR")
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except:
        print("Unknown error")
    else:
        print(x)

main()