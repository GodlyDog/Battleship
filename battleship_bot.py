from board import Board

class BattleshipBot():
    def __init__(self, opponent_board: Board, type="probability"):
        self.board = opponent_board
        self.size = opponent_board.size
        self.shots = []
        self.type = type
        if type == "probability":
            self.init_prob()
        
    def init_prob(self):
        self.prob_board = []
        for x in range(self.size):
            self.prob_board.append([])
            for y in range(self.size):
                self.prob_board[x].append(0)

    def neighbors_affected(self, board: [], x: int, y: int, change: int):
        x_neighbors = []
        y_neighbors = []
        if x - 1 >= 0:
            x_neighbors.append(x-1)
        if x + 1 < self.size:
            x_neighbors.append(x+1)
        if y - 1 >= 0:
            y_neighbors.append(y-1)
        if y + 1 < self.size:
            y_neighbors.append(y+1)
        for i in x_neighbors:
            board[i][y] += change
        for j in y_neighbors:
            board[x][j] += change

    def calculate_probs_med(self):
        self.init_prob()
        for shot in self.shots:
            if shot[2]:
                self.neighbors_affected(self.prob_board, shot[0], shot[1], 1)
            else:
                self.neighbors_affected(self.prob_board, shot[0], shot[1], -1)
        for shot in self.shots:
            self.prob_board[shot[0]][shot[1]] = -100

    def print_probs(self):
        for i in range(self.size):
            line = ""
            for j in range(self.size):
                line += " " + str(self.prob_board[i][j]) + " "
            print(line)


    def prob_med_fire(self) -> tuple([int, int]):
        self.calculate_probs_med()
        best = -10
        best_coords = ()
        for x in range(self.size):
            for y in range(self.size):
                if self.prob_board[x][y] > best:
                    best = self.prob_board[x][y]
                    best_coords = (x,y)
        return best_coords
        
    def bot_fire(self) -> tuple([int, int]):
        if self.type == "probability":
            return self.prob_med_fire()
        
    def bot_response(self, fired_coordinate: tuple([int, int]), hit: bool):
        self.shots.append((fired_coordinate[0], fired_coordinate[1], hit))

