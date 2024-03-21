from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['main.py', '--onefile', '--name=graficador_excel']
    run(opts)
