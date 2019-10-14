from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from multiprocessing import Pool


def chrome_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("Chrome Browser Started")

    return driver


def mp_generate_browser(worker_count):
    start_time = time.time()
    p = Pool()

    worker = p.map(chrome_browser(), worker_count)

    p.close()
    p.join()

    end_time = time.time() - start_time  # starts tracking runtime

    print(f"Generating the selenium driver browser took {end_time} time using multiprocessing.")

    return worker


def browse(driver, url):
    driver.get(url)


if __name__ ==  '__main__':
    url = input("Enter URL to navigate to")
    worker_count = 3
    driver = mp_generate_browser(worker_count)
    browse(driver, url)
