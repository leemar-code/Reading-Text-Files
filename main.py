def read_file_content(filename):
    with open(
        "C:/Users/user/Downloads/Reading-Text-Files/Reading-Text-Files/story.txt"
    ) as f:
        line = f.readline()
        while line:
            line = f.readline()
            print(line)
read_file_content("")