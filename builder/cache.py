from webui import initialize
import modules.interrogate

# Ensure initialize is a callable function before calling it
if callable(initialize):
    initialize()
else:
    raise TypeError(f"'initialize' is not callable. It is a {type(initialize)}")

interrogator = modules.interrogate.InterrogateModels("interrogate")
interrogator.load()
interrogator.categories()
