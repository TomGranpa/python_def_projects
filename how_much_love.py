def how_much_i_love_you(nb_petals):
    love = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    return love[(nb_petals-1)%len(love)]

print (how_much_i_love_you(8))