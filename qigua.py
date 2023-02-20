
# Get the random number from ANU Quantum Random Numbers Server, API document https://qrng.anu.edu.au/API/api-demo.php
import requests
import os
r = requests.get('http://qrng.anu.edu.au/API/jsonI.php?type=hex16&size=3&length=1')

# convert the hex result to array and get first 3 character
a = list(r.json()['data'][0]) [:3]

# convert hex to binary for each parts
b = [list(bin(int(x,16)))[2:] for x in a]

# sum the binary
c = [sum([int(y) for y in x])  for x in b]

# convert to the dictionary key
d = [str(x) for x in c]

# get html content 
url =  'https://github.com/seth2000/linqijing/blob/main/' + "".join(d) + '.md'
#r = requests.get(url)


import webbrowser

print(url)
# Open url in a new window of the default browser, if possible
webbrowser.open_new(url)


# # deal with non-english encoding as the charset in html such as <meta http-equiv="Content-Type" content="text/html; charset=gbk">
# r.encoding = 'gbk'

# # parse html by bs4
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(r.text, 'html.parser')

# # extract the content by tag and class
# items = soup.find_all('li', {'class':['b1 green','b2 green','b2']}) 

# # save the file to txt file, encoding is very important
# BASE_FOLDER = os.getcwd()
# DEFAULT_FOUT = os.path.join(BASE_FOLDER, 'gua.txt')

# f = open(DEFAULT_FOUT, 'w',  encoding="utf-8")

# f.write(soup.title.get_text() + '\n')
# # print(soup.title.get_text()) # leave it as test 
# #for x in items:
# #	if 'b1' in x['class']:
# #		f.write(x.get_text())
# #	else:
# #		f.write(x.get_text() + '\n')
# #	# print(x.get_text())  # leave it as test 

# # do forgot close the file
# f.close()

