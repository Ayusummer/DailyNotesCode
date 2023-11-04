# 使用 python 管理各 shell 进程, 执行命令, 并返回结果
import subprocess
import time
import threading

# 建立 Powershell 进程, 保持连接交互
powershell_process = subprocess.Popen(
    "powershell.exe",
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,
    bufsize=0,
)


try:
    time.sleep(5)
    # 尝试执行 whoami
    powershell_process.stdin.write("whoami\n")
    powershell_process.stdin.flush()
    # 解 stdout 缓存
    std_out = powershell_process.stdout
    cmd_out = powershell_process.stdout.readline()
    print(f"output: {cmd_out}\n==================================")

    powershell_process.stdin.write("dir\n")
    powershell_process.stdin.flush()
    print(f"output: {powershell_process.stdout}\n==================================")

    stdout, stderr = powershell_process.communicate()
    print(
        f"Stdout:===========================\n {stdout} \n\n Stderr:===========================\n {stderr}"
    )


except subprocess.TimeoutExpired:
    powershell_process.kill()
    stdout, stderr = powershell_process.communicate()
    print(f"Stdout: {stdout}, Stderr: {stderr}")
except Exception as e:
    print(f"Error: {e}")


# 尝试执行 whoami 命令, 返回 exit_code, stdout, stderr
# powershell_process.stdin.write("whoami\n")
# powershell_process.stdin.flush()
# r1 = powershell_process.stdout.readline()
# r2 = powershell_process.stdout.readline()
# r3 = powershell_process.stdout.readline()
# # 清空缓存
# r4 = powershell_process.stdout.readline()
# r5 = powershell_process.stdout.readline()
# r6 = powershell_process.stdout.readline()
# powershell_process.stdin.flush()


# result = r1 + r2 + r3 + r4 + r5 + r6
# print(result)
