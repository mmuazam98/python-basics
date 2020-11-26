def main():
    x = runMe()
    print(type(x),x)

def runMe():
    print("Hi")
    return dict(x='12',y=13)

if __name__ == '__main__':
    main()