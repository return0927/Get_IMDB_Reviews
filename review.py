import urllib2 as urllib
import bs4 as BeautifulSoup

url = str(raw_input('Please input IMDB link to parse into here\n>>> ' ))
html = urllib.urlopen(url)
soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
reviews = soup.findAll('div', attrs={'id':'tn15content'})
reviews = reviews[0]
reviews = reviews.findAll('p')
blank_count = list()

for line in range(len(reviews)):
    reviews[line] = str(reviews[line]).replace("<p>","")
    reviews[line] = str(reviews[line]).replace("</p>","")
    reviews[line] = str(reviews[line]).replace("<br>","")
    reviews[line] = str(reviews[line]).replace("</br>","")
    reviews[line] = str(reviews[line]).replace("\'","'")
    reviews[line] = str(reviews[line]).replace("\'","'")
    if reviews[line] == "<b>*** This review may contain spoilers ***</b>":
        blank_count.append(line)
    if reviews[line] == '<a href="reviews-enter">Add another review</a>':
        blank_count.append(line)

print("Done! %d reviews detected." % (len(reviews) - len(blank_count)))
print("\n\n    1. Save as file \n    2. View in this window (can make some rags\n")
menu = str(input(">>> "))

if menu == "1":
    while 1:
        filename = str(raw_input("\n    Filename: "))
        if filename:
            for review_nb in range(len(reviews)):
                for brk in blank_count:
                    if brk == review_nb:
                        do_not = 1
                        break
                    else:
                        do_not = 0
                if not do_not:
                    with open(str(filename)+"_"+str(review_nb)+".txt","w") as f:
                        f.write(reviews[review_nb])
            print(" Done!")
            break
        else:
            print("Invalid Filename! \n")

if menu == "2":
    for review_nb in range(len(reviews)):
        for brk in blank_count:
            if brk == review_nb:
                do_not = 1
                break
            else:
                do_not = 0
        if not do_not:
            print(" ============== < %d / %d > ============== " % (review_nb, len(reviews)))
            for line in reviews[review_nb].split("\n"):
                print(line)
