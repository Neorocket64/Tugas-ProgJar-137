import logging
import requests
import os
import threading


def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':
    url_gambar = []
    url_gambar.append('https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg')
    url_gambar.append('https://i0.wp.com/saintif.com/wp-content/uploads/2018/05/Pohon-header.png')
    url_gambar.append('https://www.greeners.co/wp-content/uploads/2017/05/Pohon-Ternyata-Bisa-Menjadi-Sumber-Gas-Metan.jpg')
    url_gambar.append('https://img.okezone.com/content/2018/03/15/56/1873448/pohon-tertinggi-di-dunia-hyperion-miliki-tinggi-lebih-dari-100-meter-Nb6oimqabC.jpg')

    threads = []
    for i in range(4):
        t = threading.Thread(target=download_gambar,args=(url_gambar[i],))
        threads.append(t)
        
    for thr in threads:
        thr.start()


