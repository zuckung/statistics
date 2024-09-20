import os

def write_readme():
	logfiles = os.listdir('res/dl_log/')
	logfiles.sort()
	for i in range(0, len(logfiles) - 7):
		logfiles.pop(0)
	print(logfiles)
	relevant = ['', '', '', '', '', '', '', ]
	for i in range(0,7):
		relevant[i] += logfiles[i] + '\n'
		with open('res/dl_log/' + logfiles[i], 'r') as sourcefile:
			all = sourcefile.readlines()
			started = False
			for line in all:
				if line.startswith('# TOTAL DOWNLOAD NUMBER FOR EACH PLUGIN'):
					started = True
					continue
				if started == True:
					relevant[i] += line
	with open('README.md', 'w') as target:
		target.writelines('<table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr>')
		for each in relevant:
			target.writelines('<td>')
			target.writelines(each)
			target.writelines('</td>')
		target.writelines('</tr></table>')
	
		 
		

write_readme()