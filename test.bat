@echo off

set doc_key="1Xlh7NYTHZQHAWHvGDH_JVpMqM_jWJoaYSaTfldIFmRE"
set heet="Tasks"
set creds_id="1QQwdL5TIqBTNQ5KLzGiRATimatvQWOk5"

curl -X POST -H "Content-Type: application/json" -d "{\"doc_key\":\"%doc_key%\", \"sheet\":\"%sheet%\", \"creds_id\":\"%creds_id%\"}" "https://gsheet-api-wcbz.onrender.com/" > response.json

type response.json

pause

