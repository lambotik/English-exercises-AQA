import random

import allure
from selenium.webdriver.common.by import By

from locators.main_page_locators import PrepositionsLocators
from pages.base_page import BasePage


class PrepositionsPages(BasePage):
    locators = PrepositionsLocators()

    def get_amount_of_cards(self):
        amount = int(self.element_is_presence(self.locators.AMOUNT_OF_CARDS).text)
        print('Amount cards:', amount)
        return amount

    def get_current_card_number(self):
        curd_number = int(self.element_is_presence(self.locators.CURRENT_CARD_NUMBER).text)
        return curd_number

    def get_question_text(self):
        question_text = self.element_is_presence(self.locators.QUESTION).text
        return question_text

    def check_radio_buttons(self):
        random_index = random.randint(0, len(self.elements_are_presence(
            (By.XPATH, '//div[@id="answer_radiobutton_div"] /input')))-1)
        selected_button = self.elements_are_presence(self.locators.LIST_OF_RADIO_BUTTONS)[random_index]
        selected_button.click()
        with allure.step(f"Customer selected: {selected_button.get_attribute('value')}."):
            all_options = [value.get_attribute('value') for value
                           in self.elements_are_presence(self.locators.LIST_OF_RADIO_BUTTONS)]
            print('All options:', all_options)
            selected_button_value = selected_button.get_attribute('value')
            print('Selected option:', selected_button_value)
            """Or we can use after click selected_button.is_selected()"""
            return selected_button_value, self.check_selected_radio_button(random_index)

    def check_answer(self):
        self.element_is_presence_and_clickable(self.locators.CHECK_ANSWER_BUTTON).click()
        answer = self.element_is_presence(self.locators.CORRECT_OR_WRONG).text
        print('Correct or wrong answer:', answer)
        return answer

    def check_correct_answer(self):
        show_answer = self.element_is_presence_and_clickable(self.locators.SHOW_ANSWER_BUTTON)
        show_answer.click()
        correct_answer = self.element_is_presence(self.locators.CORRECT_ANSWER_TEXT).text
        print(f'Correct answer: {correct_answer}')
        return correct_answer

    def click_next_card(self):
        button_next_card = self.element_is_presence_and_clickable(self.locators.NEXT_CARD_BUTTON)
        button_next_card.click()
