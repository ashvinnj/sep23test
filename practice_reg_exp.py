# coding: utf-8
"""
    practice_reg_exp.py this script is my way of learning regular expression discussed in class and
    slides available from class url: https://davidbpython.com/advanced_python/handouts.html
"""
'''
import re
weblog = [
   '66.108.19.165 - - [09/Jun/2003:19:56:33 -0400] "GET /&#126;jjk265/cd.jpg HTTP/1.1" 200 175449',
   '66.108.19.165 - - [09/Jun/2003:19:56:44 -0400] "GET /&#126;dbb212/mysong.mp3 HTTP/1.1" 200 175449',
   '66.108.19.165 - - [09/Jun/2003:19:56:45 -0400] "GET /&#126;jjk265/cd2.jpg HTTP/1.1" 200 175449'
]
print('++++++++++++++++++++++++++++++++++++++++ find user jjk265')
for line in weblog:
    if re.search(r'&#126;jjk265', line):
        print(line)
print('------------------------------------- find ip address and user name-----------')
for entry in weblog:
    match = re.search(r'(\d+\.\d+\.\d+\.\d+) - - \[.*\] "GET /&#126;(\w+)', entry)
    print(f'{entry[match.start():match.end()][:100]}')
    print (type(match))
    if match:
        ip_address = match.group(1)
        user_name = match.group(2)
        print(f"IP Address: {ip_address}, User Name: {user_name}")

print('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ \b boundry usage example -+-+-+')
sen_without_can = 'No we can\'t!'
print(re.search(r'\bcan\b', sen_without_can))  # True

print("++++++++++++++++++++++++++++++++++++++  find bytes downloaded from web log+++++++++++++++")
log_lines = [
    '"GET /&#126;jjk265/cd.jpg HTTP/1.1" 200 175449',
    '"GET /&#126;rba203/about.html HTTP/1.1" 200 -',
    '"GET /&#126;dd595/frame.htm HTTP/1.1" 400 1144'
]

for line in log_lines:
    matchobj = re.search(r'(\d+)\s*$', line)
    if matchobj:
        bytes_transferred = int(matchobj.group(1))
        print(bytes_transferred)
    else:
        print("No match found")

print ('--- runreport test statement')

this_name = 'abc23 great day'
this_name = this_name.replace(" ", "_")
print(this_name)
this_name = re.sub(r'[^a-zA-Z_]', '', this_name)
print(this_name)
'''
#------------------------------------------
# -- open access_log.txt file and play with grabbing different values
import re

# sample line to parse
# 172.26.93.208 - - [28/Jun/2012:21:00:45 -0400] "GET /~cmk380/pythondata/image3a.txt HTTP/1.1" 200 4487"
# 76.93.2.80 - - [29/Jun/2012:20:11:58 -0400] "GET /~kmo326/postcast.xml HTTP/1.1" 200 678
nos_records = 1
user_line_pattern = r'^\b(\d+\.\d+\.\d+\.\d+)\b - - \[.*\] "GET /~(\w{2,3}\d{2,4})'
bytes_pattern = r'GET /~\w+/.* HTTP/1\.1" 200 (\d+)'
bytes_count = 0
total_bytes = 0
bytes_count = {}
no = 0
with open(r'C:\Users\ashvi\Documents\NYU_Python\python_data_apy\session_04_working_files\access_log.txt', 'r') as file:
    line = file.readline()
    # http_resposne = re.search(bytes_pattern, line).group(1)

    no += 1
    # print(f'{no}------------------------{http_resposne}')
    while line and nos_records < 4000:

        matchobj = re.search(user_line_pattern, line)
        http_good_resposne = re.search(bytes_pattern, line)
        print(f'++++++++ {no} - {http_good_resposne}')
        if matchobj and http_good_resposne:
            nyu_id = matchobj.group(2)
            bytes = int(http_good_resposne.group(1))
            print(f'{nos_records}.  ----------------{nyu_id} - {bytes}')
            nos_records += 1
            total_bytes += bytes
            if nyu_id not in bytes_count:
                bytes_count[nyu_id] = 0
            bytes_count[nyu_id] = bytes_count[nyu_id] + bytes
        line = file.readline()
        no += 1
    print(f'total bytes = {total_bytes:,.0f}')
    for key in sorted(bytes_count, key=bytes_count.get, reverse=True):
        print(f'{key[:12].ljust(12)}: {bytes_count[key]:,.0f}')

