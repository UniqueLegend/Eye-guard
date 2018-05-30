# coding: utf-8

import libtorrent as lt
import sys
import time

ses = lt.session()
ses.listen_on(6881, 6891)

e = lt.bdecode(open("./torrents/ubunut12-04.torrent", 'rb').read())
info = lt.torrent_info(e)

params = { 'save_path': '.', \
        'storage_mode': lt.storage_mode_t.storage_mode_sparse, \
        'ti': info }
h = ses.add_torrent(params)

s = h.status()
while (not s.is_seeding):
        s = h.status()
        sys.stdout.write('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' %
                (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
                s.num_peers, s.state)
	)
	sys.stdout.write("\r")
	sys.stdout.flush()

        time.sleep(1)

