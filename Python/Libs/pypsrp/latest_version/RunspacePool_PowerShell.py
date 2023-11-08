from pypsrp.powershell import PowerShell, RunspacePool
from pypsrp.wsman import WSMan
from config import SERVER, USERNAME, PASSWORD


wsman = WSMan(
    server=SERVER,
    username=USERNAME,
    password=PASSWORD,
    ssl=False,
)

with wsman, RunspacePool(wsman) as pool:
    # execute 'Get-Process | Select-Object Name'
    ps = PowerShell(pool)
    ps.add_cmdlet("Get-Process").add_cmdlet("Select-Object").add_argument("Name")
    output = ps.invoke()
    print(f"Output: {output}")

    # execute 'Get-Process | Select-Object -Property Name'
    ps = PowerShell(pool)
    ps.add_cmdlet("Get-Process").add_cmdlet("Select-Object")
    ps.add_parameter("Property", "Name")
    ps.begin_invoke()  # execute process in the background
    ps.poll_invoke()  # update the output streams
    ps.end_invoke()  # wait until the process is finished
    print(f"Output: {ps.output}")

    # execute 'Get-Process | Select-Object -Property Name; Get-Service audiosrv'
    ps = PowerShell(pool)
    ps.add_cmdlet("Get-Process").add_cmdlet("Select-Object").add_parameter(
        "Property", "Name"
    )
    ps.add_statement()
    ps.add_cmdlet("Get-Service").add_argument("audiosrc")
    ps.invoke()
    print(f"Output: {ps.output}")

    # execute a PowerShell script with input being sent
    ps = PowerShell(pool)
    script = """begin {
    $DebugPreference = "Continue"
    Write-Debug -Message "begin"
} process {
    Write-Output -InputObject $input
} end {
    Write-Debug -Message "end"
}
"""
    ps.add_script(script)
    ps.invoke(["string", 1])
    print(ps.output)
    print(ps.streams.debug)
