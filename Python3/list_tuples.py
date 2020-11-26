def main():
    # list 
    game = ['Football','Cricket','Volleyball','Badminton','Tennis','Soccer','Rugby','Swimming','Racing']

    # tuple - cannot be modified
    # game = ('Football','Cricket','Volleyball','Badminton','Tennis','Soccer','Rugby','Swimming','Racing')


    # access individual item
    print(game[1])

    #slice 
    print(game[1:3])

    # using step 
    print(game[1:4:2])

    # search a list 
    i = game.index('Tennis')
    print(game[i])

    # append items 
    game.append('Basketball')

    #insert at position 
    game.insert(0,'Hockey')

    # remove an item 
    game.remove('Basketball')

    #remove at end of the list
    game.pop()
    print(game)

    # remove particular item 
    game.pop(3)

    #delete from index 
    del game[3]

    # remove by slice
    del game[1:3]

    # join a list 
    print(', '.join(game))

    # get count 
    print(len(game))


    print(game)

if __name__ == "__main__":
    main()
