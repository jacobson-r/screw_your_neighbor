import tkinter as tk
import random

card_deck = {"HA":1,"H2":2,"H3":3,"H4":4,"H5":5,"H6":6,"H7":7,"H8":8,"H9":9,"H10":10,"HJ":11,"HQ":12,"HK":13,
"DA":1,"D2":2,"D3":3,"D4":4,"D5":5,"D6":6,"D7":7,"D8":8,"D9":9,"D10":10,"DJ":11,"DQ":12,"DK":13,
"SA":1,"S2":2,"S3":3,"S4":4,"S5":5,"S6":6,"S7":7,"S8":8,"S9":9,"S10":10,"SJ":11,"SQ":12,"SK":13,
"CA":1,"C2":2,"C3":3,"C4":4,"C5":5,"C6":6,"C7":7,"C8":8,"C9":9,"C10":10,"CJ":11,"CQ":12,"CK":13}
cards_out = []
cards_on_table = 0
player_list = []

def top_deck(cards_out,card_deck,cards_on_table):
    if(len(cards_out) == len(card_deck)):
        cards_out = cards_out[len(cards_out)-cards_on_table:]
    while True:
        card = list(card_deck)[random.randint(0,len(card_deck)-1)]
        if card in cards_out:
            continue
        return card

player_dict = {}

players = 4

for x in range(players):
    name = input(f"player #{x+1}'s Name: ")
    player_list.append(name)
    player_dict.update({name:None})




def trade_card(player_list,player_dict):
    your_card = player_dict[player_list[0]]
    player_dict[player_list[0]] = player_dict[player_list[1]]
    player_dict[player_list[1]] = your_card
    temp = player_list.pop(0)
    player_list.append(temp)
    return (player_dict, player_list)

def pass_card(player_list,player_dict):
    temp = player_list.pop(0)
    player_list.append(temp)
    return (player_dict, player_list)


def round(player_list, player_dict, cards_out, card_deck, cards_on_table):
    #gives each player a card
    for name in player_list:
        player_dict[name] = top_deck(cards_out,card_deck,cards_on_table)
        cards_out.append(player_dict[name])
        cards_on_table += 1
    #prints everybody and thier cards
    print(player_dict)
    #print(cards_out)
    #print(cards_on_table)

    #Everybody trade except last person. 
    for i in range(len(player_list)-1):
        pass_trade = input("Do you want to pass or trade? ") #will have to link w/ ryan's stuff
        if(pass_trade == "pass"):
            temp_list = pass_card(player_list, player_dict)
        else:
            temp_list = trade_card(player_list,player_dict)
        player_list = temp_list[1]
        player_dict = temp_list[0]

    #last person top decks
    pass_trade = input("Do you want to pass or trade? ")
    if(pass_trade == "trade"):
        player_dict[player_list[0]] = top_deck(cards_out,card_deck,cards_on_table)
        cards_out.append(player_dict[player_list[0]])
        cards_on_table += 1
    temp = player_list.pop(0)
    player_list.append(temp)
    temp = player_list.pop(0)
    player_list.append(temp)

    print(player_dict)


         
round(player_list, player_dict, cards_out, card_deck, cards_on_table)

def winner_loser(player_list,player_dict):
    pass

def game():
    pass


#Makes Widnow
root = tk.Tk()
root.title("Screw Your Neighbor")
root.geometry("512x512")
pass_button = tk.Button(root, text="Pass").grid(row=5,column=5)
trade_button = tk.Button(root, text="Trade").grid(row=6,column=5)
