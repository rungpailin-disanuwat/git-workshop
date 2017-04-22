# -*- coding: utf-8 -*-
# @Author: Kotori
# @Date:   2017-03-24 20:05:19
# @Last Modified by:   b_ben
# @Last Modified time: 2017-04-19 22:33:27

import random


def main():
    print('''--------------------------------------------------------------------------------
    00         00 00000000 00        0000000  000000  00         00 00000000
    00         00 00       00       00       00    00 0000     0000 00
    00         00 00       00       00       00    00 00  00 00  00 00
    00    0    00 0000000  00       00       00    00 00    0    00 0000000     
    00  00 00  00 00       00       00       00    00 00         00 00
    0000     0000 00       00       00       00    00 00         00 00 
    00         00 00000000 00000000  0000000  000000  00         00 00000000
--------------------------------------------------------------------------------
                            000000000000   OOOOOOO0
                                 00       00      00
                                 00       00      00
                                 00       00      00
                                 00       00      00
                                 00        00000000     
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
D      DD  DDDDDDDDD   DDDDDD      D  DDD  D     00     000     000000 00   00 D
D  DDD  D  DDDDDDDD  D  DDDD  DDDDDD  D   DD     00    00 00   00      00 000  D
D     DDD  DDDDDDD       DDD  DDDDDD     DDD     00   0000000  00      0000    D
D  DD   D  DDDDDD  DDDDD  DD  DDDDDD  D   DD 0   00  00     00 00      00 00   D
D      DD       D  DDDDD  DDD      D  DD   D 000000  00     00  000000 000  00 D
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
''')
    win = ('''--------------------------------------------------------------------------------
         00    00   00000   00    00        00       00  00  000    00
          00  00   00   00  00    00        00       00  00  00 0   00
           0000    00   00  00    00        00   0   00  00  00  0  00
            00     00   00  00    00        00  0 0  00  00  00   0 00
            00     00   00  00    00        00 00 00 00  00  00    000
            00      00000    000000          000   000   00  00     00
--------------------------------------------------------------------------------''')
    lose = (''' 
--------------------------------------------------------------------------------
      00    00   000000   00    00      00        00000   000000  0000000
       00  00   00    00  00    00      00       00   00 00       00
        0000    00    00  00    00      00       00   00  00      00
         00     00    00  00    00      00       00   00    00    000000
         00     00    00  00    00      00       00   00      00  00 
         00     00    00  00    00      00       00   00       00 00
         00      000000    000000       0000000   00000   000000  0000000
--------------------------------------------------------------------------------''')
    draw = ('''
--------------------------------------------------------------------------------
                    000000    000000      000     00       00  
                    00   00   00   00    00 00    00       00     
                    00    00  00   00   00   00   00   0   00  
                    00    00  000000   000000000  00  0 0  00      
                    00   00   00   00  00     00  00 00 00 00  
                    000000    00    00 00     00   000   000   
--------------------------------------------------------------------------------
      ''')
      
    print('Input number of round to play: ',end='')
    score = [0, 0]
    Round = int(input())
    for r in range(Round):
        d = r+1
        print('Round %d'%d)
        round_score = blackjack_game()
        if(round_score[0] == 1):
            score[0] = score[0] + 1
        elif(round_score[1] == 1):
            score[1] = score[1] + 1
        print('Score PLAYER : BOT is %s'%score[0] ,end=':')
        print(score[1])
        print()
    if score[0] > score[1]:
        print(win)
    elif score[0] < score[1]:
        print(lose)
    elif score[0] == score[1]:
        print(draw)
        

def blackjack_game():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    player_hand = []
    bot_hand = []
    end = False
    b_com = 'Y'
    p_com = 'Y'
    print('Please select numbers only 0 and 1 : ',end='')
    first_ = random.randrange(0,2)
    select_num = int(input())
    if first_ == select_num:
        print('Player is first player')
        return player_st(deck,player_hand,bot_hand,end,b_com)

    elif first_ != select_num:
        print('Bot is first player')
        return bot_st(deck,player_hand,bot_hand,end,p_com)
       

