def line(length, string):
    if string != "":
        print(string[0] * length)
    else:
        print("*" * length)
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")