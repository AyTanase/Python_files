import traceback
def read_whole(path):
    content = None
    file = open(path, "rb")
    try:
        content = file.read().decode("utf-8")
    except:
        traceback.print_exc()
    finally:
        file.close()
    return content

if __name__ == "__main__":
    print(read_whole(r"..\..\ILAS_python\sample_data\poem.txt"))
    input("\nPress Any Key to Continue...")
