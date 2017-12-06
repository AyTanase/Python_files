from reading_functions import read_whole
import functions.more_reading_functions as mrf
print(read_whole(r"..\..\ILAS_python\sample_data\dot.txt"))
print()
path = r"..\..\ILAS_python\sample_data\sea.txt"
n = input("set n:")
print()
print(mrf.first_lines(path, n))
print()
print(mrf.last_words(path, n))
input("\nPress Any Key to Continue...")
