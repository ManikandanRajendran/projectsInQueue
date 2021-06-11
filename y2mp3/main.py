import youtube_dl
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior


Builder.load_file('main.kv')

# url = 'https://www.youtube.com/watch?v=EEs4mY7YpTU'


class FirstPage(Screen):
    def download_mp3(self, url):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        except:
            self.show_alert_dialog("unable to download the file. Please check the URL")

    def update_message(self, text):
        pass


# download_mp3(url)


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()