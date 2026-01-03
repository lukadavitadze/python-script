import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

with open("gdpr_recitals_1_173.txt", "w", encoding="utf-8") as file:

    for i in range(1, 174):
        url = f"https://gdpr-info.eu/recitals/no-{i}/"
        print(f"მიმდინარეობს დამუშავება: {url}")

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"❌ გვერდი ვერ მოიძებნა: no-{i}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        entry_content = soup.find("div", class_="entry-content")
        if not entry_content:
            print(f"⚠ entry-content ვერ მოიძებნა: no-{i}")
            continue

        paragraphs = entry_content.find_all("p")
        texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]

        if not texts:
            print(f"⚠ ტექსტი ცარიელია: no-{i}")
            continue

        # ===== ფაილში ჩაწერა =====
        file.write("=" * 60 + "\n")
        file.write(f"GDPR RECITAL – NO {i}\n")
        file.write(f"SOURCE: https://gdpr-info.eu/recitals/no-{i}/\n")
        file.write("=" * 60 + "\n\n")

        for text in texts:
            file.write(text + "\n\n")

        # ეთიკური scraping – პაუზა
        time.sleep(0.5)

print("\n✔ ყველა recital ჩაწერილია სათაურებით ფაილში: gdpr_recitals_1_173.txt")
