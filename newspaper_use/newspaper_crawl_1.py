import requests
from newspaper import Article
from newspaper import fulltext
url = u'http://www.sacbee.com/news/local/education/article2597911.html'
url = u'http://www.standard.net.au/story/2258145/lane-headed-for-state-parliament/'
article = Article(url)
article.download()
article.parse()
print article.authors
print article.publish_date
print article.text
# html = requests.get(url).text
# text = fulltext(html)
# print text
print "KEYWORD: ",article.keywords
print "SUMMARY: ",article.summary
