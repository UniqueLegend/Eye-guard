# coding: utf-8

from DHTSpider import DHTSpider
import logging
import asyncio
import aiomysql


class Crawler(DHTSpider):
    
    async def handle_get_peers(self, infohash, addr):
        logging.info(
            "Receive get peers message from DHT {}. Infohash: {}.".format(
                addr, infohash
            )
        )
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(
                        "INSERT INTO table_test VALUES('%s', '%s', '%s', '%s')" %
                        (addr[0], str(addr[1]), infohash, 'get_peers')
                    )
                    # await cur.execute("delete from table_test where ip='1'")
                    await conn.commit()
                    print('* Succeed! Inserted infohash "' + infohash + '"from ' + str(addr) +
                          ' into database. Type: get_peers \n')
                except aiomysql.MySQLError:
                    logging.info(
                        "Failed to save infohash: {} into database. Maybe it's already existed. \n".format(infohash)
                    )
                # finally:
                #     pool.close()
                #     await pool.wait_closed()
    """

    async def handle_announce_peer(self, infohash, addr, peer_addr):
        logging.info(
            "Receive announce peer message from DHT {}. Infohash: {}. Peer address:{}".format(
                addr, infohash, peer_addr
            )
        )
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(
                        "INSERT INTO table_test VALUES('%s', '%s', '%s', '%s')" %
                        (addr[0], str(addr[1]), infohash, 'announce_peer')
                    )
                    await conn.commit()
                    print('* Succeed! Inserted infohash "' + infohash + '"from ' + str(addr) +
                          ' into database. Type: announce_peer \n')
                except aiomysql.MySQLError:
                    logging.info(
                        "Failed to save infohash: {} into database. Maybe it's already existed. \n".format(infohash)
                    )
                # finally:
                #     pool.close()
                #     await pool.wait_closed()
"""

"""
    # 待改善
    async def handle_database(self, pool, infohash, addr):
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute(
                        "INSERT INTO table_test VALUES('%s', '%s', '%s', '%s')" %
                        (addr[0], str(addr[1]), infohash, 'announce_peer')
                    )
                    await conn.commit()
                    print('Succeed! Inserted infohash "' + infohash + '"from ' + str(addr) +
                          ' into database. Type: announce_peer')
                except aiomysql.MySQLError:
                    logging.info(
                        "Failed to save infohash: {} into database. Maybe it's already existed.".format(infohash)
                    )
"""
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    pool = loop.run_until_complete(aiomysql.create_pool(host='127.0.0.1', port=3306, user='root',
                                                        password='xuexi520', db='database_test', loop=loop))
    crawler = Crawler()
    crawler.run(port=0)
