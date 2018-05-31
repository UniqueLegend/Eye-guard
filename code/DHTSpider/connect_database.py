import asyncio
import aiomysql

magnet_head = 'magnet:?xt=urn:btih:'

async def test_example(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='xuexi520',
                                      db='database_test', loop=loop)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            # await cur.execute("INSERT INTO table_test VALUES('%s', '%s', '%s', '%s')" % ('174.110.220.255', '44787', 'B5EA0A22225644CFB745E4668397D45706C4F18C', 'get_peers'))
            # await cur.execute("create table table_test (ip varchar(20), port varchar(5), infohash char(40) primary key not null, type varchar(20))")
            # await cur.execute("drop table table_test")
            # await cur.execute("DELETE FROM table_test WHERE port='44787'")
            await cur.execute("select infohash from table_test where type='announce_peer'")
            await conn.commit()
            r = cur.fetchall().result()
            for i in r:
                link = magnet_head + i[0]
                print(link)
    pool.close()
    await pool.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))
