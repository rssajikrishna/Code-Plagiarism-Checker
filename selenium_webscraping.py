from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from hackerank_sql import insert_submission

def scrape_hackerrank(username, password, contest_slug):
    driver = webdriver.Chrome()

    driver.get("https://www.hackerrank.com/auth/login")
    time.sleep(2)

    driver.find_element(By.ID, "input-1").send_keys(username)
    driver.find_element(By.ID, "input-2").send_keys(password)
    driver.find_element(By.CLASS_NAME, "ui-btn").click()
    time.sleep(5)

    submissions_url = f"https://www.hackerrank.com/contests/mock-1744059270/submissions"
    driver.get(submissions_url)
    time.sleep(5)

    # NOTE: You need to extend this logic to paginate and scrape code
    # Fake data insertion for demo
    insert_submission("user123", "problem_slug_1", "print('hello')", "https://hrlink")

    driver.quit()


