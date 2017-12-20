import re
from traceback import print_exc

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
    rx = re.compile(r"(\S+(?:(?<=-)[\r\n]\s*\S+)*)\s*|\s+")

    def last_words(path, n=0):
        nonlocal rx
        words = None
        ret = ""
        file = open(path, "rb")
        try:
            words = rx.findall(file.read().decode("utf-8"))
            """
            # unnecessary
            if words[0] == "":
                del words[0]
            """
            i = len(words) - 1
            while n > 0 and i >= 0:
                ret = words[i] + " " + ret
                n -= 1
                i -= 1
        except:
            print_exc()
        finally:
            file.close()
        return ret

    return last_words

last_words = define_last_words()
define_last_words = None
