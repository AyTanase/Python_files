from reading_functions import read_whole
import functions.more_reading_functions as mrf

print(read_whole(r"..\..\ILAS_python\sample_data\dot.txt"))
print(end="\n\n\n")

path = r"..\..\ILAS_python\sample_data\sea.txt"
n = input("set n:")

print("\n\nFirst", n, "lines:", end="\n\n")
print(mrf.first_lines(path, int(n)), end="\n\n\n")

print("Last", n, "words:", end="\n\n")
print(mrf.last_words(path, int(n)), end="\n\n\n")

input("Press Any Key to Continue...")
