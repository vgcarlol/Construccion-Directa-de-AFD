def simulate_afd(afd, string):
    current_state = afd
    for char in string:
        if char in current_state.transitions:
            current_state = current_state.transitions[char]
        else:
            return False
    return current_state.is_final
