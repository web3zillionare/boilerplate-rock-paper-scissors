import random

def player(prev_play, opponent_history=[], strategy_state={"strategy": "frequency", "wins": 0, "losses": 0, "games": 0}):
    # Update the opponent's history
    if prev_play != '':
        opponent_history.append(prev_play)

    # Initialize default move and strategy counters
    guess = "R"
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    freq_based_guess = "R"
    pattern_based_guess = "R"

    # Step 1: Frequency Analysis
    move_freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        if move in move_freq:
            move_freq[move] += 1
    # Find the opponent's most frequent move and choose its counter
    most_frequent_move = max(move_freq, key=move_freq.get)
    freq_based_guess = counter_moves[most_frequent_move]

    # Step 2: Pattern Recognition
    pattern_length = 3
    if len(opponent_history) >= pattern_length:
        recent_pattern = tuple(opponent_history[-pattern_length:])
        pattern_dict = {}
        for i in range(len(opponent_history) - pattern_length):
            pattern = tuple(opponent_history[i:i+pattern_length])
            next_move = opponent_history[i + pattern_length]
            if pattern not in pattern_dict:
                pattern_dict[pattern] = {"R": 0, "P": 0, "S": 0}
            pattern_dict[pattern][next_move] += 1

        if recent_pattern in pattern_dict:
            likely_next_move = max(pattern_dict[recent_pattern], key=pattern_dict[recent_pattern].get)
            pattern_based_guess = counter_moves[likely_next_move]
        else:
            pattern_based_guess = freq_based_guess
    else:
        pattern_based_guess = freq_based_guess

    # Step 3: Strategy Switching Logic
    # Strategy switching based on pattern recognition and frequency analysis
    if len(opponent_history) >= pattern_length:
        guess = pattern_based_guess
    else:
        guess = freq_based_guess

    # Return the final guess based on chosen strategy
    return guess
