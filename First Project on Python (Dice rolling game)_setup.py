from cx_Freeze import setup, Executable

base = None

executables = [Executable("First Project on Python (Dice rolling game).py", base=base)]

packages = ["idna","random","os"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Dice_Rolling_Game",
    options = options,
    version = "1.0",
    description = 'Simple Rolling Dice Game',
    executables = executables
)
