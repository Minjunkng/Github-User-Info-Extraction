from bs4 import BeautifulSoup
import requests

x = True
while x:
    user_name = input("Enter the username(Case sensitive): ")
    web_address = "https://github.com/" + user_name
    html_txt = requests.get(web_address).text

    soup = BeautifulSoup(html_txt, "lxml")
    contributions = soup.find("h2", class_ = "f4 text-normal mb-2")
    num_friends = soup.find("a", class_ = "Link--secondary no-underline no-wrap")
    num_repo = soup.find("span", class_ = "Counter")

    try:
        print("\n" +  user_name + " has:\n" + contributions.text.split()[0] + " contributions this year")
        if int(num_friends.text.split()[0]) == 0:
            print("Zero friends on github :(")
        elif int(num_friends.text.split()[0]) == 1:
            print("One friend on github")
        else:
            print(num_friends.text.split()[0] + " friends on github")
        print(num_repo.text.split()[0] + " public repositories\n")
        x = False
    except:
        print("\nInvalid username, try again.\n")