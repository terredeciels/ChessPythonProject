import time

import chess


# Custom perft implementation
def custom_perft(board, depth):
    if depth == 0:
        return 1
    nodes = 0
    for move in board.legal_moves:
        board.push(move)
        nodes += custom_perft(board, depth - 1)
        board.pop()
    return nodes


# Python-Chess perft implementation
def chess_library_perft(board, depth):
    if depth == 0:
        return 1
    nodes = 0
    for move in board.legal_moves:
        board.push(move)
        nodes += chess_library_perft(board, depth - 1)
        board.pop()
    return nodes


# Correct FEN with both kings and two rooks
fen_position = "8/8/8/8/8/8/4K3/R6k w - - 0 1"
board = chess.Board(fen_position)

# Depth levels to test
depths = [1, 2, 3, 4, 5, 6]

# Measure and calculate results for custom perft
results_custom = {}
for depth in depths:
    start_time = time.time()
    nodes = custom_perft(board, depth)
    elapsed_time = time.time() - start_time
    results_custom[depth] = (nodes, elapsed_time)

# Measure and calculate results for python-chess perft
results_library = {}
for depth in depths:
    start_time = time.time()
    nodes = chess_library_perft(board, depth)
    elapsed_time = time.time() - start_time
    results_library[depth] = (nodes, elapsed_time)

# Verify equality for each depth and save the results, including output in the console
output_path_verification = "perft_verification_with_output.txt"

verification_output = ["Verification of Custom Perft and Python-Chess Perft Results:\n"]
all_passed = True
for depth in depths:
    custom_nodes = results_custom[depth][0]
    library_nodes = results_library[depth][0]
    if custom_nodes == library_nodes:
        verification_output.append(f"Depth {depth}: PASS (Nodes: {custom_nodes})\n")
    else:
        verification_output.append(f"Depth {depth}: FAIL (Custom: {custom_nodes}, Library: {library_nodes})\n")
        all_passed = False
if all_passed:
    verification_output.append("\nOverall Result: PASS\n")
else:
    verification_output.append("\nOverall Result: FAIL\n")

# Write to file
with open(output_path_verification, "w") as file:
    file.writelines(verification_output)

# Print output in the console
verification_output_text = "".join(verification_output)
print(verification_output_text)
