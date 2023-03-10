import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def clear_field(el):
    el.send_keys(Keys.CONTROL + 'a')
    el.send_keys(Keys.BACK_SPACE)
    el.send_keys("Clark")


class TestForLogin:

    def test_for_login(self):
        self.driver.maximize_window()
        login_input = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "input[name='username']")
        password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        login_button = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, ".oxd-button")

        login_input.click()
        login_input.send_keys('Admin')
        assert login_input.get_attribute('value') == 'Admin'

        password_input.click()
        password_input.send_keys('admin123')
        assert password_input.get_attribute('value') == 'admin123'

        login_button.click()

        my_info_button = self.get_wait.wait_for_element_to_be_clickable(By.XPATH, '//*[text() ="My Info"]')
        my_info_button.click()

        username_input = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "input[name='firstName']")
        username_input.click()
        clear_field(username_input)
        assert username_input.get_attribute('value') == 'Clark'

        mid_name_input = self.get_wait.wait_for_element_to_be_clickable(By.XPATH, "//input[@placeholder='Middle Name']")
        mid_name_input.click()
        clear_field(mid_name_input)
        assert mid_name_input.get_attribute('value') == 'Clark'

    def test_for_calendar(self):
        calendar_input = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR,
                                                                        'div[class="oxd-date-input"]').click()
        calendar_div = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, ".oxd-date-input-calendar", 60)
        option_list = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-calendar-date-wrapper .oxd-calendar-date")

        for option in option_list:
            current = option.text
            if current == '7':
                option.click()
                break

    def test_for_nationality(self):
        nationality_part = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, ".oxd-select-text", ).click()
        # self.driver.execute_script("arguments[0].click();", nationality_part)
        option_to_choose = "Haitian"
        huge_div = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "div[role='listbox']", 60)
        option_list = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-option']//span")

        print(len(option_list))
        for option in option_list:
            current = option.text

            if current == option_to_choose:
                option.click()
                break
            print(current)

    def test_for_marital_status(self):
        inputs = self.driver.find_elements(By.CSS_SELECTOR, ".oxd-select-text-input")

        marital_status_input = inputs[1].click()
        option_div = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "div[role='listbox']", 60)
        option_list = self.driver.find_elements(By.XPATH, "//div[@class='oxd-select-option']//span")
        option_to_choose = "Single"

        for option in option_list:
            current = option.text

            if current == option_to_choose:
                option.click()
                break
            print(current)

    def test_gender(self):
        radio_button = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, ".oxd-radio-wrapper label")
        self.driver.execute_script("arguments[0].click();", radio_button)
        save_button = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, ".oxd-button").click()
