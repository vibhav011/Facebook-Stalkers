from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.facebook.com')
userid = driver.find_element_by_id('email')
userid.send_keys('your-username')				# Enter your username here
psw = driver.find_element_by_id('pass')
psw.send_keys('your-password')					# Enter your password here
psw.submit()

driver.get('view-source:https://www.facebook.com/')

htmlText = driver.find_element_by_xpath("//html")
s = htmlText.text

ind = int(s.find("InitialChatFriendsList"))
word = s[ind:ind+4]

while word != "list" :
	ind += 1
	word = s[ind:ind+4]

ind += 6
usrID = ""

def printName(x) :
	driver.get('https://www.facebook.com/'+x)
	try:
		name = driver.find_element_by_xpath("//span[@id='fb-timeline-cover-name']//child::a").text
		print(name)
	except:
		print("hag diya")

while s[ind] != "]" :
	if s[ind] == '"' :
		usrID = ""
	elif s[ind] == "-" :
		printName(usrID)
		ind += 3
	else :
		usrID += s[ind]
	ind += 1


#print(s[ind+7: ind+21])
