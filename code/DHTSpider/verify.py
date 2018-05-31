import bcoding,urllib.request,hashlib
import threading,re
from time import  sleep


def isFileVaslid(f):
    '''检验文件格式和是否能正确解码,传入文件名'''
    try:
        fi = open(f,"rb")
        torrent=bcoding.bdecode(fi)#文件能否解码
        a,b=torrent['info'],torrent['announce'] #是否具有info和announce字段
        return 1
    except Exception:
        return 0

m = isFileVaslid("833A8D93CC94FE1E699779C3C403B062763CE4BE.torrent")


def getTrackers(fi):
    "'获取tracker服务器地址列表'"
    f = open(fi, "rb")
    torrent = bcoding.bdecode(f)
    filehash = hashlib.sha1(f.read()).hexdigest()
    trackers = []
    trackers.append(torrent['announce'])
    try:
        li = torrent['announce-list']
        for item in li:
           # print(type(item[0]),end="")
           # print(item[0])
            trackers.append(item[0])
    except KeyError:
        return trackers
    return [trackers,filehash]
# getTrackers("833A8D93CC94FE1E699779C3C403B062763CE4BE.torrent")
def expansion(trakers,info_hash):
    l = len(trakers)

    for i in range(0,l):
        url = trakers[i] +"?info_hash="+info_hash+"&peer_id=AZ34343&port=6881"
        trakers[i] = url
    return trakers

v = []
def connect(url):
     try:
         reponse = urllib.request.urlopen(url)
         sleep(5)
         data = reponse.read()
         data = data.decode("utf-8")
         m = re.match("fail reason",data)
         if m is not None:
              v.append(1)
         else:
               v.append((0))
     except:
         v.append(0)


def communicate(fi):
       info= getTrackers(fi)

       trackers = expansion(info[0],info[1])
       len_trackers = len(trackers)
       print(trackers[0])
       print(trackers[1])
       threads = []


       for i in range(0,len_trackers):
            t=threading.Thread(target=connect,args={trackers[i]})
            threads.append(t)

       for i in range(0,len_trackers):
            threads[i].start()

       for i in range(0, len_trackers):
           threads[i].join()


def verify(file_name):
    n = isFileVaslid(file_name)
    if(n == 0):
        return False
    count = 0;
    for i in v:
        if i == 1:
            count+=1
    if count>0:
        return  True
    else:
        return False


