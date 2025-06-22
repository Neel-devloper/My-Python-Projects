
# Import the Pygame library for creating the game window, handling graphics, and managing user input
import pygame

# Import the python-chess library for chess logic, including board state and legal move validation
import chess
from fontTools.subset import prune_hints

# Import a custom chess engine module, likely containing the logic for Black's moves
import NV_Chess_engine
import keyboard

# Initialize Pygame to set up its internal components for graphics, sound, and input handling
pygame.init()

THEMES = [
    ((240, 217, 181), (181, 136, 99)),  # Classic
    ((255, 255, 255), (0, 0, 0)),       # Black & White
    ((200, 200, 255), (100, 100, 200)), # Cool Blue
    ((255, 228, 196), (139, 69, 19)),   # Brown
    ((152, 251, 152), (34, 139, 34)),    # Green
    ((152, 251, 152), (34, 139, 34)),  # Green
    ((255, 192, 203), (255, 105, 180)),  # Pink
    ((255, 255, 224), (128, 128, 0)),  # Yellow Olive
    ((173, 216, 230), (0, 191, 255)),  # Sky Blue
    ((211, 211, 211), (105, 105, 105)),  # Grey
    ((255, 250, 240), (160, 82, 45))  # Antique White and Saddle Brown
]
theme_index = 0

# Define the size of each chessboard square in pixels (100x100)
SQUARE_SIZE = 100

# Create an 800x800 pixel game window for the 8x8 chessboard (8 squares x 100 pixels each)
SCREEN = pygame.display.set_mode((SQUARE_SIZE * 8, SQUARE_SIZE * 8))

# Set the window title to "Chess"
pygame.display.set_caption("Chess")

# Create a clock object to control the game's frame rate
clock = pygame.time.Clock()

LIGHT_COLOR, DARK_COLOR = THEMES[theme_index]




# List of chess piece types to be used for loading images
PIECE_TYPES = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']

# Initialize an empty dictionary to store piece images, keyed by (color, piece_type)
IMAGES = {}

# Loop over both piece colors: 'white' and 'black'
for color in ['white', 'black']:
    # Loop over each piece type in PIECE_TYPES
    for piece in PIECE_TYPES:
        # If the color is 'white', define file paths for white piece images
        if color == 'white':
            path_map = {
                'pawn': '/Users/neelvorani/Desktop/python pycharm projects/assets/white pawn img chess.png',
                'rook': '/Users/neelvorani/Desktop/python pycharm projects/assets/white rook img chess.png',
                'knight': '/Users/neelvorani/Desktop/python pycharm projects/assets/white knight img chess.png',
                'bishop': '/Users/neelvorani/Desktop/python pycharm projects/assets/white bishop img chess.png',
                'queen': '/Users/neelvorani/Desktop/python pycharm projects/assets/white queen img chess.png',
                'king': '/Users/neelvorani/Desktop/python pycharm projects/assets/white king img chess .png'
            }
        # If the color is 'black', define file paths for black piece images
        else:
            path_map = {
                'pawn': '/Users/neelvorani/Desktop/python pycharm projects/assets/pawn img chess.png',
                'rook': '/Users/neelvorani/Desktop/python pycharm projects/assets/rook img chess.png',
                'knight': '/Users/neelvorani/Desktop/python pycharm projects/assets/knight img chess.png',
                'bishop': '/Users/neelvorani/Desktop/python pycharm projects/assets/bishop img chess.png',
                'queen': '/Users/neelvorani/Desktop/python pycharm projects/assets/queen img chess.png',
                'king': '/Users/neelvorani/Desktop/python pycharm projects/assets/king img chess.png'
            }
        # Load the image from the specified path, scale it to SQUARE_SIZE (100x100), and store it in IMAGES
        IMAGES[(color, piece)] = pygame.transform.scale(pygame.image.load(path_map[piece]), (SQUARE_SIZE, SQUARE_SIZE))

# Initialize a new chess board with the standard starting position using the python-chess library
BOARD = chess.Board()

# Variable to track the currently selected square (None means no square is selected)
SELECTED_SQUARE = None

# Flag to control the main game loop (True keeps the game running)
running = True

