from logging import basicConfig, INFO, CRITICAL, getLogger, StreamHandler
from datetime import datetime
from os import listdir, path, remove, getenv
from sys import stdout

BASE_PATH = path.dirname(path.abspath(__file__))

def delete_old_log():
    while len(listdir(path.join(BASE_PATH, "logs"))) > 4:
        all_logs = listdir(path.join(BASE_PATH, 'logs'))
        all_logs_strings = [x.split("_log")[0] for x in all_logs]
        all_datetimes = []
        for l in all_logs_strings:
            l = l.replace('_', '-').split('-')
            all_datetimes.append(datetime(int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5])))
        min_date = all_datetimes.index(min(all_datetimes))
        remove(path.join(BASE_PATH, 'logs', all_logs[min_date]))



def generate_logger():
    if not getenv('TESTING', False):
        if len(listdir(path.join(BASE_PATH, "logs"))) > 4:
            delete_old_log()
        file_name = datetime.now().isoformat().replace("T", "_").replace(":", "-").split(".")[0] + "_log.log"
        basicConfig(filename=path.join(BASE_PATH, "logs", file_name), level=INFO)
        ch = StreamHandler(stdout)
        logger = getLogger(__name__)
        logger.addHandler(ch)
        return logger
    else:
        basicConfig(level=CRITICAL)
        ch = StreamHandler(stdout)
        logger = getLogger(__name__)
        logger.addHandler(ch)
        return logger

LOGGER = generate_logger()

def get_logger():
    return LOGGER