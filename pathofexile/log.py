import collections
import enum
import re
from datetime import datetime

DATETIME_FORMAT = '%Y/%m/%d %H:%M:%S'
LOG_MESSAGE_REGEX = re.compile(r'(?P<datetime>.+? .+?)\s+?(?P<unknown1>.+?)\s+?(?P<type>.+?)\s+?\[(?P<level>.+?)\s+?(?P<scope>.+?)\s+?(?P<unknown2>.+?)\]\s+?(?P<data>.+)')
CHAT_MESSAGE_REGEX_PATTERN = re.compile(r'(?P<type>#|\$|%|@From|@To|&)?\s*(?:<(?P<guild>.+?)>)?\s*(?P<username>.*?):(?:\s(?P<message>.+))?')
LogEntry = collections.namedtuple('LogEntry', ['date', 'type', 'data', 'raw'])
ChatMessage = collections.namedtuple('ChatMessage', ['type', 'source', 'target', 'message'])
User = collections.namedtuple('User', ['name', 'guild'])


class ParseError(Exception):
    pass


@enum.unique
class LogType(enum.Enum):
    Chat = enum.auto()
    Unknown = enum.auto()


@enum.unique
class ChatType(enum.Enum):
    Local = enum.auto()
    Global = enum.auto()
    Party = enum.auto()
    Whisper = enum.auto()
    Trade = enum.auto()
    Guild = enum.auto()


@enum.unique
class ChatObject(enum.Enum):
    Self = enum.auto()
    Party = enum.auto()
    Game = enum.auto()

    Local = enum.auto()
    Global = enum.auto()
    Trade = enum.auto()
    Guild = enum.auto()


LOG_TYPE_IDS = {
    'aa4': LogType.Chat,
    'aa1': LogType.Chat
}


def parse_log_entry(entry):
    match = LOG_MESSAGE_REGEX.match(entry)
    if not match:
        raise ParseError(entry)

    entry = match.groupdict()
    log_type = LOG_TYPE_IDS.get(entry['type'], LogType.Unknown)
    if log_type is LogType.Chat:
        data = parse_chat_message(entry['data'])
    else:
        data = entry['data']

    date = datetime.strptime(entry['datetime'], DATETIME_FORMAT)
    return LogEntry(date, log_type, data, entry)


def parse_chat_message(message):
    match = CHAT_MESSAGE_REGEX_PATTERN.match(message)
    if not match:
        raise ParseError(message)

    data = match.groupdict()
    type_ = data['type']
    if type_ == '#':
        type_ = ChatType.Global
        source = User(data['username'], data['guild'])
        target = ChatObject.Global
    elif type_ == '%':
        type_ = ChatType.Party
        source = User(data['username'], data['guild'])
        target = ChatObject.Party
    elif type_ == '$':
        type_ = ChatType.Trade
        source = User(data['username'], data['guild'])
        target = ChatObject.Trade
    elif type_ == '&':
        type_ = ChatType.Guild
        source = User(data['username'], data['guild'])
        target = ChatObject.Guild
    elif type_ == '@From':
        type_ = ChatType.Whisper
        source = User(data['username'], data['guild'])
        target = ChatObject.Self
    elif type_ == '@To':
        type_ = ChatType.Whisper
        source = ChatObject.Self
        target = User(data['username'], data['guild'])
    else:
        type_ = ChatType.Local
        source = data['username'] or ChatObject.Game
        target = ChatObject.Self

    return ChatMessage(type_, source, target, data['message'])
