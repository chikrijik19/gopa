# виджет = window + gadget
# типы виджетов: контейры и контет
import tkinter


    
def window_change_color(event) -> None:
    window['bg'] = 'green'

window = tkinter.Tk() # экземпляр окна
window.geometry('1000x600') # изменение размера окна
window.title('ГЕЙ КОМПРОМАТ')
window['padx'] = 30
window['pady'] = 30
window.bind('<Key>', window_change_color)

label_1 = tkinter.Label(window, text='База овец и Ивана') # создвние энкземпляра метки
label_2 = tkinter.Label(window, text='База Свиньи Кирилла') # создвние энкземпляра метки
def on_click(*event) -> None:
    label_1['bg'] = 'blue'
    label_2['bg'] = 'white'
button = tkinter.Button(window, text='Нажми если натурал', command=on_click)


label_1.config(
    bg= 'black',
    fg= 'white'
)
label_2.config(
    bg= 'yellow',
    fg= 'black'
)


label_1.bind('<Button-1>', on_click)

label_1.pack(expand = True, fill= 'both')
label_2.pack(expand = True, fill= 'both')
button.pack()

window.mainloop() # запускаем обновление окна
