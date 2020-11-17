from blackjack import Deck, Card, Player


if __name__ == '__main__':
    deck = Deck()
    dealer = Player("Dealer")
    patron = Player("Patron")

    patron.add_cards(deck.deal(2))
    dealer.add_cards(deck.deal(2))

    game_on = True
    round_num = 1
    player_turn = True

    while game_on:

        if patron.total == 21:
            print("---------- BLACKJACK! ----------")
            game_on = False
            break

        if player_turn:
            print(f"---------- ROUND {round_num} ----------")
            patron.print_total()

            choice = input("Hit or Stay: ")
            if choice.lower() == "hit":
                patron.add_cards(deck.deal(1))
            elif choice.lower() == "stay":
                player_turn = False

        else:
            print(f"---------- DEALER'S TURN ----------")
            dealer.print_total()

            if dealer.total < 17:
                dealer.add_cards(deck.deal(1))
            else:
                game_on = False
                if patron.total > dealer.total:
                    print(f"---------- YOU WIN! ----------")
                elif patron.total == dealer.total:
                    print(f"---------- TIE! ----------")
                else:
                    print(f"---------- YOU LOSE! ----------")


        if patron.total > 21:
            print(f"---------- BUST! ----------")
            game_on = False
        elif dealer.total > 21:
            print(f"---------- DEALER BUSTS! ----------")
            print(f"---------- YOU WIN! ----------")
            game_on = False

        round_num += 1

    print(f"{patron.name}'s total is {patron.total}")
    print(f"{dealer.name}'s total is {dealer.total}")
