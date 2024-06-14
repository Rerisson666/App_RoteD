from kivy.lang import Builder # type: ignore
from kivy.uix.boxlayout import BoxLayout # type: ignore
from kivy.uix.label import Label # type: ignore
from kivy.uix.textinput import TextInput # type: ignore
from kivy.uix.button import Button # type: ignore
from kivy.uix.screenmanager import ScreenManager, Screen # type: ignore
from kivy.app import App # type: ignore

# Importe o código Flask e algoritmo
from app import app as flask_app
from threading import Thread
import webbrowser

class FlaskThread(Thread):
    def run(self):
        flask_app.run()

class MainScreen(Screen):
    pass

class AddVertexScreen(Screen):
    def add_vertex(self):
        vertice = self.ids.vertice_input.text
        self.ids.vertice_input.text = ""
        # Aqui você pode chamar a função Flask para adicionar vértice

class AddEdgeScreen(Screen):
    def add_edge(self):
        origem = self.ids.origem_input.text
        destino = self.ids.destino_input.text
        peso = self.ids.peso_input.text
        self.ids.origem_input.text = ""
        self.ids.destino_input.text = ""
        self.ids.peso_input.text = ""
        # Aqui você pode chamar a função Flask para adicionar aresta

class CalculateRouteScreen(Screen):
    def calculate_route(self):
        inicio = self.ids.inicio_input.text
        fim = self.ids.fim_input.text
        self.ids.inicio_input.text = ""
        self.ids.fim_input.text = ""
        # Aqui você pode chamar a função Flask para calcular a rota

class WindowManager(ScreenManager):
    pass

kv = '''
WindowManager:
    MainScreen:
    AddVertexScreen:
    AddEdgeScreen:
    CalculateRouteScreen:

<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "Algoritmo de Roteamento - Dijkstra"
        Button:
            text: "Adicionar Vértice"
            on_release:
                app.root.current = "add_vertex"
        Button:
            text: "Adicionar Aresta"
            on_release:
                app.root.current = "add_edge"
        Button:
            text: "Calcular Rota"
            on_release:
                app.root.current = "calculate_route"

<AddVertexScreen>:
    name: "add_vertex"
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "Adicionar Vértice"
        TextInput:
            id: vertice_input
            hint_text: "Vértice"
        Button:
            text: "Adicionar"
            on_release:
                root.add_vertex()
                app.root.current = "main"
        Button:
            text: "Voltar"
            on_release:
                app.root.current = "main"

<AddEdgeScreen>:
    name: "add_edge"
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "Adicionar Aresta"
        TextInput:
            id: origem_input
            hint_text: "Origem"
        TextInput:
            id: destino_input
            hint_text: "Destino"
        TextInput:
            id: peso_input
            hint_text: "Peso"
        Button:
            text: "Adicionar"
            on_release:
                root.add_edge()
                app.root.current = "main"
        Button:
            text: "Voltar"
            on_release:
                app.root.current = "main"

<CalculateRouteScreen>:
    name: "calculate_route"
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "Calcular Rota"
        TextInput:
            id: inicio_input
            hint_text: "Início"
        TextInput:
            id: fim_input
            hint_text: "Fim"
        Button:
            text: "Calcular"
            on_release:
                root.calculate_route()
                app.root.current = "main"
        Button:
            text: "Voltar"
            on_release:
                app.root.current = "main"
'''

class MainApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    # Inicie o Flask em uma thread separada
    flask_thread = FlaskThread()
    flask_thread.start()
    # Abra a interface Flask no navegador
    webbrowser.open('http://127.0.0.1:5000/')
    MainApp().run()
