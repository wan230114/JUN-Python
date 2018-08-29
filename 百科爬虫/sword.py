# 该版本用于动态生成查找内容，解决同义词条过多卡顿的问题
import urllib.request
import re
# import pymysql


def get_baike(word):

    keywd_cn = word
    keywd = urllib.request.quote(keywd_cn)  # 编码
    url = "https://baike.baidu.com/item/" + keywd

    # 1）第一次获取网页
    try:  # 打开网页
        file = urllib.request.urlopen(url, timeout=10)
        data = file.read().decode()
        # data = open("geted_web/%s.html" % (word), "rb").read().d ecode("utf-8")

        # 2）判断是否存在同义词的二级界面，若存在则更新url和data
        jg_TY = re.search(
            r'<div class="lemmaWgt-subLemmaListTitle">\n(.*?)</div>\n', data)
        if jg_TY:  # 如果存在同义词二级界面
            sjg_TY = jg_TY.group()
            url += "/%s" % (re.search(r'data-lemmaid="\d*', sjg_TY).group()
                            ).replace('data-lemmaid="', '')
            data = urllib.request.urlopen(url).read().decode()

        # 3）判断词条是否存在，若存在结果则匹配结果s
        element = r'<div class="lemma-summary" label-module="lemmaSummary">(.*?)</div>\n'
        L = re.findall(element, data, re.I | re.S | re.M)
        pp_L = 1  # 设置指标决定是否进行近义词查询
        if L:
            s = L[0].replace("\n", "")
            s = re.sub('<div class="para" label-module="para">', '\n', s)
            s = re.sub('<.*?>|&nbsp;', '', s).strip()
            send = "%s：\n%s\n" % (word, s)
        else:
            send = "抱歉，您搜索的词条暂未被收录"
            pp_L = 0
        yield send

        # 4）寻找是否有近义词，有则添加到匹配结果s
        if pp_L == 1:
            dt_TY = re.findall(
                r'<ul class="polysemantList-wrapper cmn-clearfix(.*?)</ul>', data, re.I | re.S | re.M)
            if dt_TY:
                sdt_TY = dt_TY[0]
                L_TY = re.findall('<a title=(.*?)</a>',
                                  sdt_TY, re.I | re.S | re.M)
                # print(L_TY)
                for n in range(len(L_TY)):
                    sL_TY = L_TY[n]
                    stitle = re.match('".*"', sL_TY).group()
                    st = "【同义词%d】  %s(%s)：\n" % (n+1, word, stitle)
                    url_TY = "https://baike.baidu.com/%s" % (
                        re.search(r"item/.*#viewPageContent", sL_TY).group())
                    data_st = urllib.request.urlopen(url_TY).read().decode()
                    L_data_st = re.findall(
                        element, data_st, re.I | re.S | re.M)
                    s2 = L_data_st[0].replace("\n", "")
                    s2 = re.sub(
                        '<div class="para" label-module="para">', '\n', s2)
                    s2 = re.sub('<.*?>|&nbsp;', '', s2).strip()
                    s_TY = "\n" + st + s2 + "\n"
                    send = s_TY
                    yield send
    except Exception as e:
        print("异常-->"+str(e))
        send = "请求超时，请确保网络联通后重试。"
        yield send


def main():

    word = "李白"

    # 1爬虫获取返回并打印百科查询结果字符串。
    data = get_baike(word)
    for i in data:
        print(i)


if __name__ == "__main__":
    main()
