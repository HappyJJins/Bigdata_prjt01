from bs4 import BeautifulSoup as bs
import time
import requests
from db import getConn
from dbInsert import insertData

# DB를 생성한다. 컬럼은 data, category, title. 테이블 생성 코드는 createtablecode.py에 있다.
# 1시간마다 자동으로 작동한다. 6개의 사이트를 접속하여, db에 data, category, title(구분자|) 형식으로 저장한다.

def crowling(category):

    url = makeLink(category)
    html = requests.get(url)
    soup = bs(html.text, "html.parser")

    ranking = soup.find('ol',{'class':'ranking_list'})
    title = set(ranking.findAll('a', {'class':getTag(category)}))
    title_list = []
    for el in title:
        title_list.append(el['title'])
    date = todayDate()
    cate = category
    title = "|".join(title_list).replace('"', "")
    insertData(date, category, title)


def getTag(cate):
    tag = {
        "politics":'nclicks(rnk.gov)',
        "economy":'nclicks(rnk.eco)',
        "society":'nclicks(rnk.soc)',
        "culture":'nclicks(rnk.lif)',
        "world":'nclicks(rnk.wor)',
        "science":'nclicks(rnk.sci)'
    }
    return tag[cate]


def makeLink(cate):
    """
    politics(정치) economy(경제) society(사회) culture(문화) world(세계) science(과학)을 입력받아 현재 기사의 링크 문자열을 반환한다.
    """
    category = {
        "politics":100,
        "economy":101,
        "society":102,
        "culture":103,
        "world":104,
        "science":105
    }
    return "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId={}&date={}".format(category[cate], todayDate())


def todayDate():
    return time.strftime('%Y%m%d', time.localtime(time.time()))


# politics(정치) economy(경제) society(사회) culture(문화) world(세계) science(과학)을 입력받아 현재 기사의 링크 문자열을 반환한다.
if __name__ == "__main__":
    while True:
        for cate in ["politics", "economy", "society", "culture", "world", "science"]:
            crowling(cate)
            time.sleep(10)
        time.sleep(3600)