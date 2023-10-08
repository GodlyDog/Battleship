from board import Board
import os

def parse_input(string: str) -> tuple([int, int]):
    string = string.split(",")
    string = (int(string[0]), int(string[1]))
    return string

def request_placement(board: Board, player: str):
    correct = False
    first = True
    while not correct:
        if not first:
            print("Invalid positions, please input different positions")
        first = False
        print("Player " + player + ": input Carrier coordinates (length of 5)")
        carrier_start = input("Carrier start?")
        carrier_start = parse_input(carrier_start)
        carrier_end = input("Carrier end?")
        carrier_end = parse_input(carrier_end)
        print("Player " + player + ": input Battleship coordinates (length of 4)")
        battleship_start = input("Battleship start?")
        battleship_start = parse_input(battleship_start)
        battleship_end = input("Battleship end?")
        battleship_end = parse_input(battleship_end)
        print("Player " + player + ": input Cruiser coordinates (length of 3)")
        cruiser_start = input("Cruiser start?")
        cruiser_start = parse_input(cruiser_start)
        cruiser_end = input("Cruiser end?")
        cruiser_end = parse_input(cruiser_end)
        print("Player " + player + ": input Submarine coordinates (length of 3)")
        submarine_start = input("Submarine start?")
        submarine_start = parse_input(submarine_start)
        submarine_end = input("Submarine end?")
        submarine_end = parse_input(submarine_end)
        print("Player " + player + ": input Destroyer coordinates (length of 2)")
        destroyer_start = input("Destroyer start?")
        destroyer_start = parse_input(destroyer_start)
        destroyer_end = input("Destroyer end?")
        destroyer_end = parse_input(destroyer_end)
        correct = board.place_ships((carrier_start, carrier_end), (battleship_start, battleship_end), (cruiser_start, cruiser_end), (submarine_start, submarine_end), (destroyer_start, destroyer_end))

def request_fire(board: Board, player: str) -> bool:
    board.print_hit_map()
    inputting = True
    while inputting:
        target = input("Commander, where is our target?")
        target = parse_input(target)
        if len(target) == 2 and target[0] < board.size and target[1] < board.size:
            inputting = False
        else:
            print("Invalid target")
    status = board.fire(target)
    if status[0] < 0:
        print("Miss!")
    if status[0] == 0:
        print("Hit!")
    if status[0] == 1:
        print("Hit! Sunk " + status[1])
    if board.ships_remaining == 0:
        print("Game over! " + player + " wins!")
        return True
    return False
    

def repl(player1_board: Board, player2_board: Board):
    finished = False
    request_placement(player1_board, "1")
    os.system("cls" if os.name == "nt" else "clear")
    request_placement(player2_board, "2")
    os.system("cls" if os.name == "nt" else "clear")
    while not finished:
        input("Player 1 ready to fire? Press any key when ready.")
        finished = request_fire(player2_board, "Player 1")
        if finished:
            break
        input("Player 2 ready to fire? Press any key when ready.")
        finished = request_fire(player1_board, "Player 2")

        
        

def main():
    b1 = Board()
    b2 = Board()
    repl(b1, b2)

if __name__ == "__main__":
    main()