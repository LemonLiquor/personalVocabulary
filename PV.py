from core import PersonalVocabulary,PeelWord
from expand import Browser

def main():
    beginSts = \
"""--------------------
1.录入已经掌握的单词
2.载入并输出生词
q.退出
--------------------"""
    endBnr = \
r"""          _____           _______                   _____                    _____          
         /\    \         /::\    \                 /\    \                  /\    \         
        /::\____\       /::::\    \               /::\____\                /::\    \        
       /:::/    /      /::::::\    \             /:::/    /               /::::\    \       
      /:::/    /      /::::::::\    \           /:::/    /               /::::::\    \      
     /:::/    /      /:::/~~\:::\    \         /:::/    /               /:::/\:::\    \     
    /:::/    /      /:::/    \:::\    \       /:::/____/               /:::/__\:::\    \    
   /:::/    /      /:::/    / \:::\    \      |::|    |               /::::\   \:::\    \   
  /:::/    /      /:::/____/   \:::\____\     |::|    |     _____    /::::::\   \:::\    \  
 /:::/    /      |:::|    |     |:::|    |    |::|    |    /\    \  /:::/\:::\   \:::\    \ 
/:::/____/       |:::|____|     |:::|    |    |::|    |   /::\____\/:::/__\:::\   \:::\____\
\:::\    \        \:::\    \   /:::/    /     |::|    |  /:::/    /\:::\   \:::\   \::/    /
 \:::\    \        \:::\    \ /:::/    /      |::|    | /:::/    /  \:::\   \:::\   \/____/ 
  \:::\    \        \:::\    /:::/    /       |::|____|/:::/    /    \:::\   \:::\    \     
   \:::\    \        \:::\__/:::/    /        |:::::::::::/    /      \:::\   \:::\____\    
    \:::\    \        \::::::::/    /         \::::::::::/____/        \:::\   \::/    /    
     \:::\    \        \::::::/    /           ~~~~~~~~~~               \:::\   \/____/     
      \:::\    \        \::::/    /                                      \:::\    \         
       \:::\____\        \::/____/                                        \:::\____\        
        \::/    /         ~~                                               \::/    /        
         \/____/                                                            \/____/         
                                                                                            """

    flag = True
    while flag:
        print("欢迎使用个人词汇匹配程序，请选择你要使用的功能：")
        print(beginSts)
        menuChosen = input()
        if menuChosen == "1":
            recordWord()
        elif menuChosen == "2":
            printNewWords()
        elif menuChosen == "q":
            flag = False
            print(endBnr)
        else:
            print("***未知的输入命令，请重新输入***")
        
#记录以及熟识的单词
def recordWord():
    pv = PersonalVocabulary()
    print("请输入需要录入的单词（输入回车以结束）：")
    word = "oneword"
    while word != "" :
        word = input("> ")
        pv.add(word)
    print("录入结束")

#原生的，输出所有生词
#TODO:统计一下数量
def printNewWords():
    pw = PeelWord()
    newWords = pw.peel()
    if len(newWords)!=0:
        print("本文所含生词如下：")
        for word in newWords:
            print("· "+word)
    else:
        print("本文不含任何生词")


    _ = input("按任意键退出...\n")

#删除又忘记掉的单词
def delete4getWord():
    pv = PersonalVocabulary()
    print("请输入需要删除的单词（输入回车以结束）：")
    word = "oneword"
    while word != "" :
        word = input("> ")
        pv.delete(word)
    print("删除完毕")


def test():
    pass

if __name__ == "__main__":
    main()
    #test()