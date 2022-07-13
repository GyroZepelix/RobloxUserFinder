from bs4 import BeautifulSoup
import requests

keyword = "Meggle"

result = requests.get(f"https://www.roblox.com/search/users?keyword={keyword}")
searchPage = BeautifulSoup(result.text, "html.parser")
totalUsers = int(searchPage.find_all("span", class_="text-secondary")[1])

for pageIndex in range(0,totalUsers//12):
    print("---| Next Page |--------------")
    result = requests.get(f"https://www.roblox.com/search/users?keyword={keyword}&startIndex={pageIndex*12}")
    searchPage = BeautifulSoup(result.text, "html.parser")
    users = searchPage.find_all("li", class_="avatar-card-fullbody")
    for user in users:
        try:
            user.find("a", class_="avatar-status")
        except:
            continue
        userLink = user.find("a")
        print(user)









# userCnt = 43000000
# for i in range(1, userCnt):
#     print(f"checking ID: {i}")
#     result = requests.get(f"https://www.roblox.com/users/{i}/profile")
#     doc = BeautifulSoup(result.text, "html.parser")
#     try:
#         name = doc.find_all(class_="profile-display-name")[0]
#     except:
#         continue

#     try:
#        icon = doc.find_all(class_="profile-avatar-status")[0]
#     except:
#        continue

#     if (name.text != "@DomiGamer2303"):
#         continue

#     print("found!")
#     break