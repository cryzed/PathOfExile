import io
import re
import time

from PySide2 import QtCore
from PySide2.QtCore import QThread
from loguru import logger

import pathofexile.log
from pathofexile.log import ChatObject, ChatType, LogType

ENCODING = 'UTF-8'

# poe.trade
TRADE_MESSAGE_REGEX = re.compile(
    r'Hi, I would like to buy your (?P<item>.+?) listed for (?P<price>.+?) in (?P<league>.+?) \(stash tab \"(?P<stash>.+?)\"; position: left (?P<left>.+?), top (?P<top>.+?)\)')


# TODO: yield multiple new lines at once, don't bottleneck through the calling interval
def tail(file):
    file.seek(io.SEEK_SET, io.SEEK_END)
    while True:
        position = file.tell()
        line = file.readline()
        if not line:
            file.seek(position)
            continue

        yield line


class LogParser(QThread):
    trade_request = QtCore.Signal(dict)

    def __init__(self, path, interval=0.1):
        super().__init__()
        self.path = path
        self.interval = interval

    def run(self):
        log = tail(open(self.path, encoding=ENCODING))
        for line in log:
            try:
                entry = pathofexile.log.parse_log_entry(line.strip())
            except pathofexile.log.ParseError as error:
                logger.warning('Parse error: {!r}', error)
                continue

            received_whisper = (
                    entry.type is LogType.Chat and
                    entry.data.type is ChatType.Whisper and
                    entry.data.target is ChatObject.Self)
            if not received_whisper:
                continue

            match = TRADE_MESSAGE_REGEX.match(entry.data.message)
            if match:
                data = match.groupdict()
                data['buyer'] = entry.data.source.name
                data['guild'] = entry.data.source.guild
                data['time'] = entry.date
                data['other'] = ''
                self.trade_request.emit(data)

            time.sleep(self.interval)
