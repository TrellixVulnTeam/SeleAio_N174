import urllib, htmllib, formatter, re, sys
 
#Baraye Gerftan Argoman Dar Mohit gitBash az .argv[1] estefade mikonim
url = sys.argv[1]
#dar inja url Vared Shode Ra gerfte va b motghayer website enteqal midim
website = urllib.urlopen("http://"+url)
#dar inja URL vared Shode Ra khande Va DATA'HA Ra  Ba estefade Az Tab'e READ() Mikhanim
data = website.read()
#Dar inja url ro mibandim
website.close()
#dar inja Ham GHalebBandi Mikonim Va b dalil inke Meqdari nadaram k bash Kar konam b hamin dalil az  NullWriter()Estefade mikonam
format = formatter.AbstractFormatter(formatter.NullWriter())
# Dar inja ham ptext ro qaleb mikonam b khatere inke mikham Tag HTML Bekhonam
ptext = htmllib.HTMLParser(format)
#Dar inja ham Meqdar mojod dar DATA ra b ptext pas midam ta tab'e feed ann Ra TRACE konad
ptext.feed(data)
 
links = []
#Dar Inja Baraye Joda sazi Ebarathaye mojod dar PTEXT az anchorlist Estefade mikonam
links = ptext.anchorlist
 
for link in links:
    #Dar INja Agar Link Mojod Bod Ejaze Anjam Agar Nabod Khyr
    if re.search('http', link) != None:
        #Chap LINK
        print (link)
        # Az inja B bad dobare Tekrar Mikonam K B Linkhaye dge bere va Bekhone va  Dar ekhtoyar  Code qarar bede
        #Baqie CodeHA Dar Bala Tozih Dade Shode And.
        website = urllib.urlopen(link)
        data = website.read()
        website.close()
        ptext = htmllib.HTMLParser(format)
        ptext.feed(data)
        morelinks = ptext.anchorlist
        for alink in morelinks:
            if re.search('http', alink) != None:
                links.append(alink)