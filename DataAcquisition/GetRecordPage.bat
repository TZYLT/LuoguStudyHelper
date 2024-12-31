:: Usage: get.bat [uid] [client_id(cookie)] [record_page] [log_file] 
:: Warning: The log file will contain the client_id(cookie) and do not share it with others.
:: You can add -v manually to see more information about the process.
if exist %%4% (
    curl -o %~dp0RecordFiles/record%3.json "https://www.luogu.com.cn/record/list?user=%1&_contentOnly=1&page=%3" -H "Cookie :_uid=%1; __client_id=%2; " >> %%4% 
) else (
    curl -o %~dp0RecordFiles/record%3.json "https://www.luogu.com.cn/record/list?user=%1&_contentOnly=1&page=%3" -H "Cookie :_uid=%1; __client_id=%2; " 
)