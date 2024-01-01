import vt
client = vt.Client("c245ad21ee8c65d5f642bae9710a14dba2dbff6451826ceaf2453f2157223a36")
with open("E:\Repo\GithubRepo\Self\DailyNotesCode\Powershell\Trojan\AddMoreCommonCMD\ObfuscatedRAT.ps1", "rb") as f:
    analysis = client.scan_file(f, wait_for_completion=True)

print(analysis.results)