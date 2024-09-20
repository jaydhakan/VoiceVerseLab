import logging
from logging.handlers import QueueListener
import queue
import sys
from datetime import datetime, timezone


from utils.logger.src.constants import COLORS


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        record.auditAt = str(
            datetime.fromtimestamp(record.created, timezone.utc)
        )

        colors = {
            'levelname': COLORS.get(record.levelname, COLORS['RESET']),
            'auditAt': COLORS.get('AUDIT_AT', COLORS['RESET']),
        }
        colored_attrs = {
            attr: f"{colors[attr]}{getattr(record, attr)}{COLORS['RESET']}"
            for attr in colors
        }

        formatted_record = super().format(record)
        for attr, colored_value in colored_attrs.items():
            formatted_record = formatted_record.replace(
                getattr(record, attr), colored_value
            )
        return formatted_record


console_format = ColoredFormatter(
    fmt=' '.join(
        [
            '%(auditAt)s',
            '%(name)s',
            '%(levelname)s',
            '\033[95mmessage:\033[0;0;97m %(message)s'
        ]
    )
)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(console_format)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_queue = queue.Queue()
queue_handler = logging.handlers.QueueHandler(log_queue)
logger.addHandler(queue_handler)

handlers = [console_handler]

listener = QueueListener(
    log_queue, *handlers, respect_handler_level=True
)
listener.start()
