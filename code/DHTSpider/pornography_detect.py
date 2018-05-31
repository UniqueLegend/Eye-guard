# coding: utf-8

import cherry
import pymysql
import pymysql.cursors

config = {
	'host':'127.0.0.1',
	'port':3306,
	'user':'root',
	'password':'xuexi520',
	'db':'database_test',
	'charset':'utf8mb4',
	'cursorclass':pymysql.cursors.DictCursor
}
connection = pymysql.connect(**config)

if 1:#try:
	with connection.cursor() as cursor:
		cursor.execute("select info_hash, file_num, pornography from torrents")
		results = cursor.fetchall()
		for item in results:
			if item['pornography'] is None:
				info_hash = item['info_hash']
				sql = "select name from files where info_hash=%s"
				cursor.execute(sql, info_hash)
				res = cursor.fetchall()
				print(res)
				name_list = [i['name'] for i in res]
				name_string = '|'.join('name_list')
				
				# sex | gamble | politics | normal
				percentage = cherry.classify('测试文本test text').percentage
				print(percentage)
				pornography = [i[1] for i in percentage if 'sex.dat' in i][0]
				print(pornography)
				#sql = "update torrents set pornography=%s where info_hash=%s"
				#cursor.execute(sql, (pornography, info_hash))
				#connection.commit()
#except Exception as e:
#	print(repr(e))
#finally:
#	connection.close()

