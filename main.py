import math
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import Radiobutton, Checkbutton
from PIL import Image, ImageTk

window = Tk()
window.title("Lab 3")
window.geometry('600x700')
tab_control = ttk.Notebook(window)

'''
Первая вкладка для деменострации: 
1. Лейблов или меток (Label); 
2. Получение ввода (Entry);
3. Кнопки (Button).
'''
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Вкладка 1')
tab_control.pack(expand=1, fill='both')

lb_first_name = Label(tab1, text='1. Введите Ваше имя:')
lb_first_name.pack()

first_name = Entry(tab1, width=20)
first_name.pack()

lb_last_name = Label(tab1, text='2. Введите Вашу фамилию:')
lb_last_name.pack()

last_name = Entry(tab1, width=20)
last_name.pack()

lb_otchestvo = Label(tab1, text='3. Введите Ваше отчество:')
lb_otchestvo.pack()

otchestvo = Entry(tab1, width=20)
# otchestvo.grid(column=0, row=5)
otchestvo.pack()

lb_result = Label(tab1, width=20)
lb_result.pack()


def get_full_name():
    result = f'Ваше ФИО: {first_name.get()} {last_name.get()} {otchestvo.get()}'
    lb_result.configure(text=result)


but1 = Button(tab1, text='Сохранить!', command=get_full_name)
but1.pack()

'''
Вторая вкладка для деменострации: 
1.   Многострочного поле ввода (Опишите ваш опыт в сфере ИТ)
2.   Радиокнопки (Ваш вакультет)
3.   Чекбокс (Ваши знания языков)
4.   Полоса прокрутки
'''
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Вкладка 2')
tab_control.pack(expand=1, fill='both')

lb_information1 = Label(tab2, text='2.1 Опишите Ваш опыт в сфере ИТ:', width=40)
lb_information1.pack()
text_user_exp = Text(tab2, width=40, height=10)
text_user_exp.pack()

text_area = scrolledtext.ScrolledText(tab2, width=40, height=10)


def get_full_exp():
    text_area.delete('1.0', END)
    text = "I. Мой опыт в сфере ИТ:\n" + text_user_exp.get(1.0, END) + \
           f'II. Мой факультет: {selected.get()}\n'

    languages = 'III. Мои знания языков:\n'
    if chk_state_ukr.get():
        languages += 'Украинский язык\n'
    if chk_state_eng.get():
        languages += 'Английский язык\n'
    text += languages

    text_area.insert(INSERT, text)
    # print(chk_state_cpp.get())


but2 = Button(tab2, text='Сохранить!', command=get_full_exp)

lb_information2 = Label(tab2, text='2.2 Выберите Ваш факультет:', width=40)
lb_information2.pack()

selected = StringVar()
rad1 = Radiobutton(tab2, text='КИУ', value='КИУ', variable=selected)
rad2 = Radiobutton(tab2, text='КН', value='КН', variable=selected)
rad3 = Radiobutton(tab2, text='АКТ', value='АКТ', variable=selected)
rad4 = Radiobutton(tab2, text='ИТМ', value='ИТМ', variable=selected)
rad1.pack()
rad2.pack()
rad3.pack()
rad4.pack()

lb_information3 = Label(tab2, text='2.3 Выберите языки, которые Вы знаете:', width=40)
lb_information3.pack()

chk_state_ukr = BooleanVar()
chk_state_eng = BooleanVar()
chk = Checkbutton(tab2, text='Українська мова', var=chk_state_ukr)
chk.pack()
chk2 = Checkbutton(tab2, text='English', var=chk_state_eng)
chk2.pack()

but2.pack()
text_area.pack()


'''
Третья вкладка для деменострации: 
1.   Frame для организации других виджетов в группы
2.   Шкала для выбора значения из заданного диапазона
3.   Окно верхнего уровня (для показа информации "О лабораторной работе"
'''
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Вкладка 3')
tab_control.pack(expand=1, fill='both')

lb_information1 = Label(tab3, text='3.1 Введите n:', width=40)
lb_information1.pack()

scale = Scale(tab3, orient=HORIZONTAL, length=500, from_=0, to=100, tickinterval=10, resolution=1)
scale.pack()

image1 = Image.open("images/formula.png")
image1 = image1.resize((500, 60))

test = ImageTk.PhotoImage(image1)

label1 = Label(tab3, image=test)
label1.image = test
label1.pack()


def get_result_formula():
    n = scale.get()
    x = n
    y = n + 2
    rez = (1 + x) ** y + (y * x) / math.factorial(1) + (y * (y - 1) * x * x) / math.factorial(2) + (
                (1 + 4 * (x / y)) ** 0.5) / ((20 * y) ** 0.5)
    label_result_formula.configure(text=f'Результат = {round(rez, 2)}')


f_top = Frame(tab3)

but_formula = Button(f_top, text='Посчитать', command=get_result_formula)
but_formula.pack(side=LEFT)
label_result_formula = Label(tab3)
label_result_formula.pack()


def get_about():
    win = Toplevel(f_top)
    win.title("О лабораторной работе")
    win.minsize(width=400, height=200)
    text = 'Розробка графічного інтерфейсу в Python (Tkinter)\nМета роботи - опонувати методи створення графічного\n' \
           'інтерфейсу для програмного забезпечення на Python. '
    lb = Label(win, text=text)
    lb.pack()


btn_about = Button(f_top, text='О лабораторной работе', command=get_about)
btn_about.pack(side=LEFT)

f_top.pack()

window.mainloop()
