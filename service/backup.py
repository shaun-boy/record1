from subprocess import run


class BackUp:
    def __init__(self):
        source = "record1.db"
        tar = "D:\\backup\\"
        end = tar + "record1.db"
        try:
            with open(source):
                run('echo D | xcopy /s/f/h/y "' + source + '" "' + tar + '"',shell=True)
        except FileNotFoundError:
            run('echo D | xcopy /s/f/h/y "' + end + '" "' + "." + '"',shell=True)
