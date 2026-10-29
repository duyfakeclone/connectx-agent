def my_agent(observation, configuration):
    from random import choice
    return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(obs,config):
    #Defining a smarter agent
    def drop_piece(grid,config,col,piece):
        brd=grid.copy()
        for rows in range(config.rows-1,-1,-1):
            if brd[rows][col] == 0:
                brd[rows][col] = piece
                break
        return brd

    def winning_move_exist(obs,config,col,piece):
        grid = np.asarray(obs.board).reshape(config.rows,config.columns)
        next_grid = drop_piece(grid,config,col,piece)
        for cols in range(config.columns): # Vertical
            for rows in range(config.rows-config.inarow+1):
                window = [next_grid[rows+i][cols] for i in range(config.inarow)]
                if window.count(piece) == config.inarow:
                    return True
        for rows in range(config.rows): # Horizontal
            for cols in range(config.columns-config.inarow+1):
                window = [next_grid[rows][cols+i] for i in range(config.inarow)]
                if window.count(piece) == config.inarow:
                    return True
        for rows in range(config.rows-config.inarow+1): #Right diagonal
            for cols in range(config.columns-config.inarow+1):
                window = [next_grid[rows+i][cols+i] for i in range(config.inarow)]
                if window.count(piece) == config.inarow:
                    return True
        for rows in range(config.inarow-1,config.rows): #Left diagonal
                for cols in range(config.columns-config.inarow+1):
                    window = [next_grid[rows-i][cols+i] for i in range(config.inarow)]
                    if window.count(piece) == config.inarow:
                        return True
        return False
    def find_enemy_winning_move(obs,config,piece):
        for cols in range(config.columns):
            if obs.board[cols] == 0:
                if winning_move_exist(obs,config,cols,piece):
                    return cols
        return None
    from random import choice
    choices = [c for c in range(config.columns) if obs.board[c] ==0 ]
    for c in choices: 
        if winning_move_exist(obs,config,c,obs.mark)==True:
            return c
    if find_enemy_winning_move(obs,config,3-obs.mark) != None:
        return find_enemy_winning_move(obs,config,3-obs.mark)
    return choice(choices)
def my_agent(obs,config):
    #Defining a smarter agent
    def drop_piece(grid,config,col,piece):
        brd=grid.copy()
        for rows in range(config.rows-1,-1,-1):
            if brd[rows][col] == 0:
                brd[rows][col] = piece
                break
        return brd

    def winning_move_exist(obs,config,col,piece):
        grid = np.asarray(obs.board).reshape(config.rows,config.columns)
        next_grid = drop_piece(grid,config,col,piece)
        for cols in range(config.columns): # Vertical
            for rows in range(config.rows-config.inarow+1):
                window = [next_grid[rows+i][cols] for i in range(config.inarow)]
                if window.count(piece) == config.inarow:
                    return True
        for rows in range(config.rows): # Horizontal
            for cols in range(config.columns-config.inarow+1):
                window = [next_grid[rows][cols+i] for i in range(config.inarow)]
                if window.count(piece) == config.inarow:
                    return True
        for rows in range(config.rows-config.inarow+1): #Right diagonal
            for cols in range(config.columns-config.inarow+1):
                window = [next_grid[rows+i][cols+i] for i in range(config.inarow)]
                if window.count(piece) == config.inarow:
                    return True
        for rows in range(config.inarow-1,config.rows): #Left diagonal
                for cols in range(config.columns-config.inarow+1):
                    window = [next_grid[rows-i][cols+i] for i in range(config.inarow)]
                    if window.count(piece) == config.inarow:
                        return True
        return False
    def find_enemy_winning_move(obs,config,piece):
        for cols in range(config.columns):
            if obs.board[cols] == 0:
                if winning_move_exist(obs,config,cols,piece):
                    return cols
        return None
    from random import choice
    choices = [c for c in range(config.columns) if obs.board[c] ==0 ]
    for c in choices: 
        if winning_move_exist(obs,config,c,obs.mark)==True:
            return c
    if find_enemy_winning_move(obs,config,3-obs.mark) != None:
        return find_enemy_winning_move(obs,config,3-obs.mark)
    return choice(choices)
def my_agent(obs,config):
    #Defining a smarter agent
    def drop_piece(grid,config,col,piece):
        brd=grid.copy()
        for rows in range(config.rows-1,-1,-1):
            if brd[rows][col] == 0:
                brd[rows][col] = piece
                break
        return brd

    def winning_move_exist(obs,config,col,piece):
        grid = np.asarray(obs.board).reshape(config.rows,config.columns)
        next_grid = drop_piece(grid,config,col,piece)
        for cols in range(config.columns): # Vertical
            for rows in range(config.rows-config.inarow+1):
                window = [next_grid[rows+i][cols] for i in range(config.inarow)]
                if window.count(piece) == config.inarow:
                    return True
        for rows in range(config.rows): # Horizontal
            for cols in range(config.columns-config.inarow+1):
                window = [next_grid[rows][cols+i] for i in range(config.inarow)]
                if window.count(piece) == config.inarow:
                    return True
        for rows in range(config.rows-config.inarow+1): #Right diagonal
            for cols in range(config.columns-config.inarow+1):
                window = [next_grid[rows+i][cols+i] for i in range(config.inarow)]
                if window.count(piece) == config.inarow:
                    return True
        for rows in range(config.inarow-1,config.rows): #Left diagonal
                for cols in range(config.columns-config.inarow+1):
                    window = [next_grid[rows-i][cols+i] for i in range(config.inarow)]
                    if window.count(piece) == config.inarow:
                        return True
        return False
    def find_enemy_winning_move(obs,config,piece):
        for cols in range(config.columns):
            if obs.board[cols] == 0:
                if winning_move_exist(obs,config,cols,piece):
                    return cols
        return None
    from random import choice
    import numpy as np
    choices = [c for c in range(config.columns) if obs.board[c] ==0 ]
    for c in choices: 
        if winning_move_exist(obs,config,c,obs.mark)==True:
            return c
    if find_enemy_winning_move(obs,config,3-obs.mark) != None:
        return find_enemy_winning_move(obs,config,3-obs.mark)
    return choice(choices)
