# 使用 high level client api
from pypsrp.client import Client
from config import SERVER, USERNAME, PASSWORD
from pathlib import Path


# this takes in the same kwargs as the WSMan object
with Client(
    server=SERVER,
    username=USERNAME,
    password=PASSWORD,
    ssl=False,
) as client:
    # execute a cmd command
    stdout, stderr, rc = client.execute_cmd("dir", encoding="gbk")
    print(f"stdout: {stdout} \nstderr: {stderr} \nrc: {rc}")

    stdout, stderr, rc = client.execute_cmd("powershell.exe gci $pwd", encoding="gbk")
    print(f"stdout: {stdout} \nstderr: {stderr} \nrc: {rc}")
    sanitised_stderr = client.sanitise_clixml(stderr)
    print(f"sanitised stderr: {sanitised_stderr}")

    # execute a PowerShell script - 当前目录下的 test_path.ps1
    script_path = Path(__file__).parent / "test_path.ps1"
    with open(script_path, "r") as f:
        script = f.read()
    output, streams, had_errors = client.execute_ps(script)
    print(f"output: {output} \nstreams: {streams} \nhad_errors: {had_errors}")

    output, streams, had_errors = client.execute_ps(
        "New-Item -Path C:\\temp\\folder -ItemType Directory"
    )
    print(f"output: {output} \nstreams: {streams} \nhad_errors: {had_errors}")

    # copy a file from the local host to the remote host
    client.copy(str(script_path), "C:\\temp\\file.txt")

    # fetch a file from the remote host to the local host
    dst_path = Path(__file__).parent / "file.txt"
    client.fetch("C:\\temp\\file.txt", str(dst_path))
