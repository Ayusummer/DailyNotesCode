# 监控指定目录下的所有文件变动，并在控制台输出文件的变动类型和路径。
# 可以根据需要对 $action 变量中的脚本块进行修改，以实现更复杂的操作，比如将变动的文件复制到其他位置、发送通知等

# 监控的目录
$targetDir = "C:\sscms\wwwroot"
# log文件路径为当前目录下的log.txt
$logFile = ".\log.txt"


# 创建监控对象
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $targetDir
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true

# 监听文件变动事件
$action = {
    $path = $Event.SourceEventArgs.FullPath
    $changeType = $Event.SourceEventArgs.ChangeType
    Write-Host "File $path was $changeType"
    # 将变动的文件信息写入log文件
    $log = "File $path was $changeType"
    Add-Content $logFile $log
    
}

Register-ObjectEvent $watcher "Created" -Action $action
Register-ObjectEvent $watcher "Changed" -Action $action
Register-ObjectEvent $watcher "Deleted" -Action $action
Register-ObjectEvent $watcher "Renamed" -Action $action

# 等待事件发生
try {
    while ($true) {
        Start-Sleep 1
    }
}
finally {
    # 清理事件注册
    $watcher.Dispose()
}
