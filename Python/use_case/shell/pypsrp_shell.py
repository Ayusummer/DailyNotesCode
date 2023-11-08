from pypsrp.client import Client

# this takes in the same kwargs as the WSMan object
with Client("server", username="user", password="password") as client:
    # execute a cmd command
    stdout, stderr, rc = client.execute_cmd("dir")

    stdout, stderr, rc = client.execute_cmd("powershell.exe gci $pwd")
    sanitised_stderr = client.sanitise_clixml(stderr)

    # execute a PowerShell script
    output, streams, had_errors = client.execute_ps(
        """$path = "%s"
if (Test-Path -Path $path) {
    Remove-Item -Path $path -Force -Recurse
}
New-Item -Path $path -ItemType Directory"""
        % path
    )
    output, streams, had_errors = client.execute_ps(
        "New-Item -Path C:\\temp\\folder -ItemType Directory"
    )

    # copy a file from the local host to the remote host
    client.copy("~/file.txt", "C:\\temp\\file.txt")

    # fetch a file from the remote host to the local host
    client.fetch("C:\\temp\\file.txt", "~/file.txt")
