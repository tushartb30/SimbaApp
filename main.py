from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from google import genai  # NEW 2026 SDK

# --- CONFIGURATION ---
# Replace with your 2026 API Key
API_KEY = "AIzaSyBWPrTGAut0Hcp6bngJ2YvMjyafnTMY9fM"
client = genai.Client(api_key=API_KEY)

class SimbaApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 1. Chat History Area
        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.chat_history = Label(
            text="Simba: Hello! Type below to chat.\n", 
            size_hint_y=None, 
            halign='left', 
            valign='top'
        )
        self.chat_history.bind(size=self.chat_history.setter('text_size'))
        self.scroll.add_widget(self.chat_history)
        self.main_layout.add_widget(self.scroll)

        # 2. Input Area
        self.input_area = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=5)
        self.user_input = TextInput(multiline=False, hint_text="Ask Simba...")
        self.send_btn = Button(text="Send", size_hint=(0.3, 1))
        self.send_btn.bind(on_press=self.send_message)
        
        self.input_area.add_widget(self.user_input)
        self.input_area.add_widget(self.send_btn)
        self.main_layout.add_widget(self.input_area)

        return self.main_layout

    def send_message(self, instance):
        user_text = self.user_input.text
        if user_text.strip():
            self.chat_history.text += f"\nYou: {user_text}"
            self.user_input.text = "" # Clear input
            
            try:
                # Using gemini-2.0-flash (Stable for May 2026)
                response = client.models.generate_content(
                    model="gemini-2.0-flash", 
                    contents=user_text
                )
                self.chat_history.text += f"\nSimba: {response.text}\n"
            except Exception as e:
                self.chat_history.text += f"\nError: {str(e)}\n"

if __name__ == "__main__":
    SimbaApp().run()