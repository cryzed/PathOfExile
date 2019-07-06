import subprocess

from loguru import logger


def run(arguments):
    logger.debug(' '.join(arguments))
    process = subprocess.run(arguments, stdout=subprocess.PIPE, universal_newlines=True)
    return process.stdout.strip()


def search(query):
    return run(['xdotool', 'search', *query])


def windowactivate(window_id):
    run(['xdotool', 'windowactivate', '--sync', str(window_id)])


def key(window_id, keys):
    run(['xdotool', 'key', '--delay', '0', '--window', str(window_id), *keys])


def type_(window_id, text):
    run(['xdotool', 'type', '--delay', '0', '--clearmodifiers', '--window', str(window_id), text])
