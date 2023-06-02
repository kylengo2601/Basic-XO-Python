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

def create_board():
    return [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]

def print_board(board):
    cols = " " * 3
    for x in range(len(board[0])):
        cols += str(x) + " "
    print(cols)
    
    for y in range(len(board)):
        board_line = "{} |".format(y)
        for x in range(len(board[0])):
            board_line += "{}|".format(board[y][x])
        print(board_line)


board = create_board()
print_board(board)