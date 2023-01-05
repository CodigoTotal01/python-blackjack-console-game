
import random
def deal_card() -> int:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # lista
    if cards == 21 and len(cards) == 2:
        return 0
    # hallar un elemento dentro de un arreglo
    if 11 in cards and sum(cards) > 21:
        # si es mayor-> quitalo -> y pon uno
        cards.remove(11)
        cards.append(1)
    return sum(cards)  # la suma total nuevamente


def compare(user_score, computer_score):
    # si ambos pierden
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return f'It\'s a draw'
    elif user_score == 0:
        return "Usuario a ganado"
    elif computer_score == 0:
        return "Compuador a ganado"
    elif user_score > 21:
        return "Usuario a te pasaste "
    elif computer_score > 21:
        return "PC a te pasaste "
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


# la parte enfocada en el juego
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # iterar sobre ellos dos veces
    for i in range(2):  # (0,1)
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    # cada que se pida una carta nueva-> se debera saber el puntaje

    while not is_game_over:
        user_score = calculate_score(user_cards)  # suma
        computer_score = calculate_score(computer_cards)  # suma
        # mostar infor
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # preguntar si quiere mas cartas
            user_should_deal = input("Deseas tomar otra carta? y-> yes, n -> no")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    #the computer will take as values only if less 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()