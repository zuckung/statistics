import os



def local_check():
	# for local testing
	if os.getcwd() == '/storage/emulated/0/Download/mgit/statistics/res/src':
		os.chdir('../../')


def findp(list, p):
	# search for the plugin return the number
	count = ''
	for check in list:
		if check.startswith(p + ' '):
			count = check.split(' ')[1]
			break
	return count


def write_readme():
	logfiles = os.listdir('res/dl_log/')
	logfiles.sort()
	for i in range(0, len(logfiles) - 7): # only the last 7 files
		logfiles.pop(0)
	# get the relevant part of the sourcefiles
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
	rows1 = relevant[0].split('\n')
	rows2 = relevant[1].split('\n')
	rows3 = relevant[2].split('\n')
	rows4 = relevant[3].split('\n')
	rows5 = relevant[4].split('\n')
	rows6 = relevant[5].split('\n')
	rows7 = relevant[6].split('\n')
	# write the readme
	with open('README.md', 'w') as target:
		target.writelines('Plugin download count for https://github.com/zuckung/endless-sky-plugins<br>\n<br>\n')
		# split the 7 variable contents to lists
		first = True
		for row in rows7:
			if row == '':
					continue
			if first == True:
				# write the dates
				target.writelines('<table>\n')
				target.writelines('\t<tr>\n')
				target.writelines('\t\t<td></td>\n')
				target.writelines('\t\t<td>' + rows1[0].replace('.txt', '').replace('2024-', '') + '</td>\n')
				target.writelines('\t\t<td>' + rows2[0].replace('.txt', '').replace('2024-', '') + '</td>\n')
				target.writelines('\t\t<td>' + rows3[0].replace('.txt', '').replace('2024-', '') + '</td>\n')
				target.writelines('\t\t<td>' + rows4[0].replace('.txt', '').replace('2024-', '')  + '</td>\n')
				target.writelines('\t\t<td>' + rows5[0].replace('.txt', '').replace('2024-', '')  + '</td>\n')
				target.writelines('\t\t<td>' + rows6[0].replace('.txt', '').replace('2024-', '')  + '</td>\n')
				target.writelines('\t\t<td>' + rows7[0].replace('.txt', '').replace('2024-', '')  + '</td>\n')
				target.writelines('\t\t<td>today +</td>\n')
				target.writelines('\t</tr>\n')
				first = False
			else:
				# write the numbers
				target.writelines('\t<tr>\n')
				target.writelines('\t\t<td>' + row.split(' ')[0] + '</td>\n')
				target.writelines('\t\t<td>' + findp(rows1, row.split(' ')[0]) + '</td>\n')
				target.writelines('\t\t<td>' + findp(rows2, row.split(' ')[0]) + '</td>\n')
				target.writelines('\t\t<td>' + findp(rows3, row.split(' ')[0]) + '</td>\n')
				target.writelines('\t\t<td>' + findp(rows4, row.split(' ')[0]) + '</td>\n')
				target.writelines('\t\t<td>' + findp(rows5, row.split(' ')[0]) + '</td>\n')
				target.writelines('\t\t<td>' + findp(rows6, row.split(' ')[0]) + '</td>\n')
				target.writelines('\t\t<td>' + findp(rows7, row.split(' ')[0]) + '</td>\n')
				difference = str(int(findp(rows7, row.split(' ')[0])) - int(findp(rows6, row.split(' ')[0])))
				if difference == '0':
					difference = ''
				else:
					difference = '+ ' + difference 
				target.writelines('\t\t<td>' + difference + '</td>\n')
				target.writelines('\t</tr>\n')
		target.writelines('</table>\n')
				
		 
		
local_check()
write_readme()