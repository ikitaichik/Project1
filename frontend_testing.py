import time
from selenium import webdriver


def frontend_test(id):
    try:
        driver = webdriver.Chrome(executable_path="/users/ikitaichik/downloads/chromedriver")
        driver.get(f"http://127.0.0.1:5001/users/get_user_data/{id}")
        return driver.find_element_by_id('user').text
    except Exception as e:
        print("Test failed!")
    finally:
        time.sleep(2)
        driver.quit()


if __name__ == '__main__':
    try:
        if "Itzik" == frontend_test(1):
            print("Test succeeded")
        else:
            raise Exception
    except:
        print("Test failed")
