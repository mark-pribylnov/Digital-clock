from tkinter import ttk
from tkinter import *
from time import strftime
import datetime
import platform

try:
        import winsound #windows
except:
        import os #other

root = Tk()
root.title('Clock')

# Tabs
tabs = ttk.Notebook(root)
tabs.pack()

clock_tab = ttk.Frame(tabs)
alarm_tab = ttk.Frame(tabs)
timer_tab = ttk.Frame(tabs)
stopwatch_tab = ttk.Frame(tabs)

tabs.add(clock_tab, text='Clock')
tabs.add(alarm_tab, text='Alarm')
tabs.add(timer_tab, text='Timer')
tabs.add(stopwatch_tab, text='Stopwatch')


# Clock components
time_label = Label(root, font = ('calibri', 20))
time_label.pack()
date_label = Label(root, font = ('calibri', 15))
date_label.pack()

# Time function
def time_func():
    time_str = datetime.datetime.now().strftime("%H:%M:%S")
    date_str = datetime.datetime.now().strftime("%d.%m.%Y")
    time_label.config(text = time_str)
    date_label.config(text = date_str)
    root.after(1000, time_func)


# Alarm function
def alarm():
        main_time = datetime.datetime.now().strftime("%H:%M %p")
        alarm_time = get_alarm_time_entry.get()
        alarm_time1,alarm_time2 = alarm_time.split(' ')
        alarm_hour, alarm_minutes = alarm_time1.split(':')
        main_time1,main_time2 = main_time.split(' ')
        main_hour1, main_minutes = main_time1.split(':')
        if int(main_hour1) > 12 and int(main_hour1) < 24:
                main_hour = str(int(main_hour1) - 12)
        else:
                main_hour = main_hour1
        if int(alarm_hour) == int(main_hour) and int(alarm_minutes) == int(main_minutes) and main_time2 == alarm_time2:
                for i in range(3):
                        alarm_status_label.config(text='Time Is Up')
                        if platform.system() == 'Windows':
                                winsound.Beep(5000,1000)
                        elif platform.system() == 'Darwin':
                                os.system('say Time is Up')
                        elif platform.system() == 'Linux':
                                os.system('beep -f 5000')
                get_alarm_time_entry.config(state='enabled')
                set_alarm_button.config(state='enabled')
                get_alarm_time_entry.delete(0,END)
                alarm_status_label.config(text = '')
        else:
                alarm_status_label.config(text='Alarm Has Started')
                get_alarm_time_entry.config(state='disabled')
                set_alarm_button.config(state='disabled')
        alarm_status_label.after(1000, alarm)

# Alarm components
get_alarm_time_entry = Entry(alarm_tab, font = 'calibri 15')
get_alarm_time_entry.pack()
alarm_instructions = Label(alarm_tab, font = 'calibri 10', text = 'Enter alarm time. E.g. 15:55')
alarm_instructions.pack()
set_alarm_button = Button(alarm_tab, text = 'Set alarm',command = alarm)
set_alarm_button.pack()
alarm_status_label = Label(alarm_tab, font = 'calibri 10', text = '')
alarm_status_label.pack()


# Exit button
exit_btn = ttk.Button(
    root,
    text = 'Exit',
    command = lambda: root.quit()
        )
exit_btn.pack(fill = 'x')

# Pressing Enter triggers the exit
def exit_func(event):
    root.quit()
root.bind('<Return>', exit_func)

time_func()
mainloop()
