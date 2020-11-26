def main():
    infile = open("cat.jpg",'rb')
    outfile = open("cat-copy.jpg",'wb')

    while True:
        buf = infile.read(10240) #buffer size = 10240 (10kb)
        if buf:
            outfile.write(buf)
            print('.',end='',flush=True)

        else:
            break
    outfile.close()
    print("\n done")

main()