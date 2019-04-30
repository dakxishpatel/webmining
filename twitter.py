from selenium import webdriver
import time,codecs

url='https://twitter.com/SHAQ'

#open the browser and visit the url
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#find all elements with a class that ends in 'tweet-text'
tweets=driver.find_elements_by_css_selector("[class*=original-tweet]")

#write the tweets to a file
fw=codecs.open('tweets.txt','w',encoding='utf8')

for tweet in tweets:
    txt,retweets,comments,likes,date='NA','NA','NA','NA','NA'
    
    try: txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: print ('no Text')     

# Finding the Retweets in the SHAQ page
 # *** <button class="ProfileTweet-actionButton  js-actionButton js-actionRetweet" data-modal="ProfileTweet-retweet" type="button" aria-describedby="profile-tweet-action-
# retweet-count-aria-1117021448978280448"> *** 
 # *** <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">18</span> ***
    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no Retweets')
  
#Finding the Likes in the SHAQ page    
# *** <button class="ProfileTweet-actionButton js-actionButton js-actionFavorite" type="button" aria-describedby="profile-tweet-action-favorite-count-aria-
# 1117021448978280448"> ***
# *** <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">158</span> ***
    try:
        likesElement=tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        likes=likesElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no Likes')

# Finding the Comments in the SHAQ page 
# *** <button class="ProfileTweet-actionButton js-actionButton js-actionReply" data-modal="ProfileTweet-reply" type="button" aria-describedby="profile-tweet-action-reply-
# count-aria-1117021448978280448"> ***
# *** <span class="ProfileTweet-actionCountForPresentation" aria-hidden="true">20</span> ***
    try:
        commentsElement=tweet.find_element_by_css_selector("[class$=js-actionReply]")
        comments=commentsElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no Comments')

# Finding the Date the Tweet occured in SHAQ page        
    try:
         date = tweet.find_element_by_class_name("tweet-timestamp").text
    except:
        print ('no Date')

# Writing the tweet text, comments, retweets, likes and dates to a file
    fw.write(txt.replace('\n',' ')+'\t'+str(comments)+'\t'+str(retweets)+'\t'+str(likes)+'\t'+str(date)+'\n')


fw.close()


driver.quit()#close the browser
