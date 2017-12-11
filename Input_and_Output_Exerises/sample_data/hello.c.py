#include <stdio.h> /*
from traceback import print_exc
file = open("my_file.txt", "wb")
try:
    file.write(b"Hello, World!\r\n")
except:
    print_exc()
finally:
    file.close()
print("Hello, World!")
""" */
int main(void) {
    FILE* fp = fopen("my_file.txt", "w");
    if (fp == NULL) {
        return 1;
    }
    fprintf(fp, "Hello, World!\r\n");
    fclose(fp);
    printf("Hello, World!\n");
    return 0;
}
/* """
# */
