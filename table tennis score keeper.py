global player1_score
player1_score = 0
global player2_score
player2_score = 0
global service
service = int(input('enter service player 1 or 2: '))
global match_type
match_type = int(input('enter match type 11 or 21: '))

def deuce(ser):
    player1_duce_score = player1_score
    player2_duce_score = player2_score

    while True:
        if ser == 1:
            ser = 2
        else:
            ser = 1
        print('Service switch')

        duce_point = int(input('Enter deuce point (1 or 2): '))
        if duce_point == 1:
            player1_duce_score += 1
        elif duce_point == 2:
            player2_duce_score += 1
        else:
            print('Invalid input! Please enter either 1 or 2.')
            continue

        if player1_duce_score - player2_duce_score == 2:
            print('Player 1 wins')
            exit()
        elif player2_duce_score - player1_duce_score == 2:
            print('Player 2 wins')
            exit()

        print(f'{player1_duce_score} : {player2_duce_score}')



def normal_play():
    global player1_score, player2_score, service, match_type
    while True:
        point = int(input('enter point 1 or 2: '))
        if point == 1:
            player1_score += 1
        else:
            player2_score += 1

        if (player1_score+player2_score) % 5 == 0:
            print()
            print('service switch')

        if player2_score == match_type:
            print('player 2 win')
            exit()
        elif player1_score == match_type:
            print('player 1 wins')
            exit()

        if player1_score == match_type-1 and player2_score == match_type-1:
            print('DUCE!')
            deuce(service)


        print(f'{player1_score} : {player2_score}')


normal_play()

