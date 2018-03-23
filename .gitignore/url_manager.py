# coding=UTF-8

class UrlManger(object):
    def __init__(self):
        pass

    def getLianJiaUrls(self, region):
        # base_url="https://nj.lianjia.com/ershoufang/gulou/"
        base_url = "https://nj.lianjia.com/ershoufang/" + region + "/"
        urls = ([])
        i = 1
        while i <= 100:
            url = base_url + ("pg%s" % i)
            i += 1
            urls.append(url)
        return urls


if __name__ == "__main__":
    urls = UrlManger().getLianJiaUrls()
    for url in urls:
        print(url)
