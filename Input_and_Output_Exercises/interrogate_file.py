def get_status(f):
    if f.closed:
        return "Closed"
    else:
        return "Open"

if __name__ == "__main__":
    file = open(r"sample_data\my_file.txt", "w")
    print("File Name:", file.name)
    print("Open Mode:", file.mode)
    print("Readable:", file.readable())
    print("Writable:", file.writable())
    print("File Status:", get_status(file))
    file.close()
    print("File Status:", get_status(file))
    input("Press Any Key to Continue...")
