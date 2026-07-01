import re


def clean_log(log: str):
    log = log.lower()
    log = re.sub(r"[^a-zA-Z ]", "", log)
    return log