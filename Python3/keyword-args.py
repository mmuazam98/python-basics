def main():
    x= dict(fname='Mohammad',lname='Muazam',college='SRM-IST')
    people(**x)

def people(**kwargs):
    if len(kwargs):
        for name in kwargs:
          print(f'{name} says {kwargs[name]}')
    else: 
        print("nobody")

if __name__ == "__main__":
    main()