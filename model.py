"""
Reinforcement Learning for Tic-Tac-Toe: From Minimax to DQN

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - create_empty_board
import numpy as np

def create_empty_board():
    """Return an empty 3x3 Tic-Tac-Toe board as an int numpy array of zeros."""
    return np.array([[0,0,0],[0,0,0],[0,0,0]])

# Step 2 - encode_player
def encode_player(player):
    """Return the integer encoding for 'X', 'O', or 'empty'."""
    
    move_map = {
        'X':1,
        'O':-1,
        'empty':0
    }
    return move_map.get(player)

# Step 3 - print_board
import numpy as np

def print_board(board):
    """Print the 3x3 board using X, O, and . characters."""
    
    sym_map = {
        1:'X',
        -1:'O',
        0:'.'
    }
    for row in board:
        sym = [sym_map[cell] for cell in row]
        print(*sym)
    return None

# Step 4 - is_cell_empty
import numpy as np

def is_cell_empty(board, row, col):
    """Return True if board[row, col] is empty (0), else False."""
    if board[row][col] == 0:
        return True
    else:
        return False

# Step 5 - place_move
import numpy as np

def place_move(board, row, col, player):
    """Place player's mark at (row, col) and return the new board."""
    if is_cell_empty(board, row, col):
        board1 = board.copy()
        board1[row][col] = player
        return board1
    else:
        raise ValueError()

# Step 6 - get_legal_moves
import numpy as np

def get_legal_moves(board):
    """Return a list of (row, col) tuples for all empty cells on the board."""
    possibles = []
    for row in range(3):
        for col in range(3):
            if board[row,col] == 0:
                cell = (row,col)
                possibles.append(cell)
    return possibles

# Step 7 - check_row_win
import numpy as np

def check_row_win(board, player):
    """Return True if `player` has three-in-a-row across any row of `board`."""
    for row in range(3):
        if np.all(board[row] == player):
            return True
    return False

# Step 8 - check_column_win
import numpy as np

def check_column_win(board, player):
    """Return True if `player` has three-in-a-row in any column of `board`."""
    for row in range(3):
        for col in range(3):
            if np.all(board[:, col]==player):
                return True
    return False
    pass

# Step 9 - check_main_diagonal_win
import numpy as np

def check_main_diagonal_win(board, player):
    """Return True if `player` occupies all three main-diagonal cells."""
    if np.all(board.diagonal() == player):
        return True
    return False
    pass

# Step 10 - check_anti_diagonal_win
import numpy as np

def check_anti_diagonal_win(board, player):
    if np.all(np.fliplr(board).diagonal() == player):
        return True
    return False

# Step 11 - is_winner
import numpy as np

def is_winner(board, player):
    """Return True if `player` has three-in-a-row on `board`."""
    if check_anti_diagonal_win(board, player) == True or check_main_diagonal_win(board, player) == True or check_row_win(board, player) == True or check_column_win(board, player) == True:
        return True
    else:
        return False

# Step 12 - is_draw
import numpy as np

def is_draw(board):
    """Return True iff the board is full and neither player has won."""
    if not is_winner(board, 1) and not get_legal_moves(board) and not is_winner(board, -1):
        return True
    return False

# Step 13 - get_game_status
import numpy as np

def get_game_status(board):
    """Return 'X_win', 'O_win', 'draw', or 'ongoing' for the given 3x3 board."""
    if is_winner(board, 1):
        return 'X_win'
    elif is_winner(board, -1):
        return 'O_win'
    elif is_draw(board):
        return 'draw'
    else:
        return 'ongoing'

# Step 14 - get_current_player
import numpy as np

def get_current_player(board):
    """Return 1 if X is to move, -1 if O is to move."""
    x_count = np.sum(board == 1)
    o_count = np.sum(board == -1)

    if x_count == o_count:
        return 1      
    else:
        return -1

# Step 15 - switch_player
def switch_player(player):
    """Return the opponent of `player` (1 <-> -1)."""
    
    if player == 1:
        return -1
    else:
        return 1

# Step 16 - play_hardcoded_game
import numpy as np

