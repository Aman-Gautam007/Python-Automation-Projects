from selenium import webdriver

search_string = input("What do you want to search for? ")
# This is done to structure the string 
# into search url.(This can be ignored)
search_string = search_string.replace(' ', '+') 

browser = webdriver.Chrome() # This will open the browser
#browser.get(f"https://www.google.com/search?q={search_string}") # This will search the string on google
for i in range(1):
    matched_elements = browser.get("https://www.google.com/search?q=" +
                                     search_string + "&start=" + str(i))