def player_st(deck,player_hand,bot_hand,end,b_com):
    while not end:
        p_com = player_command(len(player_hand))
        if p_com == 'Y':
            player_hand.append(deck.pop(random.randrange(0,len(deck))))
        if p_com != 'Y' and ans_ai != 'Y':
            end = True
            break
        if len(player_hand) >= 2 and len(bot_hand) >= 2:
            print("Player cards :", end=' ')
            for i in player_hand:
                print(i, end=' ')
            print("({0}/21)".format(count_point(player_hand)))
            print("Bot cards    : ?", end=' ')
            for i in bot_hand[1:]:
                print(i, end=' ')
            print("({0}+?/21)".format(count_point(bot_hand[1:])))

        if len(bot_hand) < 2 or ans_ai =='Y':
            bot_hand.append(deck.pop(random.randrange(0,len(deck))))
        if p_com != 'Y' and ans_ai != 'Y':
            end = True
            break
        if len(player_hand) >= 2:
            print("Player cards :", end=' ')
            for i in player_hand:
                print(i, end=' ')
            print("({0}/21)".format(count_point(player_hand)))
            print("Bot cards    : ?", end=' ')
            for i in bot_hand[1:]:
                print(i, end=' ')
            print("({0}+?/21)".format(count_point(bot_hand[1:])))

        ans_ai = AI(bot_hand,player_hand)

    print("Player cards :", end=' ')
    for i in player_hand:
        print(i, end=' ')
    print("({0}/21)".format(count_point(player_hand)))
    print("Bot cards    :", end=' ')
    for i in bot_hand:
        print(i, end=' ')
    print("({0}/21)".format(count_point(bot_hand)))
    player_score = count_point(player_hand)
    bot_score = count_point(bot_hand)
    if(player_score > 21 or bot_score > 21):
        if(player_score <= 21):
            print("You win")
            return [1, 0]
        elif(bot_score <= 21):
            print("You lose")
            return [0, 1]
        else:
            print("Dawn")
            return [0, 0]
    else:
        if(player_score < bot_score):
            print("You lose")
            return [0, 1]
        elif(player_score > bot_score):
            print("You win")
            return [1, 0]
        else:
            print("Dawn")
            return [0, 0]


def bot_st(deck,player_hand,bot_hand,end,p_com):
    while not end:
        if len(bot_hand) < 2 or ans_ai == 'Y':
            bot_hand.append(deck.pop(random.randrange(0,len(deck))))

        if p_com != 'Y' and ans_ai  != 'Y':
            end = True
            break

        if len(player_hand) >= 2:
            print("Bot cards    : ?", end=' ')
            for i in bot_hand[1:]:
                print(i, end=' ')
            print("({0}+?/21)".format(count_point(bot_hand[1:])))
            print("Player cards :", end=' ')
            for i in player_hand:
                print(i, end=' ')
            print("({0}/21)".format(count_point(player_hand)))
        
        p_com = player_command(len(player_hand))
        if p_com == 'Y':
            player_hand.append(deck.pop(random.randrange(0,len(deck))))
        if p_com != 'Y' and ans_ai != 'Y':
            end = True
            break
        if len(player_hand) >= 2 and len(bot_hand) >= 2:
            print("Bot cards    : ?", end=' ')
            for i in bot_hand[1:]:
                print(i, end=' ')
            print("({0}+?/21)".format(count_point(bot_hand[1:])))
            print("Player cards :", end=' ')
            for i in player_hand:
                print(i, end=' ')
            print("({0}/21)".format(count_point(player_hand)))

        ans_ai = AI(bot_hand,player_hand)


    print("Bot cards    :", end=' ')
    for i in bot_hand:
        print(i, end=' ')
    print("({0}/21)".format(count_point(bot_hand)))
    print("Player cards :", end=' ')
    for i in player_hand:
        print(i, end=' ')
    print("({0}/21)".format(count_point(player_hand)))
    
    player_score = count_point(player_hand)
    bot_score = count_point(bot_hand)
    # count_b = 0
    # count_p = 0
    # list_score = []
    if(player_score > 21 or bot_score > 21):
        if(player_score <= 21):
            print("You win")
            return [1, 0]
        elif(bot_score <= 21):
            print("You lose")
            return [0, 1]
        else:
            print("Dawn")
            return [0, 0]
    else:
        if(player_score < bot_score):
            print("You lose")
            return [0, 1]
        elif(player_score > bot_score):
            print("You win")
            return [1, 0]
        else:
            print("Dawn")
            return [0, 0]
    # list_score.append(count_p).append(count_b)
    # return list_score


def AI(bot_hand,player_hand):
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    score_bot = count_point(bot_hand)
    player_hand = player_hand[1:]

    for data in bot_hand:
        if data in deck:
            deck.remove(data)
        if data in player_hand:
            deck.remove(data)
        list1 = []
        list2 = []
        do = []
        for i in deck:
            do.append(i)
            F = count_point(do)
            if F + score_bot > 21:
                list1.append(i)
            elif F + score_bot <= 21:
                list2.append(i)
            do.clear()
        if len(list1) > len(list2):
            return "N"
        elif len(list1) < len(list2):
            return "Y"
        else:
            dif = 21 - score_bot
            if dif <= 4:
                return 'Y'
            else:
                return 'N'


def player_command(player_hand):
    if player_hand < 2:
        return 'Y'
    print("Do you want to draw a card (Y/N)")
    command = input('=====> ')
    return command


def count_point(hand):
    point = 0
    for i in hand:
        if i == 'A':
            point = point + 11
        elif i in ['J', 'Q', 'K']:
            point = point + 10
        else:
            point = point + i
    return point


if __name__ == '__main__':
    main()




