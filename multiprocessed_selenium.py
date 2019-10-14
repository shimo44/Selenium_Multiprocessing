from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from multiprocessing import Process


def chrome_browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("Chrome Browser Started")

    return driver

def goto_perficient(driver):
    driver.get("http://perficient.com")


def mp_worker(driver=chrome_browser()):
    start_time = time.time()

    p = Process(goto_perficient(driver)).run()

    p.start()
    p.join()
    # p.terminate()

    end_time = time.time() - start_time  # starts tracking runtime

    print(f"Generating the selenium driver browser took {end_time} time using multiprocessing.")


if __name__ ==  '__main__':
    mp_worker()
