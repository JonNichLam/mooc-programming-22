# Write your solution here
#Please write a function named chessboard, which prints out a chessboard made out of ones and zeroes. The function takes an integer argument, which specifies the length of the side of the board. See the examples below for details:

def chessboard(num):



    for x in range(num):
        chessRow = ""
        if x %2 == 0:
            for y in range(num):
                if y % 2 == 0:
                    chessRow += "1"
                else:
                    chessRow += "0"
        else:
            for y in range(num):
                if y % 2 == 0:
                    chessRow += "0"
                else:
                    chessRow += "1"

        print(chessRow)



# Testing the function
if __name__ == "__main__":
    chessboard(3)
