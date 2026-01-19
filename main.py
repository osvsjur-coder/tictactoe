def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_draw(board):
    return all(cell != " " for cell in board)


def play_game(scores):
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)

        try:
            move = int(input(f"Žaidėjas {current_player}, pasirink langelį (1-9): ")) - 1
            if board[move] != " " or move < 0 or move > 8:
                print("Netinkamas ėjimas, bandyk dar kartą.")
                continue
        except:
            print("Įvesk skaičių nuo 1 iki 9.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Žaidėjas {current_player} laimėjo!")
            scores[current_player] += 1
            break

        if is_draw(board):
            print_board(board)
            print("🤝 Lygiosios!")
            break

        current_player = "O" if current_player == "X" else "X"


def main():
    scores = {"X": 0, "O": 0}

    while True:
        play_game(scores)
        print(f"\nRezultatas: X = {scores['X']} | O = {scores['O']}")

        choice = input("\nAr nori žaisti dar kartą? (t/n): ").lower()
        if choice != "t":
            print("Ačiū, kad žaidei 👋")
            break


main()
python3 main.py
touch README.md
python3 main.py
touch README.md

