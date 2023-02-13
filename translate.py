import re
from pygtrans import Translate

client = Translate()
regex = re.compile(r'(?<=">).*(?=</string>)')
result_file =  open("result.xml",mode="w")
orgin_file = open("strings.xml")

line_text = orgin_file.readlines()
for line in line_text:
    match = regex.search(line)
    if match:
        print(line)
        result_line = line[:match.start()] + client.translate(match.group(0)).translatedText + line[match.end():]
        result_file.write(result_line)
    else:

        result_file.write(line)
orgin_file.close()
result_file.close()