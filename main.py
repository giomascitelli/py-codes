import subprocess

def get_open_files():
    result = subprocess.run(['handle.exe'], capture_output=True, text=True)
    output = result.stdout

    vscode_files = [line for line in output.splitlines() if 'Code.exe' in line]

    for file in vscode_files:
        print(file)

get_open_files()