def play_hardcoded_game(moves):
    """Replay a fixed sequence of (row, col) moves and return (final_board, status)."""
    b = create_empty_board()
    for r,c in moves:
        curr_player = get_current_player(b)
        b = place_move(b,r, c,curr_player)
        curr_status = get_game_status(b)
        
        if curr_status != 'ongoing':
            final_board = b
            status = curr_status
            return(final_board, status)
    return b, get_game_status(b)

# Step 17 - play_interactive_game
def play_interactive_game():
    """Play a full game with two humans entering moves via stdin and return the final status."""
    board = create_empty_board()
    while True:
        print_board(board)
        player=get_current_player(board)
        row, col = map(int, input().split())
        if not is_cell_empty(board, row, col):
            #print("illegal move, try again")
            continue

        board = place_move(board, row, col, player)
        status = get_game_status(board)
        if status != "ongoing":
            print_board(board)
            return status

# Step 18 - TicTacToeGame
class TicTacToeGame:
    """Stateful Tic-Tac-Toe environment wrapping the Part 1 engine."""

    def __init__(self):
        self.board = create_empty_board()
        self.current_player = 1
        self.status = "ongoing"

    def reset(self):
        self.board = create_empty_board()
        self.current_player = 1
        self.status = "ongoing"
        return self.board
        

    def legal_moves(self):
        moves = get_legal_moves(self.board)
        return moves

    def is_terminal(self):
        if get_game_status(self.board) != "ongoing":
            return True
        return False

    def step(self, row, col):
        if self.is_terminal():
            raise ValueError()


        self.board = place_move(self.board, row, col, self.current_player)
        self.status = get_game_status(self.board)
        if self.status == "ongoing":
            self.current_player = switch_player(self.current_player)
        return self.board, self.status

# Step 19 - random_move_agent
import numpy as np

def random_move_agent(board, player, rng):
    """Return a uniformly random legal (row, col) move for `player`."""
    
    moves = get_legal_moves(board)
    move = moves[rng.integers(len(moves))]
    return move

# Step 20 - play_random_vs_random_game
def play_random_vs_random_game(rng):
    """Simulate one full random-vs-random game and return the final status."""
    game = TicTacToeGame()
    while not game.is_terminal():
        row, col = random_move_agent(game.board, game.current_player, rng)
        game.step(row,col)
    return game.status

# Step 21 - play_random_vs_random_matches
def play_random_vs_random_matches(n_games, rng):
    """Run n_games random-vs-random games and return the list of outcome strings."""
    outcome = []
    for n in range(0,n_games):
        res = play_random_vs_random_game(rng)
        outcome.append(res)
    return outcome

# Step 22 - compute_outcome_rates
def compute_outcome_rates(outcomes):
    """Return {'x_win_rate','o_win_rate','draw_rate'} from a list of outcome labels."""
    if len(outcomes) == 0:
        return {
            "x_win_rate": 0.0,
            "o_win_rate": 0.0,
            "draw_rate": 0.0
        }

    outcome_map = {'X_win':0,'O_win':0,'draw':0}
    for o in outcomes:
        outcome_map[o] += 1
    rate_map = {
        'x_win_rate':outcome_map['X_win']/len(outcomes),
        'o_win_rate':outcome_map['O_win']/len(outcomes),
        'draw_rate':outcome_map['draw']/len(outcomes)
    }
    return rate_map

# Step 23 - minimax_terminal_score
def minimax_terminal_score(status):
    """Return +1 for 'X_win', -1 for 'O_win', 0 for 'draw'."""
    # minimax assumes perfect information, deterministic environment, perfect opponent, full searches of future states
    # RL assumes that optimalstrategy is unknown, will learn from experience, improve over many games
    #minimax gives the optimal policy, RL algorithm tries to learn a policy that approaches it
    #using zero-sum convention
    if status == 'X_win':
        return 1
    elif status == 'O_win':
        return -1
    else:
        return 0

# Step 24 - minimax_value
def minimax_value(board, player):
    """Return the minimax value of `board` with `player` to move."""
    status = get_game_status(board)

    if status != "ongoing":
        return minimax_terminal_score(status)

    child_values = []
    for row, col in get_legal_moves(board):
        next_board = place_move(board, row, col, player)
        next_player = switch_player(player)
        child_value = minimax_value(next_board, next_player)
        child_values.append(child_value)

    if player == 1:
        return max(child_values)
    return min(child_values)

