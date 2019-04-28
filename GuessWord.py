from random import randint


def printWord(wordNow):
    for i in range(len(wordNow)):
        print(wordNow[i],end="")


if __name__ == "__main__":
    words = ["static","abstract","extends","implements","throw","orange"]
    randomIndex = randint(0,len(words) - 1)

    selectWord = words[randomIndex]
    print("选择的单词：" + selectWord)

    # 定义一个列表保存用户当前猜中的单词
    wordNow = []

    # 将每个字符串初始值设置成-
    for i in range(len(selectWord)):
        wordNow.append('-')

    printWord(wordNow)

    userTimes = 5
    while True:
        strGuess = input("输入字符")
        nIndex = -1
        if strGuess in selectWord:
            nIndex = selectWord.index(strGuess)

        if nIndex < 0:
            userTimes -= 1
            if userTimes == 0:
                break

            print("还剩" + str(userTimes) + "次机会")
            printWord(wordNow)

        else:
            for i in range(len(selectWord)):
                tempC = selectWord[i]
                if tempC == strGuess[0]:
                    wordNow[i] = tempC

            printWord(wordNow)

        strWordNow = "".join(wordNow)

        if "-" not in strWordNow:
            break

    if userTimes > 0:
        print("恭喜，猜对了")
    else :
        print("你输了，正确答案是：" + selectWord)
