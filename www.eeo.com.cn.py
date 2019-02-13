import requests
from lxml import etree

#�����Ӳ���

def num(*x):
    base_url = 'http://app.eeo.com.cn/?app=epaper&controller=text&action=eeolist&cid=261&qid={}'
    new_qishu = []
    for x in range(x[0], x[1]):
        url = base_url.format(x)
        new_qishu.append(url)
    return new_qishu

#��ȡһ�����������µ�url
def get_new_url(url):
    new_all_url = []
    respone = requests.get(url)
    text = respone.content.decode("utf-8")
    html = etree.HTML(text)
    #ҳ��url ��������li �ټ�ȥ��һҳ����һ������li �õ�ʵ�� ҳ��
    new_age_num = html.xpath("//div[@class='wzlist_page font14']/ul/li")
    t = len(new_age_num)-2
    base_url = url + '&page={}'
    for x in range(1, t+1):
        url = base_url.format(x)
        respone1 = requests.get(url)
        text1 = respone1.content.decode("utf-8")
        html1 = etree.HTML(text1)
        all_url = html.xpath("//ul[@class='new_list']/li/a/@href")
        print()
        for url in all_url:
            new_all_url.append(url)
    return new_all_url

#����get_new_url(url) �õ�һ�ڵ�ȫ���������ӣ���ȡ������������ҳ�����ݡ�
def new_info():
    #������ȡ�ڿ���Χ�����ֻ��ȡһ�ڣ���ֻ��Ҫ��904�� ��904��905��
    qishu_url = num(903,905)
    for url in qishu_url:
       all_url = get_new_url(url)

       new = {}
       for url in all_url:
           respone1 = requests.get(url)
           text1 = respone1.content.decode("utf-8")
           html1 = etree.HTML(text1)
           new['title'] = html1.xpath("//div[@class='xd-b-left']//h1/text()")[0]
           new['auth'] = html1.xpath("//div[@class='xd-b-b']/p/text()")[0]
           new['time'] = html1.xpath("//div[@class='xd-b-left']//p/span/text()")[0]
           new['content'] = html1.xpath("//div[@class='xx_boxsing']/p[position()>1]/text()")
           print(new)


if __name__ =='__main__':
    new_info()