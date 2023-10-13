from ship import Ship
import random

class Tile():
    def __init__(self, position: tuple([int, int])):
        self.position = position
        self.contents = None
        self.hit = False
    
    def create_contents(self, ship: Ship) -> bool:
        if self.contents is not None:
            return False
        self.contents = ship
        return True
    
    def ship_present(self) -> bool:
        if self.contents is None:
            return False
        else:
            return True

    def hit_contents(self) -> int:
        assert(not self.hit)
        self.hit = True
        if self.contents is None:
            return -1
        else:
            return self.contents.hit()

class Board():
    def __init__(self, board_side_length=10):
        self.size = board_side_length
        self.grid = []
        self.misses = []
        self.hits = []
        self.ships_remaining = 5
        # x is a row number (the board indexes down then over)
        for x in range(self.size):
            self.grid.append([])
            for y in range(self.size):
                self.grid[x].append(Tile((x, y)))

    def debug_print(self):
        print("\n")
        for x in range(self.size):
            line = ""
            for y in range(self.size):
                if self.grid[x][y].contents is None:
                    line += "O"
                else:
                    if self.grid[x][y].contents.type == "Carrier":
                        line += "C"
                    if self.grid[x][y].contents.type == "Destroyer":
                        line += "D"
                    if self.grid[x][y].contents.type == "Cruiser":
                        line += "U"
                    if self.grid[x][y].contents.type == "Submarine":
                        line += "S"
                    if self.grid[x][y].contents.type == "Battleship":
                        line += "B"
            print(line)

    def print_hit_map(self):
        print("\n")
        for x in range(self.size):
            line = ""
            for y in range(self.size):
                if (x,y) in self.hits:
                    line += "X"
                elif (x,y) in self.misses:
                    line += "#"
                else:
                    line += "O"
            print(line)

    def find_positions(self, positions: tuple([tuple([int, int]), tuple([int, int])])) -> [tuple([int, int])]:
        start = positions[0]
        end = positions[1]
        vector = (start[0] - end[0], start[1] - end[1])
        result = []
        if vector[0] == 0:
            length = vector[1]
            if length < 0:
                for i in range(0, length - 1, -1):
                    result.append((start[0], start[1] + (-1 * i)))
            if length > 0:
                for i in range(0, length + 1):
                    result.append((start[0], start[1] + (-1 * i)))
        elif vector[1] == 0:
            length = vector[0]
            if length < 0:
                for i in range(0, length - 1, -1):
                    result.append((start[0] + (-1 * i), start[1]))
            if length > 0:
                for i in range(0, length + 1):
                    result.append((start[0] + (-1 * i), start[1]))
        return result

    
    def create_ship_random(self, n: int, name: str):
        finished = False
        while not finished:
            vertical = bool(random.randint(0, 1))
            positive = bool(random.randint(0, 1))
            x,y = -1,-1
            if vertical:
                y = random.randint(0, self.size - 1)
                if positive:
                    if x + (n-1) >= self.size:
                        continue
                    else:
                        x = random.randint(0, self.size - n)
                        end_x, end_y = x + (n - 1), y
                else:
                    if x - (n - 1) < 0:
                        continue
                    else:
                        x = random.randint(n-1, self.size - 1)
                        end_x, end_y = x - (n - 1), y
            else:
                x = random.randint(0, self.size - 1)
                if positive:
                    if y + (n-1) >= self.size:
                        continue
                    else:
                        y = random.randint(0, self.size - n)
                        end_x, end_y = x, y + (n-1)
                else:
                    if y - (n-1) < 0:
                        continue
                    else:
                        y = random.randint(n-1, self.size - 1)
                        end_x, end_y = x, y - (n-1)
            positions = self.find_positions(((x, y), (end_x, end_y)))
            print("n: " + str(n))
            print("x: " + str(x))
            print("y: " + str(y))
            print("end x: " + str(end_x))
            print("end y: " + str(end_y))
            ship = Ship(name, ((x,y), (end_x, end_y)))
            print(len(positions))
            assert(len(positions) == n)
            flag = False
            for position in positions:
                if self.grid[position[0]][position[1]].ship_present():
                    flag = True
            if flag:
                continue
            for position in positions:
                self.grid[position[0]][position[1]].create_contents(ship)
            finished = True
        
    def place_random(self):
        self.create_ship_random(5, "Carrier")
        self.create_ship_random(4, "Battleship")
        self.create_ship_random(3, "Cruiser")
        self.create_ship_random(3, "Submarine")
        self.create_ship_random(2, "Destroyer")
            

    def place_ships(self, carrier_pos: tuple([tuple([int, int]), tuple([int, int])]), battleship_pos: tuple([tuple([int, int]), tuple([int, int])]), cruiser_pos: tuple([tuple([int, int]), tuple([int, int])]), submarine_pos: tuple([tuple([int, int]), tuple([int, int])]), destroyer_pos: tuple([tuple([int, int]), tuple([int, int])])) -> bool:
        carrier = Ship("Carrier", carrier_pos)
        battleship = Ship("Battleship", battleship_pos)
        cruiser = Ship("Cruiser", cruiser_pos)
        submarine = Ship("Submarine", submarine_pos)
        destroyer = Ship("Destroyer", destroyer_pos)
        carrier_positions = self.find_positions(carrier_pos)
        battleship_positions = self.find_positions(battleship_pos)
        cruiser_positions = self.find_positions(cruiser_pos)
        submarine_positions = self.find_positions(submarine_pos)
        destroyer_positions = self.find_positions(destroyer_pos)
        if len(carrier_positions) != 5 or len(battleship_positions) != 4 or len(cruiser_positions) != 3 or len(submarine_positions) != 3 or len(destroyer_positions) != 2:
            print("Carrier Length :" + str(len(carrier_positions)))
            print("Battleship Length :" + str(len(battleship_positions)))
            print("Cruiser Length :" + str(len(cruiser_positions)))
            print("Submarine Length :" + str(len(submarine_positions)))
            print("Destroyer Length :" + str(len(destroyer_positions)))
            print("LENGTH ERROR")
            return False
        for position in carrier_positions:
            if not self.grid[position[0]][position[1]].create_contents(carrier):
                self.__init__(self.size)
                return False
        for position in battleship_positions:
            if not self.grid[position[0]][position[1]].create_contents(battleship):
                self.__init__(self.size)
                return False
        for position in cruiser_positions:
            if not self.grid[position[0]][position[1]].create_contents(cruiser):
                self.__init__(self.size)
                return False
        for position in submarine_positions:
            if not self.grid[position[0]][position[1]].create_contents(submarine):
                self.__init__(self.size)
                return False
        for position in destroyer_positions:
            if not self.grid[position[0]][position[1]].create_contents(destroyer):
                self.__init__(self.size)
                return False
        return True
    
    def fire(self, position: tuple([int, int])) -> tuple([int, str]):
        if position in self.hits or position in self.misses:
            return (-2, "")
        hit_or_miss = self.grid[position[0]][position[1]].hit_contents()
        if hit_or_miss == -1:
            self.misses.append(position)
            return (hit_or_miss, "")
        if hit_or_miss >= 0:
            self.hits.append(position)
            if hit_or_miss == 1:
                self.ships_remaining -= 1
            return (hit_or_miss, self.grid[position[0]][position[1]].contents.type)


        



