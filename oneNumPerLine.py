inputFile = input("Enter Your Input File. With Extension (.csv, .txt): ")
#outputFile = input("Enter Out Put File Name : ")

#string = open('todaywoman.csv', 'r')
string = open(inputFile, 'r')
output = open("todayman.txt", 'a')

#stripList = lists.rstrip()
numbers = string.readlines()

try:
    for i in numbers: #range(len(numbers) - 1): #five line
        number = i.replace(',', '')
        numbers = number.split()
        for number in numbers:
            output.write(number)
            output.write("\n")

except IndexError:
    print("Please Your output file is outputFile.txt")
