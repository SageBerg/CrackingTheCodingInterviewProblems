def master_mind(board, guess):
    hits = 0
    pseudo_hits = 0
    board_with_no_hits = ""
    guess_with_no_hits = ""

    #record hits
    for i in range(min(len(board), len(guess))):
        if board[i] == guess[i]:
            hits += 1
        else:
            board_with_no_hits += board[i]
            guess_with_no_hits += guess[i]

    #record pseudo hits
    frequencies = dict()
    for letter in board_with_no_hits:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    for letter in guess_with_no_hits:
        if letter in frequencies and frequencies[letter] > 0:
            frequencies[letter] -= 1
            pseudo_hits += 1

    return (hits, pseudo_hits)

   
def main():
    results = master_mind("RGBY", "GGRR")
    print "hits: " + str(results[0])
    print "pseudo hits: " + str(results[1])

    results = master_mind("YYBB", "BBYY")
    print "hits: " + str(results[0])
    print "pseudo hits: " + str(results[1])


main()
