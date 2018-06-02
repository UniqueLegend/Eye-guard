# 种子文件验证

种子文件是文件发布者根据要发布的文件生成的一个后缀为.torrent的文件，简称“种子”。种子文件本质上是一个文本文件，包含Tracker服务器信息和文件信息两部分。Tracker信息主要是BT下载中需要用到的tracker服务器的地址和针对tracker服务器的设置，文件信息根据目标文件的计算生成。整个文件需要进行Bencode编码。

种子文件结构为：tracker信息：announce ,[announce-list],comment[comment.encoding],creation date,encoding]；info信息{files,files,length,path,path.encoding,name,name.encoding,piece length,pieces,publisher}

Bencode是BitTorrent用在传输数据结构的编码方式。该种编码支持四种类型的数据：string，dictionary，int，list。string类型编码格式为[length]:[string]；int类型编码格式为i[int]e;list类型编码格式为l[list]e,list内元素可以是四种类型的全部；dictionary类型编码额是d[key-pair]e。

本地客户端与tracker服务器使用get方法建立连接。必须传入infohash（二十字节）,peert_id,ip,port

对种子文件的验证分为两方面，一是种子文件本身的是否完整，能否用bencode正确编解码；二是能否与tracker服务器建立连接，如果能够建立连接，则检查构造的get请求的反馈消息，若是有fail reason字段，则判定割爱tracker失效检查下一个tracker。如果所有tracker无要下载文件，判定种子无效。