import requests
import aiomysql
import asyncio
import time
from bs4 import BeautifulSoup

url = 'http://www.torrent.org.cn/home/convert/magnet2torrent.html?hash='
loop = asyncio.get_event_loop()


async def test_example(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='admin', db='database_test',
                                  loop=loop)

    async with conn.cursor() as cur:
        await cur.execute("SELECT infohash FROM table_test")
        r = await cur.fetchall()
        for i in r:
            check_info_url = url + i[0]
            res = requests.get(check_info_url)
            soup = BeautifulSoup(res.text, 'html.parser')
            if soup.title.text[0:2] == "失败":
                print('infohash "' + i[0] + '” failed!')
            elif soup.title.text[0:2] == "成功":
                print('infohash "' + i[0] + '” succeed!')
            else:
                print("Connection error!")
            time.sleep(5)

    conn.close()

loop.run_until_complete(test_example(loop))


