import mechanize
import urllib
from urllib import urlopen
import cookielib
import BeautifulSoup
import html2text
import re
import sys
import StringIO
from urllib2 import HTTPError
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import pickle

# Initialize mechanize headless browser
br = mechanize.Browser()

# This is where we hold our cookies
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br._ua_handlers['_cookies'].cookiejar

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but doesn't hang on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# UA
br.addheaders = [('User-agent', 'Chrome')]

# Initialize selenium with a headless driver as well for behind the scenes magic
# Have phantomjs.exe in same directory as where this file is
myPhantomFolder = os.getcwd()
browser = webdriver.PhantomJS(executable_path=(str(myPhantomFolder)+'\\phantomjs.exe'))

# Freshen up
browser.delete_all_cookies()

print'............................................................'
print'......77777......................................77777......'
print'.....777777...............:?+++??...............777777......'
print'...7 777777...........??+++++++++++++...........,7777777,...'
print'..777777777.........+++++++++++++++++++~........,77777777 ..'
print'..7777777777?.....?++.+?++++++++++++++.++......7777777777 ..'
print'...777.: 77777...++:.+.??.++++++++++.++.++...7777777.7777...'
print'.........777777.++++++++++++++++++++:++?~++..77777..........'
print'...........777.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~. 77~...........'
print'............,7.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.7.............'
print'..............:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~...............'
print'.......?+????+++??++++++++++++++++++??+++++++?++??+??.......'
print'.......??????????????????????????????????????????????.......'
print'..............:7777777 7777777777777777777777...............'
print'...............7777 +......777777......777777...............'
print'...............77777........777 ........7777................'
print'................777,........777 ........777.................'
print'.................777.......77777........77..................'
print'..................777.....7777777?....I 7...................'
print'....................7777 777...7777 777.....................'
print'......................=777777 7777777.......................'
print'.....................777...........=77.~....................'
print'..................77.777I7 77.77 I7777+77...................'
print'................777.77...7777.7777.:.,7.777.................'
print'...............7777.7 77.77~...:77.777 .77777...............'
print'........777..777777.7..7.7777.7777.77...777777..77 .........'
print'.......7777777777 ..7777....+.I:...?777..77777777777~.......'
print'......,777777777....:777777777777777777....7777777777.......'
print'.......+7777777~.....7777777777777777 ......77777777........'
print'..........777777......777777777777777......777777...........'
print'..........:77777........77777777777........777777...........'
print'............,~...............................++.............\n'

# Normal Three Digit associated with each respective size
# Not goint to throw an exception if undefined so please only use the sizes provided. KThnx.
sizeIn = raw_input("Size (8-12): ")
if (sizeIn=='8'):
    threeDigit = "610"
if (sizeIn=='8.5'):
    threeDigit = "620"    
if (sizeIn=='9'):
    threeDigit = "630"
if (sizeIn=='9.5'):
    threeDigit = "640"
if (sizeIn=='10'):
    threeDigit = "650"    
if (sizeIn=='10.5'):
    threeDigit = "660"
if (sizeIn=='11'):
    threeDigit = "670"
if (sizeIn=='11.5'):
    threeDigit = "680"    
if (sizeIn=='12'):
    threeDigit = "690"

# Self explanatory variables
# Stub out/play with url strings to see results and causality
cart_url="https://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-Show"
url = "http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct?layer=Add%20To%20Bag%20overlay&pid=B35309_"+str(threeDigit)+"&Quantity=1&masterPid=B35309add-to-cart-button="

# Test Cases below
'''
url="http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct?layer=Add%20To%20Bag%20overlay&pid=B26813_650&Quantity=1&masterPid=B26813add-to-cart-button="
url="http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct?layer=Add%20To%20Bag%20overlay&pid=B35996_660&Quantity=1&masterPid=B35996add-to-cart-button="
url="http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct?layer=Add%20To%20Bag%20overlay&pid=M18838_610&Quantity=1&masterPid=M18838add-to-cart-button="
url="http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct?layer=Add%20To%20Bag%20overlay&pid=M29395_670&Quantity=1&masterPid=M29395add-to-cart-button="
'''

# Counter variable to keep track of tries
loop = 1
 
print "\nRunning..."
print "Target (StyleCode): " + str(url.split("add-to-cart-button=")[0].split("=")[len(url.split("add-to-cart-button=")[0].split("="))-1])

while (1==1):
    try:
        # Cool your jets - please don't be an asshat. Leave some delay
        time.sleep(3)

	# Let's get mechanize and selenium to the cart call address
	# and see what's going on
        br.open(str(url))
        browser.get(url)

	# Scrape page for anything in span tag.
	# Can use the contrapositive with the <strong> tag with the null on not yet available items
        regex='<span>(.+?)</span>'
        pattern = re.compile(regex)
        htmltext = br.open(str(url)).read()
        title = re.findall(pattern,htmltext)
        
        # Just to see what's going on - image saved in same directory as this file
        browser.save_screenshot("addRequest.png")

        # If page has an element of <span> tag, trigger - ATC
        if len(title)>0:
            # Whoop-dee-fucking doo. Congrats.
            print "Try: " + str(loop) + " - ATC success! Getting cart...\n"
            # Bringing to cart page for easiser load on cookies
            br.open(cart_url)
            # Circumvent bullshit of webbrowser not being able to handle headers
            # Saving successful ATC cookies in same folder for reuse
            pickle.dump(browser.get_cookies(), open("cookies.pkl","wb"))
            # Changing webdriver - sewing a head onto it - chromedriver.exe
            browser = webdriver.Chrome()
            # Fetching that cookie file
            cookies = pickle.load(open("cookies.pkl", "rb"))
            
            # Cookies to console
            print "Here, have some cookies ya bish..."
            print cookies 
            # Domain specific cookies so now opening physical browser to cart page
            browser.get(cart_url)
            # Passing cookies into the header 
            for cookie in cookies:
                browser.add_cookie(cookie)
            # Refresh to see our successful cookies
            browser.refresh() 
            # Okay Adidas
            browser.refresh()
            # Great, it's in your cart - instead of doing things properly and exiting/deleting the created cookie file,
            # I'm just going to sit you in timeout.
            time.sleep(600)
     
        # Sorry no <span> tags in your html document
        if len(title)==0:
             print "Try: " + str(loop) + " - Not yet available \n"
            
        # Increment count
        loop+=1
        
    except:
        print "Try: " + str(loop) + " - IDEK WHAT YOUR DOING BRUH. \n"
        loop+=1
        continue
    
os.system("pause")



