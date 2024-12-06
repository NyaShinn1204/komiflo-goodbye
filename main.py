import re
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
class komiflo_downloader:
    def __init__(self, session):
        self.session = session
    def login(self, email, password):
        check_email = session.post("https://api.komiflo.com/user/exist", json={"email": email})
        if check_email.json()["status"] == "account_exists":
            pass
        
        payload = {
            "email": email,
            "password": password,
        }
        login_req = session.post("https://api.komiflo.com/session/login", json=payload)
        if login_req.json()["success"] == "false":
            print(login_req.json()["error"])
        
        if login_req.json()["success"]:
            print("[+] Success tp login")
    def download(self, url):
        
        default_directory = "download"
        
        # parse url to contend_id
        
        content_id = re.search(r"/comics/(\d+)/", url).group(1)
        comic_json = session.get(f"https://api.komiflo.com/content/id/{content_id}")
        img_list = []
        title = comic_json.json()["content"]["data"]["title"]
        for img in comic_json.json()["content"]["imgs"].values():
            img_list.append("https://cdn.komiflo.com/resized/396_desktop_medium_2x/" + img["filename"])
        
        base_dir = "komiflo"
        download_dir = os.path.join(default_directory, base_dir, content_id)
        
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        
        print(f"[+] Downloading title: {title} page: {len(img_list)}p")
        
        def download_image(url, index):
            tries = 3  # Number of retry attempts
            for attempt in range(tries):
                try:
                    response = session.get(url)
                    response.raise_for_status()  # Raise an exception for bad status codes
                    # Save the image with a sequential file name like image_1.jpg, image_2.jpg, etc.
                    filename = os.path.join(download_dir, f"image_{index+1}{os.path.splitext(url)[-1]}")
                    with open(filename, 'wb') as file:
                        file.write(response.content)
                    return url, True
                except requests.RequestException:
                    print(f"[-] Error downloading {url}, attempt {attempt + 1} of {tries}")
                    if attempt == tries - 1:
                        return url, False
        
        # マルチスレッドで画像をダウンロード
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(download_image, url, index) for index, url in enumerate(img_list)]
            for future in tqdm(as_completed(futures), total=len(futures), desc="Downloading", unit="file"):
                url, success = future.result()
                if not success:
                    print(f"[-] Failed to download {url}")
        
        print(f"[+] Download complete title: {title}")
        
        
session = requests.Session()
downloader = komiflo_downloader(session)
downloader.login("email", "password")

url_list = [
    "https://komiflo.com/#!/comics/25580/read/page/1"
]

for url in url_list:
    downloader.download(url)