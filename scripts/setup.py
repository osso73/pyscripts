from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {
    'packages': ['dbm'], 
    'excludes': ['unittest', 'pydoc'],
    'zip_include_packages': ['encodings'],
    }

base = 'console'

executables = [
    Executable('alarm.py', base=base),
    Executable('backup_to_zip.py', base=base),
    Executable('clp.py', base=base),
    Executable('grep.py', base=base),
    Executable('mcb.py', base=base),
    Executable('openURLs.py', base=base),
    Executable('pdf_pages.py', base=base),
    Executable('alarm.py', base=base),
    Executable('pyfind.py', base=base),
    Executable('pyrename.py', base=base),
    Executable('tree_info.py', base=base),
]

setup(name='pyscripts',
      version = '1.0',
      description = 'Some scripts to enhance your Windows experience',
      options = {'build_exe': build_options},
      executables = executables)
