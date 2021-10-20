board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def printBoard(bd):
    for row in range(len(bd)):
        if row!= 0:
            print('\n')
        for col in range(len(bd[0])):
            if col!= 0:
                print('|',end='')
            if col == len(bd):
                print(col)
            else:
                print(f'  {bd[row][col]}   ',end='')
    return ''


def takePosition(num):
    position_x = int(input(f'Player {num} choose a position on the row: '))
    position_y = int(input(f'Player {num} choose a position on the column: '))
    return (position_x, position_y)

def checkResult(bd,symbol):
    if bd[0][0] == bd[0][1] == bd[0][2] == symbol[0] \
    or bd[0][0] == bd[1][0] == bd[2][0] == symbol[0] \
    or bd[0][1] == bd[1][1] == bd[2][1] == symbol[0] \
    or bd[0][2] == bd[1][2] == bd[2][2] == symbol[0] \
    or bd[2][0] == bd[2][1] == bd[2][2] == symbol[0] \
    or bd[1][0] == bd[1][1] == bd[1][2] == symbol[0] \
    or bd[0][0] == bd[1][1] == bd[2][2] == symbol[0] \
    or bd[0][2] == bd[1][1] == bd[2][0] == symbol[0]: 
        print('Player 1 wins!!')
        return True

    if bd[0][0] == bd[0][1] == bd[0][2] == symbol[1] \
    or bd[0][0] == bd[1][0] == bd[2][0] == symbol[1] \
    or bd[0][1] == bd[1][1] == bd[2][1] == symbol[1] \
    or bd[0][2] == bd[1][2] == bd[2][2] == symbol[1] \
    or bd[2][0] == bd[2][1] == bd[2][2] == symbol[1] \
    or bd[1][0] == bd[1][1] == bd[1][2] == symbol[1] \
    or bd[0][0] == bd[1][1] == bd[2][2] == symbol[1] \
    or bd[0][2] == bd[1][1] == bd[2][0] == symbol[1]: 
        print('Player 2 wins!!')
        return True
    return False

def main(bd):
    player_one = input('Player one ? Nots or Cross(O or X): ').upper()
    game_is_on = True
    #display board at the beginning of the game
    while game_is_on:
        print(printBoard(bd))
        #Tell player one to select the symbol
        if player_one == 'O':
            player_two = 'X'
        else:
            player_two = 'O'
    
        if type(player_one) is not str:
            raise('YOu need to Enter either X or O')

        symbol = (player_one,player_two)

        #select position on board
        first = takePosition('one')
        bd[first[0]][first[1]] = symbol[0]
        print(printBoard(bd))
        print('.................................')

        if checkResult(bd,symbol):
            playagain = input('Do you want to play again(yes or no)...').lower()
            if playagain == 'yes':
                continue
            else:
                game_is_on = False

        second = takePosition('two')

        bd[second[0]][second[1]] = symbol[1]
        print(printBoard(bd))
        print('.................................')
        if checkResult(bd,symbol):
            playagain = input('Do you want to play again(yes or no)...').lower()
            if playagain == 'yes':
                continue
            else:
                game_is_on = False
    

main(board)