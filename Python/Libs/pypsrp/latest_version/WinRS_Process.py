from pypsrp.shell import Process, SignalCode, WinRS
from pypsrp.wsman import WSMan
from config import SERVER, USERNAME, PASSWORD


# creates a http connection with no encryption and basic auth
wsman = WSMan(
    server=SERVER,
    username=USERNAME,
    password=PASSWORD,
    ssl=False,
)

with wsman, WinRS(wsman) as shell:
    process = Process(shell, "dir")
    process.invoke()
    process.signal(SignalCode.CTRL_C)
    print(
        f"stdout: {process.stdout.decode('gbk')} \n=======\nstderr: {process.stderr.decode('gbk')} \n======\nrc: {process.rc}\n======\n"
    )

    # execute a process with arguments in the background
    process = Process(shell, "powershell", ["gci", "$pwd"])
    process.begin_invoke()  # start the invocation and return immediately
    process.poll_invoke()  # update the output stream
    process.end_invoke()  # finally wait until the process is finished
    process.signal(SignalCode.CTRL_C)
    print(
        f"stdout: {process.stdout.decode('gbk')} \n=======\nstderr: {process.stderr.decode('gbk')} \n======\nrc: {process.rc}\n======\n"
    )
