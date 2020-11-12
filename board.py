class board:
    def __init__(self):
        self.state = "inprogress"
        self.board = [
            ["#", "#", "#"],
            ["#", "#", "#"],
            ["#", "#", "#"]
        ]
        self.turn = "X"
        self.winner = ""
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
        if self.board[x - 1][y - 1] == "#":
            self.board[x - 1][y - 1] = self.turn
            self.swap_turn()
        else:
            "Invalid Space"

    def check_winner(self):
        # Vertical
        for col in self.board:
            if col[0] == col[1] and col[1] == col[2] and col[0] != "#":
                self.state = "over"
                self.winner = col[0]
                print("Congrats! " + self.winner + " is the winner")

        # Horizontal
        for i in range(3):
            index = i - 1
            if (self.board[0][index] == self.board[1][index] and
                    self.board[1][index] == self.board[2][index] and
                    self.board[0][index] != "#"):
                self.state = "over"
                self.winner = self.board[0][index]
                self.draw_board()
                print("Congrats! " + self.winner + " is the winner")

        # Diagonal
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] != "#":
            self.state = "over"
            self.winner = self.board[0][0]
            self.draw_board()
            print("Congrats! " + self.winner + " is the winner")
        elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] != "#":
            self.state = "over"
            self.winner = self.board[0][2]
            self.draw_board()
            print("Congrats! " + self.winner + " is the winner")
