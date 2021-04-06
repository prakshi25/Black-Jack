import playing_cards

player_hand = [] 
dealer_hand = [] 
 
def display_details():
    print("File   : ")
    print("Author   : ")
    print("Stud ID   : ")
    print("Email ID   : ")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")

def st_en():
    ch=input("\nWould you like to play BlackJack [y|n]? ")
    if (ch=='y')|(ch=='Y'):
        print("\n---------------------- START GAME ----------------------")
        con=1
        return con
    elif (ch=='n')|(ch=='N'):
        con=2
        return con
    else:
        st_en()
        
con=st_en()

def bust_win():
    player_total = get_hand_total(player_hand)
    dealer_total = get_hand_total(dealer_hand)
    if player_total > 21:
        print("Player Busts -> ",player_total)
        card = playing_cards.deal_one_card() 
        player_hand.append(card)
        display_hand('\nPlayer\'s hand is ',player_hand)
        exit(0)
    elif dealer_total > 21:
        print("Dealer Busts -> ", dealer_total)
        card = playing_cards.deal_one_card() 
        dealer_hand.append(card)
        display_hand('\nDealer\'s hand is ',dealer_hand)
        exit(0)
    elif player_total == 21:
        print("--- Player: ",player_total," Dealer: ",dealer_total," -> Player Wins! --- ")
        exit(0)
    elif dealer_total == 21:
        print("--- Dealer: ",dealer_total," Player: ",player_total," -> Dealer Wins! --- ")
        exit(0)

def get_hand_total(hand):
    total=0
    for i in range(len(hand)):
        name = hand[i][0]
        if name == 'T' or name == 'J' or name == 'Q' or name == 'K':
            total+=10
        elif name == 'A':
            total+=11
        else:
            total+=int(name)
    return total

def display_hand(hand_text, hand):
    total_hand = get_hand_total(hand)
    #final="\n"+str(hand_text)+str(total_hand)+": "
    print(hand_text,total_hand,": ",end = '')
    n=len(hand)
    for i in range(n):
        sign = hand[i][1]
        if sign == 'D':
            string1 = " of Diamonds"
        elif sign == 'C':
            string1 = " of Clubs"
        elif sign == 'S':
            string1 = " of Spades"
        else:
            string1 = " of Hearts"

        name = hand[i][0]
        if name == 'J':
            string2 = "Jack" + string1
        elif name == 'Q':
            string2 = "Queen" + string1
        elif name == 'K':
            string2 = "King" + string1
        elif name == 'A':
            string2 = "Ace" + string1
        elif name == 'T':
            string2 = "10" + string1
        else:
            string2 = name + string1
        #final=final+str(string2)
        print(string2,end = '')
        if i<n-1:
            #final= final+" | "
            print(" | ",end = '')
    #print(final) 

def get_hit_choice():
    player_total = get_hand_total(player_hand)
    if len(player_hand)>1:
        hit_choice = input("\n\nPlease enter h or s (h = Hit, s = Stand): ")
        if hit_choice == 'h':
                card = playing_cards.deal_one_card() 
                player_hand.append(card)
                #get_hit_choice()
                display_hand('\nPlayer\'s hand is ',player_hand)
                bust_win()
                get_hit_choice()
        elif hit_choice == 's':
            #player_total=get_hand_total(player_hand)
            if player_total<15:
                print("Cannot stand on value less than 15!")
                play_player_hand(dealer_hand)
            else:
                play_dealer_hand(dealer_hand)
        else:
            while hit_choice!='h' or hit_choice!='s':
                get_hit_choice()
    else:
        card = playing_cards.deal_one_card() 
        player_hand.append(card)

def play_player_hand(player_hand):
    #card = playing_cards.deal_one_card() 
    #player_hand.append(card)
    get_hit_choice()
    #get_hand_total(player_hand)
    display_hand('\nPlayer\'s hand is ',player_hand)
    bust_win()
#play_player_hand(player_hand)

def play_dealer_hand(dealer_hand):
    card = playing_cards.deal_one_card() 
    dealer_hand.append(card)
    #get_hand_total(dealer_hand)
    display_hand('\nDealer\'s hand is ',dealer_hand)
#play_dealer_hand(dealer_hand)

while (con==1):
    for i in range(1,3):
        if i%2!=0:
            if len(dealer_hand)<1:
                play_dealer_hand(dealer_hand)
        else:
            play_player_hand(player_hand)
    #print("\n\nPlay again ? ",end="")
    #con=st_en()
