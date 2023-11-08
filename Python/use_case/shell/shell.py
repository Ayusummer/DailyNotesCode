# 调用 Powershell 执行 command 并返回结果
from typing import Tuple
import subprocess


def run_command(
    command: str, shell_type: str, timeout: int = 60
) -> Tuple[int, str, str]:
    """
    Run a command and return the exit code, stdout, and stderr.
    """
    if shell_type == "powershell":
        command = f'powershell.exe -NonInteractive -Command "{command}"'
    elif shell_type == "cmd":
        command = f'cmd.exe /c "{command}"'
    else:
        raise ValueError(f"Unsupported shell type: {shell_type}")

    # Run the command
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        universal_newlines=True,
    )

    # Wait for the command to complete
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        return (-1, stdout, stderr)

    # Return the exit code, stdout, and stderr
    return (process.returncode, stdout, stderr)


def main():
    # Run the command
    exit_code, stdout, stderr = run_command(command="whoami", shell_type="powershell")

    # Print the results
    print(f"Exit code: {exit_code}")
    print(f"Stdout: {stdout}")
    print(f"Stderr: {stderr}")


if __name__ == "__main__":
    main()
