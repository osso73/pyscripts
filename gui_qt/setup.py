from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {
    'packages': [], 
    'excludes': []
    }

base = 'WIN32GUI'

executables = [
    Executable('main.py', base=base, target_name='pyscripts'),
]

setup(name='pyscripts',
      version = '1.0',
      description = 'Some scripts to enhance your Windows experience',
      options = {'build_exe': build_options},
      executables = executables)
