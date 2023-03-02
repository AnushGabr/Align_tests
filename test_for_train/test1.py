from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from wait.wait import Wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = None
get_wait = None


def get_url(url):
    global driver, get_wait
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    get_wait = Wait(driver)


class TestsForRadioButtons:
    get_url('https://courses.letskodeit.com/practice')

    def test_only_one_radio_button_is_selected(self):
        bmw_button = get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "#bmwradio")
        benz_button = driver.find_element(By.CSS_SELECTOR, "#benzradio")
        honda_button = driver.find_element(By.CSS_SELECTOR, "#hondaradio")

        assert not bmw_button.is_selected()
        bmw_button.click()

        assert bmw_button.is_selected()
        assert not benz_button.is_selected()
        assert not honda_button.is_selected()

        assert not benz_button.is_selected()
        benz_button.click()

        assert benz_button.is_selected()
        assert not honda_button.is_selected()
        assert not bmw_button.is_selected()

        assert not honda_button.is_selected()
        honda_button.click()
        assert honda_button.is_selected()
        assert not bmw_button.is_selected()
        assert not benz_button.is_selected()


class TestsForCheckButtons:

    def test_only_one_checkbox_button_is_selected(self):
        bmw_check = get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "#bmwcheck")
        benz_check = driver.find_element(By.CSS_SELECTOR, "#benzcheck")
        honda_check = driver.find_element(By.CSS_SELECTOR, "#hondacheck")

        assert not bmw_check.is_selected()

        bmw_check.click()
        bmw_check.is_selected()

        assert not benz_check.is_selected()
        assert not honda_check.is_selected()
        bmw_check.click()

        # for benz

        assert not bmw_check.is_selected()
        assert not benz_check.is_selected()

        benz_check.click()
        benz_check.is_selected()

        assert not bmw_check.is_selected()
        assert not honda_check.is_selected()
        benz_check.click()

        # for honda

        assert not benz_check.is_selected()
        assert not honda_check.is_selected()

        honda_check.click()
        honda_check.is_selected()

        assert not bmw_check.is_selected()
        assert not benz_check.is_selected()
        honda_check.click()

    def test_three_buttons_is_selected_then_one_removed(self):
        bmw_check = get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "#bmwcheck")
        benz_check = driver.find_element(By.CSS_SELECTOR, "#benzcheck")
        honda_check = driver.find_element(By.CSS_SELECTOR, "#hondacheck")

        assert not bmw_check.is_selected()
        assert not benz_check.is_selected()
        assert not honda_check.is_selected()

        bmw_check.click()
        benz_check.click()
        honda_check.click()

        assert bmw_check.is_selected()
        assert benz_check.is_selected()
        assert honda_check.is_selected()

        bmw_check.click()

        assert not bmw_check.is_selected()
        assert benz_check.is_selected()
        assert honda_check.is_selected()


class TestsForSwitchWindow:

    def test_is_new_window_opened(self):
        button = get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "#openwindow")
        button.click()

        original_window = driver.current_window_handle

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                search_form = get_wait.wait_for_element(By.CSS_SELECTOR, '#search')
                assert search_form
                break
        driver.close()
        driver.switch_to.window(original_window)


class TestForSwitchTab:

    def test_is_new_tab_opened(self):
        button = get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "#opentab")
        button.click()
        original_window = driver.current_window_handle

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                search_form = get_wait.wait_for_element(By.CSS_SELECTOR, '#search')
                assert search_form
                break
        driver.close()
        driver.switch_to.window(original_window)




