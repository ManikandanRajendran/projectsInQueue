from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetExample(GridLayout):
    count = 1
    my_text = StringProperty("1")
    count_enabled = BooleanProperty(False)
    slider_val = StringProperty("0")
    textInput_text = StringProperty("foo")

    def click_me(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

    def toggle_button_press(self, widget):
        # print(widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def switch_active(self, widget):
        print(widget.active)

    def slider_value(self, widget):
        self.slider_val = str(int(widget.value))

    def text_input_validate(self,widget):
        self.textInput_text = widget.text


class BoxLayoutWidget(BoxLayout):
    pass


"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""


class StackLayoutWidget(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        size = dp(100)
        for i in range(0, 100):
            b = Button(text=str(i + 1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)


class GridLayoutWidget(GridLayout):
    pass


class AnchorLayoutWidget(AnchorLayout):
    pass


class mainWidget(Widget):
    pass


class testApp(App):
    pass


if __name__ == '__main__':
    testApp().run()