# Step 25 - minimax_recursive
def minimax_recursive(board, player):
    """Return the minimax value of `board` with `player` to move."""
    cache = {}
    key = (board.tobytes(), player)
    if key in cache:
        return cache[key]
    status = get_game_status(board)
    if status != "ongoing":
        val = minimax_terminal_score(status)
        cache[key] =val
        return val
    child_values = []
    for row, col in get_legal_moves(board):
        next_board = place_move(board, row, col, player)
        next_player = switch_player(player)
        child_value = minimax_recursive(next_board, next_player)
        child_values.append(child_value)
    if player == 1:
        val = max(child_values)
    else:
        val = min(child_values)

    cache[key] = val
    return val

# Step 26 - minimax_max_min_step
import numpy as np

def minimax_max_min_step(board, player):
    """Return (best_score, best_move) after expanding one minimax level."""
    best_move=None
    moves=get_legal_moves(board)
    if player == 1:
        best_score = float("-inf")
        for row, col in moves:
            next_board = place_move(board, row, col, player)
            score = minimax_recursive(next_board, switch_player(player))

            if score > best_score:
                best_score = score
                best_move = (row, col)
    else:
        best_score = float("inf")

        for row, col in moves:
            next_board = place_move(board, row, col, player)
            score = minimax_recursive(next_board, switch_player(player))

            if score < best_score:
                best_score = score
                best_move = (row, col)

    return best_score, best_move

# Step 27 - minimax_best_move
def minimax_best_move(board, player):
    """Return the optimal (row, col) move for `player` via minimax."""
    best_score, best_move = minimax_max_min_step(board, player)
    return best_move

# Step 28 - minimax_alpha_beta
import numpy as np

def minimax_alpha_beta(board, player, alpha, beta):
    """Return (best_score, best_move) for `player` using alpha-beta pruning."""
    #best score for X in alpha, best score for O at beta

    alpha = float("-inf")
    beta = float("inf")
    status = get_game_status(board)
    if status != 'ongoing':
        return minimax_terminal_score(status), None
    best_move = None
    if player == 1:
        best_score = float("-inf")

        for r, c in get_legal_moves(board):
            next_board = place_move(board, r, c, player)
            score, m = minimax_alpha_beta(next_board, switch_player(player), alpha, beta)
            if score >best_score:
                best_score = score
                best_move= (r, c)
            alpha = max(alpha, best_score)
            #pruning rule
            if alpha >= beta:
                break
    else:
        best_score= float("inf")
        for r, c in get_legal_moves(board):
            next_board = place_move(board, r, c, player)
            score, m = minimax_alpha_beta(next_board, switch_player(player), alpha, beta)
            if score < best_score:
                best_score = score
                best_move = (r, c)
            beta = min (beta, best_score)
            #pruning rule
            if alpha >= beta:
                break
    return best_score, best_move

# Step 29 - play_minimax_vs_random_matches (not yet solved)
# TODO: implement

# Step 30 - play_minimax_vs_minimax_matches (not yet solved)
# TODO: implement

# Step 31 - encode_board_state_key (not yet solved)
# TODO: implement

# Step 32 - canonical_board_key (not yet solved)
# TODO: implement

# Step 33 - initialize_q_table (not yet solved)
# TODO: implement

# Step 34 - get_q_value (not yet solved)
# TODO: implement

# Step 35 - set_q_value (not yet solved)
# TODO: implement

# Step 36 - choose_learning_rate_alpha (not yet solved)
# TODO: implement

# Step 37 - choose_discount_factor_gamma (not yet solved)
# TODO: implement

# Step 38 - choose_initial_epsilon (not yet solved)
# TODO: implement

# Step 39 - epsilon_decay_schedule (not yet solved)
# TODO: implement

# Step 40 - epsilon_greedy_explore_move (not yet solved)
# TODO: implement

# Step 41 - epsilon_greedy_select_action (not yet solved)
# TODO: implement

# Step 42 - greedy_argmax_over_legal_actions (not yet solved)
# TODO: implement

