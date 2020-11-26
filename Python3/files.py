def main():
    f = open('lines.txt','r') #read only
    # for line in f:
    #     print(line.rstrip())


    # f = open('lines.txt','w') write only (empties file)
    # f = open('lines.txt','a') appends the data i file
    # f = open('lines.txt','r+') optional + to read or write
    

    infile = open('lines.txt','rt')
    outfile = open('lines-copy.txt','wt')   
    for line in infile:
        print(line.rstrip(), file = outfile) 
        print('.',end='',flush=True)

    outfile.close()
    print('\ndone')


main()