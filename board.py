class board:
    def __init__(self):
        self.state = "inprogress"
        self.board = [
                        ["#", "#", "#"],
                        ["#", "#", "#"],
                        ["#", "#", "#"]
                    ]
        self.turn = "X"
        print("X starts the game")

    def draw_board(self):
        print(self.board[0][2] + self.board[1][2] + self.board[2][2])
        print(self.board[0][1] + self.board[1][1] + self.board[2][1])
        print(self.board[0][0] + self.board[1][0] + self.board[2][0])


    def swap_turn(self):
        if self.turn == "X":
            self.turn = "O"
            print("It is now Os turn...")
        else:
            self.turn = "X"
            print("It is now Xs turn...")

    def move(self, x, y):
        if self.board[x][y] == "#":
            self.board[x][y] = self.turn
            self.swap_turn()
        else:
            "Invalid Space"
