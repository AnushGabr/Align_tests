import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TestsForRadioButtons:

    def test_only_one_radio_button_is_selected(self):
        bmw_button = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "#bmwradio")
        benz_button = self.driver.find_element(By.CSS_SELECTOR, "#benzradio")
        honda_button = self.driver.find_element(By.CSS_SELECTOR, "#hondaradio")

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
        bmw_check = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "#bmwcheck")
        benz_check = self.driver.find_element(By.CSS_SELECTOR, "#benzcheck")
        honda_check = self.driver.find_element(By.CSS_SELECTOR, "#hondacheck")

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
        bmw_check = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "#bmwcheck")
        benz_check = self.driver.find_element(By.CSS_SELECTOR, "#benzcheck")
        honda_check = self.driver.find_element(By.CSS_SELECTOR, "#hondacheck")

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
        button = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "#openwindow")
        button.click()

        original_window = self.driver.current_window_handle

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                search_form = self.get_wait.wait_for_element(By.CSS_SELECTOR, '#search')
                assert search_form
                break
        self.driver.close()
        self.driver.switch_to.window(original_window)


class TestForSwitchTab:

    def test_is_new_tab_opened(self):
        button = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "#opentab")
        button.click()
        original_window = self.driver.current_window_handle

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                search_form = self.get_wait.wait_for_element(By.CSS_SELECTOR, '#search')
                assert search_form
                break
        self.driver.close()
        self.driver.switch_to.window(original_window)


class TestForDropDown:
    def test_dropdown(self):
        cars = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'select[id="carselect"]')
        cars_select = Select(cars)

        cars_select.select_by_index(0)

        cars_select.select_by_index(1)

        cars_select.select_by_index(2)

        assert cars_select.first_selected_option.text == "Honda"


class TestForAutoSuggestExample():

    def test_is_input_text_is_saved(self):
        input_field = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "input[id='autosuggest']")

        input_field.click()
        input_field.send_keys('search')

        assert input_field.get_attribute('value') == 'search'


class TestForDisableEnabledField():

    def test_disabled(self):
        disabled_input = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="enabled-example-input"]')
        disable_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="disabled-button"]')

        assert disabled_input.is_enabled()

        disabled_input.send_keys('enable')
        disable_button.click()

        assert not disabled_input.is_enabled()

        enable_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="enabled-button"]')
        enable_button.click()

        assert disabled_input.is_enabled()

        assert disabled_input.get_attribute('value') == 'enable'


class TestForHiddenElement:

    def is_element_hidden(self):
        show_button = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, 'input[id="show-textbox"]')
        hide_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="hide-textbox"]')
        input = self.driver.find_element(By.CSS_SELECTOR, 'input[id="displayed-text"]')

        assert input.is_displayed()

        hide_button.click()
        assert not input.is_displayed()

        show_button.click()
        assert input.is_displayed()


class TestForAlert:

    def test_alert(self):
        name_1 = 'A'
        input = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="name"]')
        alert_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="alertbtn"]')
        confirm_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="confirmbtn"]')
        input.send_keys(name_1)
        alert_button.click()

        alert = self.driver.switch_to.alert

        assert alert.text == f'Hello {name_1}, share this practice page and share your knowledge'
        alert.accept()

        input.send_keys(name_1)
        confirm_button.click()
        confirm = self.driver.switch_to.alert

        assert confirm.text == f'Hello {name_1}, Are you sure you want to confirm?'
        confirm.dismiss()


class TestsForHover:

    def test_hover_elements(self):
        mouse_hover = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'button[id="mousehover"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", mouse_hover)

        actions = ActionChains(self.driver)
        actions.move_to_element(mouse_hover).perform()

        self.driver.find_element(By.CSS_SELECTOR, 'div[class="mouse-hover-content"] > a:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="mouse-hover-content"] > a:nth-child(2)').click()
