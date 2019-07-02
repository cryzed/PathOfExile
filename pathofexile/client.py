from pathofexile import xdotool

PATH_OF_EXILE_CLASSNAME_REGEX = r'^pathofexile_x64\.exe$'


def find_path_of_exile_window():
    return xdotool.search(['--onlyvisible', '--limit', '1', '--classname', PATH_OF_EXILE_CLASSNAME_REGEX])


def type_chat_message(window_id, message, submit=True):
    xdotool.windowactivate(window_id)
    xdotool.key(window_id, ['KP_Enter'])
    xdotool.type_(window_id, message)
    if submit:
        xdotool.key(window_id, ['KP_Enter'])
