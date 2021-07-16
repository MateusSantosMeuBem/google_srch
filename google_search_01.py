from selenium import webdriver
from pyfiglet import Figlet
from time import sleep
from sys import stdout

creator = 'by Mateus Santos'
for i in creator:
    print(i, end='')
    stdout.flush()
    sleep(0.07)
print()

browser = webdriver.Chrome()

# Maximize window
browser.maximize_window()

# Website where it is looking for
url = 'https://www.google.com'

# Object to creat texts
f = Figlet(font='standard')

print(f.renderText('What are you looking for?'))

# What it will looking for
search = input('--> ')

# Website from where it will search
web_sites = {
                'Stack Overflow' : 'stackoverflow.com',
                'Git Hub' : 'github.com',
                'W3Schools' : 'w3schools.com',
                'MDN' : 'developer.mozilla.org',
                'Clube do Hardware' : 'clubedohardware.com.br',
                'Viva o Linux' : 'vivaolinux.com.br',
                'Alura Fórum' : 'cursos.alura.com.br/forum',
                'QTStack' : 'qastack.com.br'
}
c = 1

print(f.renderText('Where ?'))
# Menu
for i, j in web_sites.items():
    print(f' {c} - {i:.<25} {j:<30}')
    c += 1
resp = int(input('--> '))
# Checking if it's a right answer
while resp < 1 or resp > len(web_sites):
    print('[WRONG OPTION]')
    resp = int(input('--> '))

# Getting domain chosen
place = list(web_sites.values())[resp-1]

# Starting in the url
browser.get(url)

# Typing the search
browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(search)
# Clicking in the button to search
browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

# Showing from where it is looking for
print(f.renderText(list(web_sites.keys())[resp-1]))

print('Searchig...')
while True:
    # Looing till first 15 pages
    for i in range(1, 15):
        try:
            # Getting url to this link
            url = browser.find_element_by_xpath(f'//*[@id="rso"]/div[{i}]/div/div/div[1]/a').get_attribute("href")
            # If this where it is looking for...
            if place in url:
                # It opens this link in a new tab
                browser.execute_script(f"window.open('{url}', '_blank')")
        except:
            pass

    try:
        # Pass next page
        browser.find_element_by_xpath(f'//*[@id="pnnext"]/span[1]').click()
    except:
        print('[PAGES ENDED]')
        break
