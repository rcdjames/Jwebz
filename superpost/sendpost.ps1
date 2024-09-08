$body = @{
 "name"="james"
 "email"="james@gmail.com"
 "age"="29"
 "some_number"="648312358"
} | ConvertTo-Json

$header = @{
 "Accept"="application/json"
 "Content-Type"="application/json"
} 

Invoke-RestMethod -Uri "http://127.0.0.1:8080/post_json" -Method 'Post' -Body $body -Headers $header | ConvertTo-HTML
