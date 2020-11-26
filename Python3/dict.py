def main():
    people = {'fname':'Muazam','lname':'Bhat'}
    for k in people.keys():
        print(k)

    for v in people.values():
        print(v)

    people['college'] = 'SRM' # adds 'college' : 'SRM' to the dictionary
    
    print_dict(people)

def print_dict(o):
    for x in o:
        print(f'{x}:{o[x]}')

if __name__ == '__main__':
    main()