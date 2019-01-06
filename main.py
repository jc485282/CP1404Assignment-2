from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from Songslist import SongList

class SongsList(App):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.song_list = SongList()
        self.top_label = Label(text="", id="count_label")
        self.status_label = Label(text="")
        self.sort_label = Label(text="Sort by:")
        self.spinner = Spinner(text='Artist', values=('Artist', 'Title', 'Year', 'Required'))
        self.append_Songs_label = Label(text="Add Song...")
        self.title_label = Label(text="Title:")
        self.title_text_input = TextInput(write_tab=False, multiline=False)
        self.artist_label = Label(text="Artist:")
        self.artist_text_input = TextInput(write_tab=False, multiline=False)
        self.year_label = Label(text="Year:")
        self.year_text_input = TextInput(write_tab=False, multiline=False)

        self.append_Songs_button = Button(text='Add Song')
        self.clear_button = Button(text='Clear')

    def append_Songs_handler(self, *args):
        if str(self.title_text_input.text).strip() == '' or str(self.artist_text_input.text).strip() == '' or str(
                self.year_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be completed"
        else:
            try:

                if int(self.year_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Year must be >= 0"
                else:
                    self.song_list.append_Songs(self.title_text_input.text, self.artist_text_input.text,
                                            int(self.year_text_input.text))
                    self.song_list.sorting(self.spinner.text)
                    self.fields_text_clearer()
                    self.root.ids.rightLayout.clear_widgets()
                    self.build_right_widgets()

            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"


        if str(self.title_text_input.text).strip() == '' or str(self.artist_text_input.text).strip() == '' or str(
                self.year_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be filled"
        else:
            try:

                if int(self.year_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Year must be >= 0"
                else:
                    self.song_list.append_Songs(self.title_text_input.text, self.artist_text_input.text,
                                            int(self.year_text_input.text))
                    self.song_list.sorting(self.spinner.text)
                    self.fields_text_clearer()
                    self.root.ids.rightLayout.clear_widgets()
                    self.build_right_widgets()
            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"

    def build(self):

        self.title = "Songs to learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.song_list.load_songs()
        self.song_list.sorting('Artist')
        self.build_left_widgets()
        self.build_right_widgets()
        return self.root


    def build_left_widgets(self):
        self.root.ids.leftLayout.add_widget(self.sort_label)
        self.root.ids.leftLayout.add_widget(self.spinner)
        self.root.ids.leftLayout.add_widget(self.append_Songs_label)
        self.root.ids.leftLayout.add_widget(self.title_label)
        self.root.ids.leftLayout.add_widget(self.title_text_input)
        self.root.ids.leftLayout.add_widget(self.artist_label)
        self.root.ids.leftLayout.add_widget(self.artist_text_input)
        self.root.ids.leftLayout.add_widget(self.year_label)
        self.root.ids.leftLayout.add_widget(self.year_text_input)
        self.root.ids.leftLayout.add_widget(self.append_Songs_button)
        self.root.ids.leftLayout.add_widget(self.clear_button)
        self.root.ids.topLayout.add_widget(self.top_label)
        self.spinner.bind(text=self.sorting_songs)
        self.append_Songs_button.bind(on_release=self.append_Songs_handler)
        self.clear_button.bind(on_release=self.fields_text_clearer)

    def learn_Songs(self, button):
        if self.song_list.song_get(button.id).status == 'n':
            self.song_list.song_get(button.id).status = 'y'
            self.root.ids.bottomLayout.text = "You need to learn " + str(self.song_list.song_get(button.id).title)

        else:
            self.song_list.song_get(button.id).status = 'n'
            self.root.ids.bottomLayout.text = "You have learnt " + str(self.song_list.song_get(button.id).title)

        self.sorting_songs()
        self.root.ids.rightLayout.clear_widgets()
        self.build_right_widgets()





















