from pypsrp.powershell import PowerShell, RunspacePool


def sync_rps(runspace: PowerShell, script: str):
    """同步执行 Powershell script"""
    runspace.add_script(script)
    print(f"执行脚本：{script}")
    output = runspace.invoke()
    if runspace.had_errors:
        print(f"执行脚本 {script} 时出错")
        if runspace.streams.error.__len__() > 0:
            for error in runspace.streams.error:
                print(f"ERROR: {error.exception}")
    else:
        if output:
            print(f"OUTPUT: {output}")
        # 例如 Write-Host 的输出就会存在 information stream 中:
        if runspace.streams.information.__len__() > 0:
            for info in runspace.streams.information:
                print(f"INFORMATION: {info.message_data}")
