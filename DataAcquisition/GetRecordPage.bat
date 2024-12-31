:: Usage: get.bat [uid] [client_id(cookie)] [target_user_id] [record_page] [log_file] 
:: Example: get.bat 123456 123456789abcdefg 114514 1 record.log
:: Example: get.bat 123456 123456789abcdefg 123456 1
:: Example: get.bat 123456 123456789abcdefg kkksc03 1 

:: Warning: The log file will contain the client_id(cookie) and do not share it with others.
:: You have to login with your Luogu cookies to get the other user's record page.
:: You can add -v manually to see more information about the process.
if exist %%4% (
    curl -o %~dp0RecordFiles/record%4.json "https://www.luogu.com.cn/record/list?user=%3&_contentOnly=1&page=%4" -H "Cookie :_uid=%1; __client_id=%2; " >> %%4% 
) else (
    curl -o %~dp0RecordFiles/record%4.json "https://www.luogu.com.cn/record/list?user=%3&_contentOnly=1&page=%4" -H "Cookie :_uid=%1; __client_id=%2; " 
)