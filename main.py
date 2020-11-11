from board import board

if __name__ == "__main__":
    table = board()
    while table.state == "inprogress":
        table.draw_board()
        x = input("Enter x-coordinate of position\n>>")
        y = input("Enter y-coordinate of position\n>>")

        if x.isdigit() and y.isdigit():
            table.move(int(x), int(y))
        else:
            print("Invalid input, please enter again...")
