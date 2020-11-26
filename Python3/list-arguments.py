def main():
    people('Mohammad','Muazam','SRM-IST')

def people(*args):
    if len(args):
        for name in args:
          print(name)
    else: 
        print("nobody")

if __name__ == "__main__":
    main()