board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]
board_1 = [
    "##########",
    "#........#",
    "#..####..#",
    "#..#..#..#",
    "#..####..#",
    "#........#",
    "##########",
]

def flood_fill(input_board, old, new, x, y):

    # Check if the coordinates are out of bound
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]):
      return input_board

    # Replace the starting point
    if input_board[x][y] == old:
      input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]

      # Replace the entire row
      flood_fill(input_board, old, new, x, y+1)
      flood_fill(input_board, old, new, x, y-1)

      # Replace the rows on top
      flood_fill(input_board, old, new, x-1, y)

      # Replace the rows below
      flood_fill(input_board, old, new, x+1, y)

    return input_board

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

modified_board = flood_fill(input_board=board, old=".", new="~", x=1, y=1)

for a in modified_board:
    print(a)

# Expected output:
#~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~##########~~~~~~
#~~~~~~#........#~~~~~~
#~~~~~~#........#~~~~~~
#~~~~~~#........#####~~
#~~~~###............#~~
#~~~~#............###~~
#~~~~##############~~~~

modified_board = flood_fill(input_board=board_1, old=".", new="~", x=1, y=1)
for a in modified_board:
    print(a)
