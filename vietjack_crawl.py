import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')
def crawl_vietjack(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        content = soup.find('div', class_='content')

        if content:
            headings_h1 = content.find_all('h1', class_='title')
            headings_h2 = content.find_all('h2', class_='sub-title') 
            paragraphs = content.find_all('p') 
            with open('output2.txt', 'w', encoding='utf-8') as file:
                for heading in headings_h1:
                    file.write(f"{heading.get_text()}\n\n")
                for heading in headings_h2:
                    file.write(f"{heading.get_text()}\n\n")
                for paragraph in paragraphs:
                    if paragraph.find('a'):
                        continue
                    file.write(f"{paragraph.get_text()}\n\n")
                for sup in content.find_all('sup'):
                    sup.string = f"^{sup.text}"

                print("Đã lưu")
        else:
            print("Không tìm thấy nội dung.")
    else:
        print(f"{response.status_code}")
        
if __name__ == "__main__":
    url = "https://www.vietjack.com/sbt-toan-6-ket-noi/bai-1-27-trang-13-sbt-toan-lop-6-tap-1-ket-noi.jsp"
    crawl_vietjack(url)
