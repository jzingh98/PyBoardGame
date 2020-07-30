class Entity:
    def __init__(self, icon, top_left_x, top_left_y, width, height):
        self.icon = icon
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height


def draw_entity(entity, board):
    boardHeight = len(board)
    boardWidth = len(board[0])

    # Ensure valid board dimensions
    if boardHeight * boardWidth == 0:
        return False

    # Ensure bounds
    if entity.top_left_x + entity.width - 1 > boardWidth:
        return False
    if entity.top_left_y + entity.height - 1 > boardHeight:
        return False

    # Add entity to board
    for i in range(entity.top_left_y, entity.top_left_y + entity.height):
        for j in range(entity.top_left_x, entity.top_left_x + entity.width):
            # Check for conflict
            if board[i][j] != "_":
                return False
            # Otherwise, insert unit
            board[i][j] = entity.icon

    return True


b = [['_'] * 6 for i in range(7)]
e = Entity('Y', 2, 0, 2, 4)
print(draw_entity(e, b))
for row in b:
    print(row)
