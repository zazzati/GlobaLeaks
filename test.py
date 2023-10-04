def move_knight(current_square, target_square):
  """Moves a knight from the current square to the target square.

  Args:
    current_square: The current square of the knight.
    target_square: The target square of the knight.

  Returns:
    A list of knight moves, starting with the current square and ending with the
    target square.
  """

  knight_moves = []
  while current_square != target_square:
    # Identify the possible knight moves from the current square.
    possible_moves = [
        (current_square[0] + 2, current_square[1] + 1),
        (current_square[0] + 2, current_square[1] - 1),
        (current_square[0] - 2, current_square[1] + 1),
        (current_square[0] - 2, current_square[1] - 1),
        (current_square[0] + 1, current_square[1] + 2),
        (current_square[0] + 1, current_square[1] - 2),
        (current_square[0] - 1, current_square[1] + 2),
        (current_square[0] - 1, current_square[1] - 2),
    ]

    # Eliminate any possible moves that are blocked by other pieces.

    # Choose the knight move that gets you closest to the target square.

    # Move the knight to the chosen square.

    current_square = possible_moves[0]
    knight_moves.append(current_square)

  return knight_moves


# Example usage:

knight_moves = move_knight('h7', 'a2')

# Print the knight moves.

for move in knight_moves:
  print(move)
