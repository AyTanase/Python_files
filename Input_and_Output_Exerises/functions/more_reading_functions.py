import re
import traceback

def first_lines(path, n=0):
    content = None
    file = open(path, "rb")
    try:
        content = re.match(
            r"(?:.*\r?\n){0," + str(n) + "}",
            file.read().decode("utf-8")
        )[0]
    except:
        traceback.print_exc()
    finally:
        file.close()
    return content

def last_words(path, n=0):
    content = None
    file = open(path, "rb")
    try:
        content = re.search(
            r"(?:\s+[^\s]+){0," + str(n) + "}\s*$",
            file.read().decode("utf-8")
        )[0]
    except:
        traceback.print_exc()
    finally:
        file.close()
    return content
