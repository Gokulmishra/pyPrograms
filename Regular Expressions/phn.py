#9959555952 saketh kollepu
import re
ph=re.compile(r'\d\d\-\d\d\d\d\d\d\d\d')
i=0
while i<2:
	n=ph.search("sedfgvbhj 98-76543210 ggdlutc 96-76543210")
	print(n.group())
	i+=1