def my_agent(obs, config):
    import numpy as np

    # Cache winning lines to avoid recalculating them on every single turn
    if not hasattr(my_agent, "windows_cache"):
        my_agent.windows_cache = {}

    key = (config.rows, config.columns, config.inarow)
    if key not in my_agent.windows_cache:
        windows = []
        # Horizontal
        for r in range(config.rows):
            for c in range(config.columns - config.inarow + 1):
                windows.append([r * config.columns + c + i for i in range(config.inarow)])
        # Vertical
        for r in range(config.rows - config.inarow + 1):
            for c in range(config.columns):
                windows.append([(r + i) * config.columns + c for i in range(config.inarow)])
        # Positive diagonal (top-left to bottom-right)
        for r in range(config.rows - config.inarow + 1):
            for c in range(config.columns - config.inarow + 1):
                windows.append([(r + i) * config.columns + c + i for i in range(config.inarow)])
        # Negative diagonal (bottom-left to top-right)
        for r in range(config.inarow - 1, config.rows):
            for c in range(config.columns - config.inarow + 1):
                windows.append([(r - i) * config.columns + c + i for i in range(config.inarow)])
        my_agent.windows_cache[key] = windows

    windows = my_agent.windows_cache[key]
    board = obs.board
    mark = obs.mark
    opp_mark = mark % 2 + 1
    inarow = config.inarow

    # Optimized Heuristic: Uses 1D array and simple integer counting (no list slicing)
    def get_heuristic(current_board):
        score = 0
        for w in windows:
            m_count = 0
            o_count = 0
            e_count = 0
            for i in w:
                if current_board[i] == mark:
                    m_count += 1
                elif current_board[i] == opp_mark:
                    o_count += 1
                else:
                    e_count += 1

            if m_count == inarow:
                score += 1e6
            elif m_count == inarow - 1 and e_count == 1:
                score += 1
            elif o_count == inarow - 1 and e_count == 1:
                score -= 1e2
            elif o_count == inarow:
                score -= 1e4
        return score

    # Optimized Minimax with Alpha-Beta Pruning
    def minimax(current_board, depth, maximizingPlayer, alpha, beta):
        # Fast terminal win check using precomputed 1D windows
        for w in windows:
            first = current_board[w[0]]
            if first != 0 and all(current_board[i] == first for i in w):
                if first == mark:
                    return 1e9 + depth
                else:
                    return -1e9 - depth

        # Fast draw check (if top row has no zeros, board is full)
        if all(current_board[c] != 0 for c in range(config.columns)):
            return 0

        if depth == 0:
            return get_heuristic(current_board)

        valid_moves = [c for c in range(config.columns) if current_board[c] == 0]

        # Sorting moves by proximity to the center column dramatically increases 
        # alpha-beta pruning efficiency because better moves are evaluated first.
        center_col = config.columns // 2
        valid_moves.sort(key=lambda c: abs(c - center_col))

        if maximizingPlayer:
            value = -np.inf
            for col in valid_moves:
                # Find lowest empty row in this column (1D index math)
                for r in range(config.rows - 1, -1, -1):
                    idx = r * config.columns + col
                    if current_board[idx] == 0:
                        new_board = current_board.copy() # Fast 1D list copy
                        new_board[idx] = mark
                        break

                score = minimax(new_board, depth - 1, False, alpha, beta)
                value = max(value, score)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break # Alpha-beta cutoff
            return value
        else:
            value = np.inf
            for col in valid_moves:
                for r in range(config.rows - 1, -1, -1):
                    idx = r * config.columns + col
                    if current_board[idx] == 0:
                        new_board = current_board.copy()
                        new_board[idx] = opp_mark
                        break

                score = minimax(new_board, depth - 1, True, alpha, beta)
                value = min(value, score)
                beta = min(beta, value)
                if alpha >= beta:
                    break # Alpha-beta cutoff
            return value

    # Root Execution
    valid_moves = [c for c in range(config.columns) if board[c] == 0]
    if not valid_moves:
        return 0

    # Apply center preference to root moves as well
    center_col = config.columns // 2
    valid_moves.sort(key=lambda c: abs(c - center_col))

    best_score = -np.inf
    best_col = valid_moves[0]
    alpha = -np.inf

    # Tune this if you want deeper lookahead
    N_STEPS = 5

    for col in valid_moves:
        for r in range(config.rows - 1, -1, -1):
            idx = r * config.columns + col
            if board[idx] == 0:
                new_board = board.copy()
                new_board[idx] = mark
                break

        score = minimax(new_board, N_STEPS - 1, False, alpha, np.inf)

        if score > best_score:
            best_score = score
            best_col = col

        # Pass the best score found so far to prune subsequent sibling branches
        alpha = max(alpha, best_score)

    return best_col