# Start the main game loop, which continues until running becomes False
while running:
    # Process all events in the Pygame event queue (e.g., mouse clicks, window close)
    for event in pygame.event.get():
        # If the user clicks the window's close button
        if event.type == pygame.QUIT:
            # Set running to False to exit the game loop
            running = False
        # If a mouse button is pressed and it's White's turn to move
        elif event.type == pygame.MOUSEBUTTONDOWN and BOARD.turn == chess.WHITE:
            # Get the (x, y) pixel coordinates of the mouse click
            pos = pygame.mouse.get_pos()
            # Convert the x-coordinate to a column number (0-7) by integer division with SQUARE_SIZE
            screen_col = pos[0] // SQUARE_SIZE
            # Convert the y-coordinate to a row number (0-7) by integer division with SQUARE_SIZE
            screen_row = pos[1] // SQUARE_SIZE
            # Convert screen row to chess rank (0 is rank 1 at bottom, 7 is rank 8 at top)
            board_row = 7 - screen_row
            # Column directly maps to chess files a-h (0 is a, 7 is h)
            board_col = screen_col
            # Calculate the square index (0-63) used by python-chess (row * 8 + col)
            square = board_row * 8 + board_col

            # If no square is currently selected
            if SELECTED_SQUARE is None:
                # Get the piece at the clicked square
                piece = BOARD.piece_at(square)
                # If there is a piece and it’s White (user plays as White)
                if piece and piece.color == chess.WHITE:
                    # Select this square by storing its index
                    SELECTED_SQUARE = square
            # If a square is already selected
            else:
                # If the clicked square is different from the selected square
                if SELECTED_SQUARE != square:
                    # Store the starting square (selected square)
                    from_square = SELECTED_SQUARE
                    # Store the destination square (clicked square)
                    to_square = square
                    # Get the piece at the starting square
                    piece = BOARD.piece_at(from_square)
                    # If the piece is a pawn and it’s moving to the 8th rank (top row for White)
                    if piece.piece_type == chess.PAWN and to_square // 8 == 7:
                        # Create a move with pawn promotion to a queen
                        move = chess.Move(from_square, to_square, promotion=chess.QUEEN)
                    # For all other moves (no promotion)
                    else:
                        # Create a standard move without promotion
                        move = chess.Move(from_square, to_square)
                    # Check if the move is legal according to the current board state
                    if move in BOARD.legal_moves:
                        # Apply the move to the board, which also switches the turn to Black
                        BOARD.push(move)
                        # Reset the selected square since the move is complete
                        SELECTED_SQUARE = None
                        # Call the custom chess engine to make a move for Black
                        NV_Chess_engine.black_move(BOARD)
                        print(f'score : {NV_Chess_engine.evaluate_position(BOARD)}')
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                theme_index = 0
            elif event.key == pygame.K_2:
                theme_index = 1
            elif event.key == pygame.K_3:
                theme_index = 2
            elif event.key == pygame.K_4:
                theme_index = 3
            elif event.key == pygame.K_5:
                theme_index = 4
            elif event.key == pygame.K_6:
                theme_index = 5
            elif event.key == pygame.K_7:
                theme_index = 6
            elif event.key == pygame.K_8:
                theme_index = 7
            elif event.key == pygame.K_9:
                theme_index = 8
            elif event.key == pygame.K_0:
                theme_index = 9


    LIGHT_COLOR, DARK_COLOR = THEMES[theme_index]

    # Draw the chessboard by iterating over all rows and columns
    for screen_row in range(8):
        for screen_col in range(8):
            # Calculate the x-pixel position of the square (column * square size)
            x = screen_col * SQUARE_SIZE
            # Calculate the y-pixel position of the square (row * square size)
            y = screen_row * SQUARE_SIZE
            # Convert screen row to chess rank (0 is rank 1, 7 is rank 8)
            board_row = 7 - screen_row
            # Column maps directly to chess files (0 is a, 7 is h)
            board_col = screen_col
            # Determine square color: light if row + col is even, dark if odd (standard chess pattern)
            color = LIGHT_COLOR if (board_row + board_col) % 2 == 0 else DARK_COLOR
            # Draw a rectangle for the square with the chosen color at position (x, y)
            pygame.draw.rect(SCREEN, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

            # Calculate the square index (0-63) for this position
            square = board_row * 8 + board_col
            # Get the piece at this square, if any
            piece = BOARD.piece_at(square)
            # If there is a piece on this square
            if piece:
                # Determine the piece’s color ('white' if True, 'black' if False)
                color = 'white' if piece.color else 'black'
                # Map the piece type (1-6) to its name (pawn=1, knight=2, etc., adjusted by -1 for list index)
                piece_type = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king'][piece.piece_type - 1]
                # Draw the piece image at the square’s position using the preloaded image
                SCREEN.blit(IMAGES[(color, piece_type)], (x, y))

    if BOARD.is_checkmate() and BOARD.turn == chess.WHITE:
        font = pygame.font.Font('freesansbold.ttf',32)
        text = font.render('Black Won!',True,(0,255,0),(0,0,255))
        textRect = text.get_rect()
        textRect.center = (400,400)
    elif BOARD.is_checkmate() and BOARD.turn == chess.BLACK:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('White Won!', True, (0, 255, 0), (0, 0, 255))
        textRect = text.get_rect()
        textRect.center = (400, 400)

    # Update the display to reflect all drawing operations (show the current board state)
    pygame.display.flip()

    # Limit the frame rate to 60 FPS to avoid excessive CPU usage
    clock.tick(60)

# Clean up Pygame resources and close the window when the game loop exits
pygame.quit()
