def update_difficulty(difficulties, selected_difficulty, difficulty_number=None):

    for i, difficulty in enumerate(difficulties):
        for key in difficulty.keys():
            if key == selected_difficulty:
                difficulty[key] = 'checked'
                difficulty_number = i
            else:
                difficulty[key] = ''

    return difficulties, difficulty_number
