# coding:utf-8

from get_torrent_info import get_torrent_info
import pymysql.cursors
import pymysql
import libtorrent as lt
import os

os.system('mv /root/xunlei/downloads/TDDOWNLOAD/*.torrent /root/PythonProjects/DHTSpider/torrents/')

def save_torrent_info():
	config = {'host':'127.0.0.1', 'port':3306, 'user':'root', 'password':'xuexi520', 'db':'database_test', 'charset':'utf8mb4', 'cursorclass':pymysql.cursors.DictCursor
	}
	connection = pymysql.connect(**config)

	torrents = [i for i in os.listdir('/root/PythonProjects/DHTSpider/torrents/') if '.torrent' in i]
	for i in torrents:
		e = lt.bdecode(open("/root/PythonProjects/DHTSpider/torrents/%s" % i, 'rb').read())
		info = lt.torrent_info(e)
		torrent_information = get_torrent_info(info)
		info_hash = torrent_information['info_hash']

		name = torrent_information['name']
		print 'Name: ' + name
		comment = torrent_information['comment']
		print 'Comment: ' + comment
		file_num = torrent_information['file_num']
		print 'File_num: ' + str(file_num)
		files = torrent_information['files']
		print 'Files: ', files
		total_size = torrent_information['total_size']
		print 'Total_size: ' + total_size
		creator = torrent_information['creator']
		print 'Creator: '+ creator
		creation_date = torrent_information['creation_date']
		print 'Creaton_date: ' + creation_date
		trackers = '|'.join(torrent_information['trackers'])
		print 'Trackers: ' + trackers

		try:   
			with connection.cursor() as cursor:
				sql = "insert into torrents(info_hash, name, comment, file_num, total_size, creator, creation_date, trackers) values(%s, %s, %s, %s, %s, %s, %s, %s)"
				cursor.execute(sql,(info_hash, name, comment, file_num, total_size, creator, creation_date, trackers))
				connection.commit()
				for f in files:
					name = pymysql.escape_string(f['name'])
					size = f['size']
					path = pymysql.escape_string(f['path'])
					sql = "INSERT INTO files values(%s, %s, %s, %s)"
					cursor.execute(sql, (info_hash, name, size, path))
					connection.commit()
				os.system('mv /root/PythonProjects/DHTSpider/torrents/%s /root/PythonProjects/DHTSpider/torrents/done' % i)
				print 'Successfully saved torrent_information.'
		except Exception, e:
			print repr(e)

	connection.close()

if __name__ == '__main__':
	save_torrent_info()

