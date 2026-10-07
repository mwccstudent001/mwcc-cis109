matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

#playerO_choices = [] #Unutalized
#playerX_choices = [] #Unutalized

turn = 1

players = ['X','O']

winner = None

playerturn = ''

#Game
while winner == None:
    #Who's turn?
    if turn % 2 == 1:
        playerturn = 'X'
    else:
        playerturn = 'O'

    print(f'''TIC-TAC-TOE
Turn: {turn}\n
{matrix[0]}
{matrix[1]}
{matrix[2]}''')

    #Tie condition
    if turn == 10 and winner == None:
        print("----------\nIt's a tie\n----------")
        exit
        break
    else:
        pass

    #Win conditions
    for column in range(3):
        
        if matrix[0][column] == matrix[1][column] == matrix[2][column]:
            if matrix[0][column] == '-':
                break
            winner = matrix[0][column]
            print(f'Player {winner} wins!')
            exit()
        else:
            pass
    for row in range(3):
        if matrix[row][0] == matrix[row][1] == matrix[row][2]:
            if matrix[row][0] == '-':
                break
            winner = matrix[0][row]
            print(f'Player {winner} wins!')
            exit()
        else:
            pass
    for diagonal_right in range(3):
        if matrix[0][0] == matrix[1][1] == matrix[2][2]:
            if matrix[0][0] == '-':
                break
            winner = matrix[0][0]
            print(f'Player {winner} wins!')
            exit()
        else:
            pass
    for diagonal_left in range(3):
        if matrix[0][2] == matrix[1][1] == matrix[2][0]:
            if matrix[0][2] == '-':
                break
            winner = matrix[0][row]
            print(f'Player {winner} wins!')
            exit()
        else:
            pass
        
    print(f"{playerturn}'s Turn")
    rowchoice = input('Enter row (1-3): ')
    columnchoice = input('Enter row (1-3): ')

    #Check for int input
    try:
        rowchoice = int(rowchoice)
        columnchoice = int(columnchoice)
    except ValueError:
        print('\nInvalid input, please try again\n')
        continue

    print('')
    
    #Check for valid number
    if not rowchoice in range(1,4) or not columnchoice in range(1,4):
        print('Invalid number, please try again\n')
        turn = turn - 1 #Keeping turn the same
    else:
        #Check for empty spot
        if matrix[(rowchoice - 1)][(columnchoice - 1)] == '-':
            matrix[(rowchoice - 1)][(columnchoice - 1)] = playerturn
        else:
            print('That spot is taken, pick a different one.\n')
            turn = turn - 1 #Keeping turn the same
    
    turn = turn + 1 #Next turn