# Step 43 - random_tie_break_argmax (not yet solved)
# TODO: implement

# Step 44 - tic_tac_toe_reward (not yet solved)
# TODO: implement

# Step 45 - q_learning_nonterminal_target (not yet solved)
# TODO: implement

# Step 46 - q_learning_terminal_target (not yet solved)
# TODO: implement

# Step 47 - q_learning_update (not yet solved)
# TODO: implement

# Step 48 - episode_reset_game (not yet solved)
# TODO: implement

# Step 49 - episode_agent_pick_action (not yet solved)
# TODO: implement

# Step 50 - episode_apply_action (not yet solved)
# TODO: implement

# Step 51 - episode_apply_q_update (not yet solved)
# TODO: implement

# Step 52 - episode_check_terminate (not yet solved)
# TODO: implement

# Step 53 - train_q_learning_agent (not yet solved)
# TODO: implement

# Step 54 - compute_batched_outcome_stats (not yet solved)
# TODO: implement

# Step 55 - self_play_episode (not yet solved)
# TODO: implement

# Step 56 - flip_board_perspective (not yet solved)
# TODO: implement

# Step 57 - perspective_reward_sign (not yet solved)
# TODO: implement

# Step 58 - train_q_agent_self_play (not yet solved)
# TODO: implement

# Step 59 - evaluate_q_agent_vs_random (not yet solved)
# TODO: implement

# Step 60 - evaluate_q_agent_vs_minimax (not yet solved)
# TODO: implement

# Step 61 - inspect_q_values_for_state (not yet solved)
# TODO: implement

# Step 62 - serialize_q_table_to_dict (not yet solved)
# TODO: implement

# Step 63 - deserialize_q_table_from_dict (not yet solved)
# TODO: implement

# Step 64 - encode_board_flat_length_nine (not yet solved)
# TODO: implement

# Step 65 - encode_board_one_hot_length_eighteen (not yet solved)
# TODO: implement

# Step 66 - build_mlp_architecture (not yet solved)
# TODO: implement

# Step 67 - initialize_mlp_parameters (not yet solved)
# TODO: implement

# Step 68 - mlp_forward_pass (not yet solved)
# TODO: implement

# Step 69 - mask_illegal_actions_neg_inf (not yet solved)
# TODO: implement

# Step 70 - argmax_action_from_q_values (not yet solved)
# TODO: implement

# Step 71 - mse_loss_on_chosen_action (not yet solved)
# TODO: implement

# Step 72 - mlp_backward_pass (not yet solved)
# TODO: implement

# Step 73 - adam_update_step (not yet solved)
# TODO: implement

# Step 74 - create_replay_buffer (not yet solved)
# TODO: implement

# Step 75 - append_transition_to_buffer (not yet solved)
# TODO: implement

# Step 76 - cap_buffer_size_drop_oldest (not yet solved)
# TODO: implement

# Step 77 - sample_minibatch_from_buffer (not yet solved)
# TODO: implement

# Step 78 - build_target_network_copy (not yet solved)
# TODO: implement

# Step 79 - compute_target_q_with_target_network (not yet solved)
# TODO: implement

# Step 80 - sync_target_network_periodically (not yet solved)
# TODO: implement

# Step 81 - dqn_select_action (not yet solved)
# TODO: implement

# Step 82 - dqn_train_step (not yet solved)
# TODO: implement

# Step 83 - train_dqn_agent (not yet solved)
# TODO: implement

# Step 84 - compare_dqn_tabular_random_minimax (not yet solved)
# TODO: implement

# Step 85 - sarsa_on_policy_update (not yet solved)
# TODO: implement

# Step 86 - train_sarsa_agent (not yet solved)
# TODO: implement

# Step 87 - reinforce_log_prob_of_action (not yet solved)
# TODO: implement

# Step 88 - reinforce_collect_episode_returns (not yet solved)
# TODO: implement

# Step 89 - reinforce_policy_gradient_update (not yet solved)
# TODO: implement

# Step 90 - train_reinforce_agent (not yet solved)
# TODO: implement

# Step 91 - compare_value_vs_policy_learners (not yet solved)
# TODO: implement

# Step 92 - symmetry_augmented_training (not yet solved)
# TODO: implement

