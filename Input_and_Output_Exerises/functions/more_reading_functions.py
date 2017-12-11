import re
from traceback import print_exc
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
        print_exc()
    finally:
        file.close()
    return content

def define_last_words():
    rx = re.compile("\s+")

    def last_words(path, n=0):
        nonlocal rx
        words = None
        ret = ""
        file = open(path, "rb")
        try:
            words = rx.split(file.read().decode("utf-8"))
            if words[0] == "":
                del words[0]
            if words[len(words) - 1] == "":
                del words[len(words) - 1]
            if len(words) < n:
                n = len(words)
            for i in range(len(words) - n, len(words)):
                ret += words[i] + " "
        except:
            print_exc()
        finally:
            file.close()
        return ret

    return last_words

last_words = define_last_words()
define_last_words = None
