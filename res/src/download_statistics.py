import requests
import os
from datetime import datetime
import json


# for local testing
if os.getcwd() == '/storage/emulated/0/Download/mgit/statistics/res/src':
	os.chdir('../../')



def set_var():
	global username
	global token
	global repo
	username = ''
	token = ''
	repo = 'zuckung/endless-sky-plugins'

def get_date():
	now = datetime.now()
	date_time = now.strftime('%Y-%m-%d')
	return date_time

def analyze_write():
	rcount = 0
	downloads = 0
	plugins = []
	pcount = []
	if not os.path.isdir('res/dl_log/'):
		os.makedirs('res/dl_log/')
	with open('res/dl_log/' + get_date() + '.txt', 'w') as target:
		target.writelines('# DOWNLOADS FOR EACH RELEASE:\n')
		for i in range(1, 100): # call api for felease downloads, max 100 times if needed
			if username == '' or token == '':
				response = requests.get('https://api.github.com/repos/' + repo + '/releases?page=' + str(i) + '&per_page=100')
			else:
				response = requests.get('https://api.github.com/repos/' + repo + '/releases?page=' + str(i) + '&per_page=100', auth=(username, token))
			data = response.json()	
			if len(data) == 0:
				break
			for obj in data: # each data has max 100 releases
				rcount += 1 # number of releases
				rname = obj['tag_name']
				rdownload = obj['assets'][0]["download_count"] # number of downloads for each release 
				if rname == 'Latest':
					break
				if rname.split('-', 1)[1] in plugins:
					index = plugins.index(rname.split('-', 1)[1])
					icount = pcount[index]
					icount += rdownload
					pcount[index] = icount
				else:
					plugins.append(rname.split('-', 1)[1])
					pcount.append(rdownload)
				target.writelines(rname + ' | downloads: ' + str(rdownload) + '\n')
				downloads += rdownload
		target.writelines('\n\n')
		target.writelines('# NUMBER OF RELEASES: ' + str(rcount) + '\n')
		target.writelines('# TOTAL DOWNLOADS: ' + str(downloads) + '\n\n\n')
		target.writelines('# TOTAL DOWNLOAD NUMBER FOR EACH PLUGIN:\n')
		for each in plugins:
			index = plugins.index(each)
			plugins[index] = each + ' ' + str(pcount[index])
		plugins.sort()
		for each in plugins:
			index = plugins.index(each)
			target.writelines(each + '\n')

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
	
		 
		


set_var()
analyze_write()
#write_readme()
