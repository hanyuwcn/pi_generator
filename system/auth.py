import config

def authentication():
    counter = 0
    while input(config.PASSWORD_MESSAGE) != config.PASSWORD:
        counter += 1
        if counter == config.PASSWORD_INCORRECT_COUNTER:
            return False

    return True