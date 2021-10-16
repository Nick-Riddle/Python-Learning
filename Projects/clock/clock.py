from constants import *
from PIL import Image, ImageTk
import time
import tkinter as tk


class Clock:

    def __init__(self):

        self.clock = tk.Tk()
        self.canvas = tk.Canvas(
            self.clock,
            height=HEIGHT,
            width=WIDTH,
            highlightthickness=0)
        self.background = tk.PhotoImage(file='bg.png')
        self.clock_properties = []

    def create_clock(self):

        self.clock.resizable(False, False)
        self.clock.geometry('540x210')
        self.clock.title('Clock')
        self.canvas.pack()

        self._change_window_position()

        self._set_background()

        self._create_labels()

        self._nospace_label_anim()

        self._update_clock()

        self._change_time()

        self.clock.mainloop()

    def _change_window_position(self):

        x = (self.clock.winfo_screenwidth() -
             self.clock.winfo_reqwidth()) / 2.7
        y = (self.clock.winfo_screenheight() -
             self.clock.winfo_reqheight()) / 2.3
        self.clock.wm_geometry("+%d+%d" % (x, y))

    def _set_background(self):

        self._resize_img()
        self.canvas.create_image(0, 0, anchor='nw', image=self.background)
        self.clock.iconbitmap('icon.ico')

    def _create_labels(self):

        hours = self.canvas.create_text(
            100,
            105,
            text=f'{time.strftime("%H")}',
            fill=FONT_COLOR,
            font=(
                FONT,
                FONT_SIZE))
        self.nospace_label1 = self.canvas.create_text(
            185, 96, text=f':', fill=LABEL_COLOR, font=(FONT, FONT_SIZE))
        minutes = self.canvas.create_text(
            270,
            105,
            text=f'{time.strftime("%M")}',
            fill=FONT_COLOR,
            font=(
                FONT,
                FONT_SIZE))
        self.nospace_label2 = self.canvas.create_text(
            355, 96, text=f':', fill=LABEL_COLOR, font=(FONT, FONT_SIZE))
        seconds = self.canvas.create_text(
            440,
            105,
            text=f'{time.strftime("%S")}',
            fill=FONT_COLOR,
            font=(
                FONT,
                FONT_SIZE))

        self.clock_properties.extend([hours, minutes, seconds])

    def _nospace_label_anim(self):

        self.canvas.itemconfigure(self.nospace_label1, text=f'')
        self.canvas.itemconfigure(self.nospace_label2, text=f'')

        self.clock.update()
        time.sleep(0.1)

        self.canvas.itemconfigure(self.nospace_label1, text=f':')
        self.canvas.itemconfigure(self.nospace_label2, text=f':')

        self.clock.after(900, self._nospace_label_anim)

    def _update_clock(self):

        h = f'{time.strftime("%H")}'
        m = f'{time.strftime("%M")}'
        s = f'{time.strftime("%S")}'

        self.canvas.itemconfigure(self.clock_properties[0], text=h)
        self.canvas.itemconfigure(self.clock_properties[1], text=m)
        self.canvas.itemconfigure(self.clock_properties[2], text=s)

        self.clock.after(1000, self._update_clock)

    def _change_time(self):

        change = 4

        for i in range(1, change):
            self.canvas.itemconfigure(
                self.clock_properties[0], font=(
                    FONT, FONT_SIZE + i))
            self.canvas.itemconfigure(
                self.clock_properties[1], font=(
                    FONT, FONT_SIZE + i))
            self.canvas.itemconfigure(
                self.clock_properties[2], font=(
                    FONT, FONT_SIZE + i))
            self.clock.update()
            time.sleep(0.02)

        time.sleep(0.15)

        for i in range(1, change):
            self.canvas.itemconfigure(
                self.clock_properties[0], font=(
                    FONT, FONT_SIZE - i))
            self.canvas.itemconfigure(
                self.clock_properties[1], font=(
                    FONT, FONT_SIZE - i))
            self.canvas.itemconfigure(
                self.clock_properties[2], font=(
                    FONT, FONT_SIZE - i))
            self.clock.update()
            time.sleep(0.02)
        self.clock.after(150, self._change_time)

    def _resize_img(self):

        img = Image.open('bg.png')
        img = img.resize((WIDTH, HEIGHT))
        self.background = ImageTk.PhotoImage(image=img)