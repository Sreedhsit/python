a = 0

while a == 0:
    #print("\n \n" * 100)
    print("Please enter a word to check if it is a palindrome: ")
    word = input("?: ")

    wordLength = int(len(word))
    finalWordLength = int(wordLength / 2)
    firstHalf = word[:finalWordLength]
    secondHalf = word[finalWordLength + 1:]
    secondHalf = secondHalf[::-1]
    print(firstHalf)
    print(secondHalf)

    if firstHalf == secondHalf:
        print("This is a palindrom")
    else:
        print("This is not a palindrom")


    print("Press enter to restart")
    input()