from taipy.gui import Gui

index = "<h1>Happy learning</h1>"

app = Gui(page=index)

if __name__ == '__main__':
    app.run(use_loaders=True)