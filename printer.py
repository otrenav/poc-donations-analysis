
def print_header(msg, config, level, verbose=False):
    if not(config['printer']['verbose'] or verbose):
        return
    print(str(level) * config['printer']['width'])
    print(msg)
    print(str(level) * config['printer']['width'])


def print_message(msg, config, verbose=False):
    if not(config['printer']['verbose'] or verbose):
        return
    print(msg)
