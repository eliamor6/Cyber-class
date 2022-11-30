import random
class map:
    def __init__(self, map_file_path):
        x = open(map_file_path , 'rb')
        map_x = x.read()
        self.line_length = map_x[0]
        self.game_map = []
        self.num_of_lines = int(len(map_x) / self.line_length)
        index = 0
        map_x = map_x[1:]
        for j in range(self.num_of_lines):
            line_list = []
            for i in range(self.line_length):
                line_list.append(int(map_x[index]))
                index += 1
            self.game_map.append(line_list)
        self.location_of_C = [1,1]
        self.location_of_T = [1,2]
        self.location_of_X = [1,2]

        def start_random_locaition(game_map_list):
            while True:
                line = random.randint(0, len(game_map_list) - 1)
                column = random.randint(0, len(game_map_list[0]) - 1)
                if game_map_list[line][column] == 0:
                    return [line, column]
        while self.location_of_T == self.location_of_X or self.location_of_T == self.location_of_C:
            self.location_of_C = start_random_locaition(self.game_map)
            self.location_of_T = start_random_locaition(self.game_map)
            self.location_of_X = start_random_locaition(self.game_map)

    def move(self, direction):
        if direction == "UP":
            self.new_location_of_T = [self.location_of_T[0] , self.location_of_T[1] - 1]
        elif direction == "DOWN":
            self.new_location_of_T = [self.location_of_T[0] , self.location_of_T[1] + 1]
        elif direction == "LEFT":
            self.new_location_of_T = [self.location_of_T[0] - 1, self.location_of_T[1]]
        elif direction == "RIGHT":
            self.new_location_of_T = [self.location_of_T[0] + 1 , self.location_of_T[1]]
        if self.game_map[self.new_location_of_T[0] , self.new_location_of_T[1]] == 1:
            return "you bumped in the wall,you stay where you were"
        if self.new_location_of_T == self.location_of_C:
            return "you got caught:(, maybe next time you'll win"
        if self.new_location_of_T == self.location_of_X:
            return "Congratulations, you won"
        else:
            self.location_of_T = self.new_location_of_T
            return "got it"
    def cop_random_move(self):
        new_location_of_C = [self.location_of_C[0] + random.randint(-1,1) , self.location_of_C[1] + random.randint(-1,1)]
        if self.game_map[new_location_of_C[0] , new_location_of_C[1]] == 1:
            return "you bumped in the wall,you stay where you were"
        if new_location_of_C == self.location_of_T:
            return "you got caught:(, maybe next time you'll win"
        else:
            self.location_of_C = [new_location_of_C[0], new_location_of_C[1]]
    def one_step_away(self):
        if  abs(self.location_of_T[0] - self.location_of_X[0]) == 1 or abs(self.location_of_T[1] - self.location_of_X[1]) or abs(self.location_of_T[0] - self.location_of_C[0]) == 1 or abs(self.location_of_T[1] - self.location_of_C[1]):
            return "you are one step away from the tresur or the cop"
        else:
            return "you are not one step away from the treasure or the cop"
    def __str__(self):
        map_now = ""
        for j in range(self.num_of_lines):
            for i in range(self.line_length):
                if i == True:
                    map_now += "*"
                elif self.game_map[i,j] == self.game_map[self.location_of_T[0],self.location_of_T[1]]:
                    map_now += "T"
                elif self.game_map[i,j] == self.game_map[self.location_of_X[0],self.location_of_X[1]]:
                    map_now += "X"
                elif self.game_map[i,j] == self.game_map[self.location_of_C[0],self.location_of_C[1]]:
                    map_now += "C"
                else:
                    map_now += " "
            map_now += "\n"
