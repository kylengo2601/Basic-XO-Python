# Array: chứa nhiều giá trị (values) trong cùng một biến (variable)
# arr = ["Honda", "Yamaha", "KTM", "Harley Davidson"]
# matrix = [
#     ["Honda", "Yamaha", "KTM", "Harley Davidson"], 
#     ["Airbus", "Boeing", "Cessna", "Pilatus"], 
#     ["Ford", "Toyota", "Mercedes", "Honda"]
# ]

# print(arr[0])
# print(matrix[0][0])



"""
    Luật chơi:
    Có 2 người chơi: X và O. Hai người chơi trên một bàn cờ có 3 cột ngang và 3 cột dọc.
    
    Nếu người chơi nào đặt được cờ (X hoặc O) của mình từ trái sang phải theo chiều dọc, 
    ngang, hoặc chéo trước, thì người đó thắng. 
    Trong trường hợp cả 2 không thể thắng vì đã hết nước đi, hai người chơi sẽ hòa.
"""

# As a beginning state, write a function to return a 3x3 matrix with all space - " " 
# characters.
def create_board():
    return [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]

board = create_board()

# Given
def print_board():
    cols = " " * 3
    for x in range(len(board[0])):
        cols += str(x) + " "
    print(cols)
    
    for y in range(len(board)):
        board_line = "{} |".format(y)
        for x in range(len(board[0])):
            board_line += "{}|".format(board[y][x])
        print(board_line)


# Write a function to either place an X or O to the specified position on the board.
def make_play(player, y_coor, x_coor):
    board[y_coor][x_coor] = player
    print_board()

# Sample manual play
# make_play("O", 1, 1)
# make_play("X", 1, 2)
# make_play("O", 0, 0)
# make_play("X", 2, 2)
# make_play("O", 0, 2)
# make_play("X", 2, 0)
# make_play("O", 2, 1)
# make_play("X", 0, 1)
# make_play("O", 1, 0)