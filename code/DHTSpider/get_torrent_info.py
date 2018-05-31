# coding: utf-8

import time
import os

def bytes2human(n):                                                                                                    
        symbols = ('K','M','G','T','P','E','Z','Y')                                                                    
        prefix = {}                                                                                                    
        for i,s in enumerate(symbols):                                                                                 
                prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
                if n >= prefix[s]:
                        value = float(n) / prefix[s]
                        return '%.1f%s' % (value,s)
        return '%sB' % n   

def get_files_info(info):
        files_info=[]
        for i in range(len(info.files())):
                name = info.files().file_name(i)
                path = info.files().file_path(i)
                size = bytes2human(info.files().file_size(i))
                file_info = {'name':name, 'path':path, 'size':size}
                files_info.append(file_info)
        return files_info

def get_torrent_info(info):

	# 种子生成时间
	creation_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(info.creation_date()))

	# 种子名
	name = info.name()

	# info_hash
	info_hash = str(info.info_hash())

	# 种子文件注释
	comment = info.comment()

	# 制作者
	creator = info.creator()

	# 文件数量
	file_num = info.files().num_files()

	# 总大小
	total_size = bytes2human(info.total_size())

	# 文件详情
	files = get_files_info(info)
	"""
	# 文件列表
	file_list = []
	for i in range(file_num):
		file_name = info.files().file_name(i)
		file_list.append(file_name)
	"""
	# trackers
	trackers = []
	for i in info.trackers():
		tracker = i.url
		trackers.append(tracker)

	# 种子信息汇总
	torrent_info = {'creation_date':creation_date, 'name':name, 'comment':comment, 'creator':creator, 'file_num':file_num, 'total_size':total_size, 'files':files, 'info_hash':info_hash, 'trackers':trackers}
	return torrent_info

