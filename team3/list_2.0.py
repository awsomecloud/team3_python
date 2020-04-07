import feedparser
import time
import sys
import openpyxl
import datetime

url = "https://aws.amazon.com/about-aws/whats-new/recent/feed/" #what's New list
# last_modified = 'Mon, 06 Apr 2000 02:07:40 GMT'

while True:
    file = open("modified.txt",'r')
    last_modified = file.readline()
    print("1.현재 modified 값 " + last_modified)
    last_modified_date = datetime.datetime.strptime(last_modified, '%a, %d %b %Y %H:%M:%S %Z ')
    file.close()

    feed = feedparser.parse(url, modified=last_modified)

    if feed.get('status') == 304:
        print ("...")

    else:

        for i in range(len(feed.entries)) :
            print("Refresh feed")
            published = str(feed.entries[i].published).replace("+0000","")
            published_date = datetime.datetime.strptime(published,'%a, %d %b %Y %H:%M:%S  ')

            if published_date > last_modified_date :
                print ("New Feed !!--> ", feed.entries[i].title)
                with open ('List03.txt', 'a' , encoding="utf8") as f :
                    f.write(str(published_date) + "," + feed.entries[i].link + "," + feed.entries[i].title+"\n")
            else :
                pass

        with open('modified.txt', 'w') as m:
            last_modified = feed.get('modified', '')
            m.write(last_modified + "\n")
            print("3.업데이트 된 modified 값 " + last_modified)
        m.close()

    time.sleep(100)

    # 'Fri, 03 Apr 2020 00:46:45 +0000'
    # 'Fri, 03 Apr 2020 01:07:39 GMT'

