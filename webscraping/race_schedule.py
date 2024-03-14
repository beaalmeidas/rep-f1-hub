from bs4 import BeautifulSoup
import requests
import json


schedule_to_scrape = requests.get("https://racingnews365.com/formula-1-calendar-2024")
soup = BeautifulSoup(schedule_to_scrape.content, "html.parser")

for i in range (1,24):
    race_schedule = soup.find_all("tr")

schedule_list = []

for race in race_schedule[1:25]:
    columns = race.find_all("td")
    if len(columns) == 0:
        continue
    race_data = {
        "order": columns[0].text.strip(),
        "grand prix": columns[1].text.strip(),
        "circuit": columns[2].text.strip(),
        "date": columns[3].text.strip(),
    }
    schedule_list.append(race_data)

schedule = json.dumps(schedule_list, indent=4)
print(schedule)