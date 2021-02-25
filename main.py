from tkinter import *
from body import *

wndw = Tk()
num = -1
dict = {}
bdwords = ""
input0 = input1 = ""


def const():
    global num, dict, input0, input1, words, label
    num = -1
    dict = {}
    input1 = ""
    words.delete("1.0", END)
    label["text"] = "Сколько букв в слове?"


f = open("words.txt", "r")

wndw.title("HangmanHack")
dicti = f.readlines()[0].split()


def buttinmain():
    global label, number, count, const
    const()
    count["show"] = ""
    string["show"] = ""
    badwords["show"] = ""
    label.grid()
    number.grid()
    button_next.grid()
    button_inmain.grid()
    words.grid_remove()
    button_add.grid_remove()
    count.grid_remove()
    string.grid_remove()
    button_give.grid_remove()
    badwords.grid_remove()
    button_inmain.grid_remove()


def buttnext():
    global num, label
    label["text"] = "На каких позициях отгаданные буквы?\nКакие буквы отгаданы?"
    num = number.get()
    number.grid_remove()
    button_next.grid_remove()
    count.grid()
    string.grid()
    badwords.grid()
    button_give.grid()
    button_inmain.grid()


def buttadd(a):
    global bdwords, dict, count, string, input0, input1, label
    input0 = count.get()
    input1 = string.get()
    bdwords = badwords.get()
    dict[input0] = input1
    label["text"] = "Как я понял:\n{0} = {1}".format(input0, input1)


def buttgive():
    global dict, num, words, dicti, bdwords, str
    words.delete("1.0", END)
    alphabet = {"а": 0, "б": 0, "в": 0, "г": 0, "д": 0, "е": 0, "ж": 0, "з": 0, "и": 0, "й": 0, "к": 0, "л": 0, "м": 0,
                "н": 0, "о": 0, "п": 0, "р": 0, "с": 0, "т": 0, "у": 0, "ф": 0, "х": 0, "ц": 0, "ч": 0, "ш": 0, "щ": 0,
                "ъ": 0, "ы": 0, "ь": 0, "э": 0, "ю": 0, "я": 0, "-": 0}
    arr = finder(num, dicti, dict, bdwords=bdwords)
    arr = last_check(arr, bdwords)
    output = "Не знаю таких слов\n =Р\n"
    for i in arr:
        if output == "Не знаю таких слов\n =Р\n":
            output = "Попробуй что-нибудь из этого\n ;)\n"
        output += i + "\n"
    for j in arr:
        for k in j:
            alphabet[k] += 1


    max = [0, 0, 0, 0, 0]
    maxchr = ["", "", "", "", ""]
    output += "Максимально часые буквы здесь: " + maxchr[0] + ", " + maxchr[1] + ", " + maxchr[2] + ", " + maxchr[3] + ", " + maxchr[4] + '\n'
    for i in alphabet:
        output += i + " : " + str(alphabet[i]) + "\n"
        if int(max[0]) < int(alphabet[i]):
            max[0] = alphabet[i]
            maxchr[0] = i
        elif int(max[1]) < int(alphabet[i]):
            max[1] = alphabet[i]
            maxchr[1] = i
        elif int(max[2]) < int(alphabet[i]):
            max[2] = alphabet[i]
            maxchr[2] = i
        elif int(max[3]) < int(alphabet[i]):
            max[3] = alphabet[i]
            maxchr[3] = i
        elif int(max[4]) < int(alphabet[i]):
            max[4] = alphabet[i]
            maxchr[4] = i

    words.insert("1.0", output)
    words.grid()


words = Text(wndw, height=20, width=50, font="Arial 14")
label = Label(wndw, text="Сколько букв в слове?")
number = Scale(wndw, orient="horizontal", length=500, from_=0, to=26, resolution=1)
button_next = Button(wndw, text="Дальше", command=buttnext)
button_inmain = Button(wndw, text="Вернуться в начало", command=buttinmain)
button_add = Button(wndw, text="Добавить", command=buttadd)
count = Entry(wndw, width=2, bd=10)
string = Entry(wndw, width=num, bd=10)
badwords = Entry(wndw, bd=5)
button_give = Button(wndw, text="Показать слова", command=buttgive)

label.grid()
number.grid()
button_next.grid()

wndw.bind("<Return>", buttadd, "+")

wndw.mainloop()
