from board import Board

def main():
    b = Board()
    carrier = ((0,0), (0,4))
    battleship = ((1,0), (1,3))
    cruiser = ((2,0), (2,2))
    submarine = ((3,0), (3,2))
    destroyer = ((4,0), (4,2))
    assert(b.place_ships(carrier, battleship, cruiser, submarine, destroyer))
    b.debug_print()

if __name__ == "__main__":
    main()