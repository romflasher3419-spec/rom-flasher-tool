# Weekly update reminder for Rom Flasher.
#
# Registers (or removes) a Windows scheduled task that pops a reminder every
# Monday morning. Run this once from PowerShell:
#
#     powershell -ExecutionPolicy Bypass -File _weekly_reminder.ps1 install
#     powershell -ExecutionPolicy Bypass -File _weekly_reminder.ps1 status
#     powershell -ExecutionPolicy Bypass -File _weekly_reminder.ps1 remove
#
# It writes a small file to .romflasher\weekly_reminder.txt and shows a Windows
# notification. Nothing is sent anywhere.

param(
    [Parameter(Position = 0)]
    [ValidateSet('install', 'remove', 'status', 'test')]
    [string]$Action = 'status'
)

$ErrorActionPreference = 'Stop'
$TaskName = 'RomFlasher Weekly Update Reminder'
$StateDir = Join-Path $env:USERPROFILE '.romflasher'
$StateFile = Join-Path $StateDir 'weekly_reminder.txt'
$AppDir = 'C:\Users\vrohi\Documents\ROM_Flasher_Tool'
$ReleaseScript = Join-Path $AppDir '_weekly_release.py'
$Python = 'C:\Python315\python.exe'

function Write-Reminder {
    if (-not (Test-Path $StateDir)) { New-Item -ItemType Directory -Path $StateDir -Force | Out-Null }

    $today = Get-Date -Format 'yyyy-MM-dd HH:mm'

    # What version are we on right now?
    $gradle = Join-Path $AppDir 'app\build.gradle.kts'
    $code = '?'; $name = '?'
    if (Test-Path $gradle) {
        $g = Get-Content $gradle -Raw
        if ($g -match 'versionCode\s*=\s*(\d+)') { $code = $Matches[1] }
        if ($g -match 'versionName\s*=\s*"([^"]+)"') { $name = $Matches[1] }
    }

    # What is the newest release on GitHub?
    $latest = 'unknown'
    try {
        $r = gh release list --repo romflasher3419-spec/rom-flasher-tool --limit 1 2>$null
        if ($r) { $latest = ($r -split "`t")[2] }
    } catch { }

    $text = @"
Rom Flasher - weekly update reminder
====================================
Time            : $today
Current version : versionCode $code / $name
Newest release  : $latest

It is update day. Ten minutes of work:

  1. Pick one small real change (a fix, a tweak, a new device or ROM preset).
  2. Run:  python _weekly_release.py --note "what you changed"
  3. Build the APKs.
  4. Run:  gh release create v<version> --title "ROM Flasher Tool v<version>" --notes "..."
  5. Nothing else - the app on users' phones offers the update by itself the
     next time it is open and idle.

The release notes you type in step 4 are what the in-app dialog shows.
"@

    Set-Content -Path $StateFile -Value $text -Encoding UTF8
    Write-Output $text

    try {
        Add-Type -AssemblyName System.Windows.Forms
        $balloon = New-Object System.Windows.Forms.NotifyIcon
        $balloon.Icon = [System.Drawing.SystemIcons]::Information
        $balloon.BalloonTipTitle = 'Rom Flasher: update day'
        $balloon.BalloonTipText = "Version $name is live. Time for this week's release."
        $balloon.Visible = $true
        $balloon.ShowBalloonTip(15000)
        Start-Sleep -Seconds 6
        $balloon.Dispose()
    } catch {
        # No notification support - the file and the console output are enough.
    }
}

switch ($Action) {
    'test' { Write-Reminder }

    'install' {
        $self = $MyInvocation.MyCommand.Path
        $cmd = "powershell -NoProfile -ExecutionPolicy Bypass -File `"$self`" test"
        $act = New-ScheduledTaskAction -Execute 'powershell.exe' `
            -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$self`" test"
        $trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Monday -At 10am
        $settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
        Register-ScheduledTask -TaskName $TaskName -Action $act -Trigger $trigger `
            -Settings $settings -Description 'Reminds you to ship the weekly Rom Flasher update' -Force | Out-Null
        Write-Output "installed: $TaskName (every Monday 10:00)"
        Write-Output "state file: $StateFile"
        Write-Output ""
        Write-Output "Check it any time with:  schtasks /query /tn `"$TaskName`""
    }

    'remove' {
        try {
            Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
            Write-Output "removed: $TaskName"
        } catch {
            Write-Output "nothing to remove ($TaskName was not registered)"
        }
    }

    'status' {
        try {
            $t = Get-ScheduledTask -TaskName $TaskName -ErrorAction Stop
            Write-Output "registered : yes"
            Write-Output "state      : $($t.State)"
            $info = Get-ScheduledTaskInfo -TaskName $TaskName
            Write-Output "next run   : $($info.NextRunTime)"
            Write-Output "last run   : $($info.LastRunTime)"
        } catch {
            Write-Output "registered : no  (run this script with 'install' to add it)"
        }
        Write-Output ""
        if (Test-Path $StateFile) {
            Write-Output "last reminder:"
            Get-Content $StateFile | ForEach-Object { "  $_" }
        } else {
            Write-Output "no reminder written yet"
        }
    }
}
