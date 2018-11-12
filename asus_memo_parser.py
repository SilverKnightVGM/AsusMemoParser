# coding: latin-1
"""

This script tries to parse .memo files from the ASUS Quick Memo Android app, since there is no backup and export function in the app.

Usage:

python asus_memo_parser.py [path]

"""

import os, sys
import glob

if(len(sys.argv) == 2):
	os.chdir(sys.argv[1])

count = 0
print("\nPROCESSING:", os.getcwd(), "\n")

os.makedirs(os.path.dirname(os.getcwd() + "\converted\\"), exist_ok=True)

for memo in glob.glob("*.memo"):
	with open(memo, "rb") as fp:
		# 0x31 is where the message length is specified
		fileContent = fp.seek(int(0x31))
		# Read the 1 byte length
		msgSize = fp.read(1).hex()
		# Convert to int, specifying my original input in in base 16
		msgSize = int(msgSize,16)
		# Read the message itself
		msg = fp.read(msgSize)
		msg = msg.decode("utf-8")
		
		# print(msg.decode("utf-8"))
		# print("-----------------")
		with open("converted\\" + memo + ".txt", "w", encoding="utf8") as of:
			of.write(msg)
	count += 1

print("{} file(s) processed".format(count))
input("\nPress any key to end...")