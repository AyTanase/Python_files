from traceback import print_exc
path = r"sample_data\hello.c.py"
file = open(path, "wb")
try:
    file.write(b'#include <stdio.h> /*\r\n')
    file.write(b'from traceback import print_exc\r\n')
    file.write(b'file = open("my_file.txt", "wb")\r\n')
    file.write(b'try:\r\n')
    file.write(b'    file.write(b"Hello, World!\\r\\n")\r\n')
    file.write(b'except:\r\n')
    file.write(b'    print_exc()\r\n')
    file.write(b'finally:\r\n')
    file.write(b'    file.close()\r\n')
    file.write(b'print("Hello, World!")\r\n')
    file.write(b'""" */\r\n')
    file.write(b'int main(void) {\r\n')
    file.write(b'    FILE* fp = fopen("my_file.txt", "w");\r\n')
    file.write(b'    if (fp == NULL) {\r\n')
    file.write(b'        return 1;\r\n')
    file.write(b'    }\r\n')
    file.write(b'    fprintf(fp, "Hello, World!\\r\\n");\r\n')
    file.write(b'    fclose(fp);\r\n')
    file.write(b'    printf("Hello, World!\\n");\r\n')
    file.write(b'    return 0;\r\n')
    file.write(b'}\r\n');
    file.write(b'/* """\r\n')
    file.write(b'# */\r\n')
except:
    print_exc()
finally:
    file.close()
file = open(path, "rb")
try:
    print(file.read().decode("utf-8"))
except:
    print_exc()
finally:
    file.close()
input("Press Any Key to Continue...")
