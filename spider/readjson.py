import json
# 讀取json檔案
url ='test.json'
with open(url, 'r') as result_fd:
    result_file = json.load(result_fd)
    print(result_file['info'])

