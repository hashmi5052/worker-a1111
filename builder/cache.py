from webui import launch  # Assuming initialize is in launch
import modules.interrogate

# Ensure initialize is a callable function before calling it
if callable(launch.initialize):
    launch.initialize()
else:
    raise TypeError(f"'initialize' is not callable. It is a {type(launch.initialize)}")

interrogator = modules.interrogate.InterrogateModels("interrogate")
interrogator.load()
interrogator.categories()
