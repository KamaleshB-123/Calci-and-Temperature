import time
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder


class MenuScreen(Screen):
    t = time.asctime()


class SimpleCalculator(Screen):
    def clear(self):
        self.ids.input_box.text = "0"

    def button_value(self, num):
        prev_number = self.ids.input_box.text

        if "Wrong Equation" in prev_number:
            prev_number = ""

        if prev_number == "0":
            self.ids.input_box.text = ""
            self.ids.input_box.text = f"{num}"

        else:
            self.ids.input_box.text = f"{prev_number}{num}"

    def operator(self, op):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f"{prev_number}{op}"

    def rem(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    def equal_to(self):
        prev_number = self.ids.input_box.text
        try:
            result = eval(prev_number)
            self.ids.input_box.text = str(result)

        except ZeroDivisionError:
            self.ids.input_box.text = "Wrong Equation"

    def posneg(self):
        prev_number = self.ids.input_box.text

        if "-" in prev_number:
            self.ids.input_box.text = f"{prev_number.replace('-','')}"

        else:
            self.ids.input_box.text = f"-{prev_number}"


class Temperature(Screen):
    pass


class CelsiustoKelvin(Screen):
    ans = StringProperty(" ")
    error = StringProperty(" ")

    def clear(self):
        self.ids.input_box.text = "0"

    def back(self):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = prev_number[:-1]

    def results(self):
        if not self.ids.input_box.text:
            self.error = "Error: ENTER THE VALUE"

        else:
            self.ans = str(int(self.ids.input_box.text) + 273.15)


class Kelvintocelsius(Screen):
    ans = StringProperty(" ")
    error = StringProperty("")

    def clear(self):
        self.ids.input_box.text = "0"

    def back(self):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = prev_number[:-1]

    def results(self):
        if not self.ids.input_box.text:
            self.error = "Error: ENTER THE VALUE"
        else:
            self.ans = str(int(self.ids.input_box.text) - 273.15)


class Fahrenheittocelsius(Screen):
    ans = StringProperty(" ")
    error = StringProperty("")

    def clear(self):
        self.ids.input_box.text = "0"

    def back(self):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = prev_number[:-1]

    def results(self):
        if not self.ids.input_box.text:
            self.error = "Error: ENTER THE VALUE"
        else:
            self.ans = str((int(self.ids.input_box.text) - 32) * 5 / 9)


class CelsiustoFahrenheit(Screen):
    ans = StringProperty(" ")
    error = StringProperty("")

    def clear(self):
        self.ids.input_box.text = "0"

    def back(self):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = prev_number[:-1]

    def results(self):
        if not self.ids.input_box.text:
            self.error = "Error: ENTER THE VALUE"
        else:
            self.ans = str(int(self.ids.input_box.text) * 9 / 5 + 32)


class FahrenheittoKelvin(Screen):
    ans = StringProperty(" ")
    error = StringProperty("")

    def clear(self):
        self.ids.input_box.text = "0"

    def back(self):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = prev_number[:-1]

    def results(self):
        if not self.ids.input_box.text:
            self.error = "Error: ENTER THE VALUE"
        else:
            self.ans = str((int(self.ids.input_box.text) - 32) * (5 / 9) + 273.15)


class KelvintoFahrenheit(Screen):
    ans = StringProperty(" ")
    error = StringProperty(" ")

    def clear(self):
        self.ids.input_box.text = "0"

    def back(self):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = prev_number[:-1]

    def results(self):
        if not self.ids.input_box.text:
            self.error = "Error: ENTER THE VALUE"
        else:
            self.ans = str((int(self.ids.input_box.text) - 273.15) * (9 / 5) + 32)


class MainScreen(ScreenManager):
    pass


kv = Builder.load_file("Calci.kv")


class CalciTemperature(App):
    def build(self):
        return kv


CalciTemperature().run()
