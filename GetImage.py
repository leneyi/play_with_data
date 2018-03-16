import urllib.request
import re
import urllib
#import sys  
#reload(sys)  
#sys.setdefaultencoding('utf8')
#http://www.jianshu.com/p/696922f268df
def download_page(url):
    page = urllib.request.Request(url)
    #response = urllib.request.urlopen(page)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read()
    #print(html)
    return html


def getImg(html):
    #regx = r'src="(.+?\.jpg)" pic_ext'
 #   regx= r'src="([.*\S]*\.jpg)" pic_ext="jpeg"' # for tieba the key is a right expression
    regx = r'http://[\S]*\.jpg' # for huaban
    pattern = re.compile(regx)
    get_img = re.findall(pattern, repr(html));# repr convert expression string
    print(get_img);
    num = 1
    for img in get_img:
        image = download_page(img) 
        with open('%s.jpg'%num, 'wb') as fp:
           fp.write(image)
           print('downloading %s images'%num);
           num +=1
    return
    #return imglist

    
html = download_page('http://huaban.com/favorite/beauty/');#valid http://huaban.com/favorite/beauty/
#https://tieba.baidu.com/p/3205263090 none
getImg(html);
