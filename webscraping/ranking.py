from bs4 import BeautifulSoup
import requests
import json


drivers_to_scrape = requests.get("https://www.skysports.com/f1/standings")
soup = BeautifulSoup(drivers_to_scrape.content, "html.parser")

drivers_list = []

for i in range(1,21):
    drivers_ranking = soup.find_all("tr")
for pilot in drivers_ranking[1:23]:
    columns = pilot.find_all("td", attrs="standing-table__cell")
    if len(columns) == 0:
        continue
    driver_data = {
        "position": columns[0].text.strip(),
        "name": columns[1].text.strip(),
        "nationality": columns[2].text.strip(),
        "team": columns[3].text.strip(),
        "points": columns[4].text.strip(),
    }
    drivers_list.append(driver_data)

grid = json.dumps(drivers_list, indent=4)
print(grid)