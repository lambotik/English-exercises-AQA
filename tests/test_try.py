from pprint import pprint

import allure

from pages.chapter1.prepositions.Prepositions import PrepositionsPages


@allure.feature('Test Prepositions OfT Time Page.')
class TestPrepositions_1_1:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_of_time'

    @allure.title('test_check_main_page')
    def test_check_main_page(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        amount_of_cards = main_page.get_amount_of_cards()
        for i in range(amount_of_cards):
            current_card_number = main_page.get_current_card_number()
            with allure.step(f'\n{current_card_number}. Check card.'):
                question = main_page.get_question_text()
            with allure.step(f'Question: {question}'):
                button_value, result = main_page.check_radio_buttons()
            with allure.step(f'Customer selected: {button_value}'):
                pass
            with allure.step(f'\n\nValue of button is: {result}'):
                pass
                correct_or_wrong = main_page.check_answer()
                correct_answer = main_page.check_correct_answer()
            with allure.step(f'Should be: {correct_answer}'):
                print(f'Should be: {correct_answer}')
            with allure.step(f'Result should be:{correct_answer}'):
                assert result is True, 'Clicked button is not selected'
                try:
                    assert button_value == correct_answer and correct_or_wrong == 'CORRECT'
                    print('#' * 10, "It's right answer.", '#' * 10)
                    print('\n')
                except Exception as ex:
                    print('\n', ex, '\n', '#' * 10, 'Wrong answer!', '#' * 10, '\n')
                main_page.click_next_card()
            with allure.step('*' * 90):
                pass

    @allure.title('test_check_questions_no_repeated')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        amount_of_cards = main_page.get_amount_of_cards()
        data1 = {}
        data2 = {}
        for _ in range(amount_of_cards):
            current_card_number = main_page.get_current_card_number()
            question = main_page.get_question_text()
            data1[current_card_number] = question
            if question not in list(data2.values()):
                data2[current_card_number] = question
            main_page.click_next_card()
        pprint(data1)
        pprint(data2)
        assert data1 == data2, 'Question is repeated'

    @allure.title('test_args_is_not_presence')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        amount_of_cards = main_page.get_amount_of_cards()
        data = {}
        for _ in range(amount_of_cards):
            current_card_number = main_page.get_current_card_number()
            question = main_page.get_question_text()
            data[current_card_number] = question
            assert 'args' not in question, 'Args is presence'
            main_page.click_next_card()


@allure.feature('In/on time, at/in the end/beginning.')
class TestPrepositions_1_3:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_in_on_time_at_in_the_end'

    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        amount_of_cards = main_page.get_amount_of_cards()
        for i in range(amount_of_cards):
            current_card_number = main_page.get_current_card_number()
            with allure.step(f'\n{current_card_number}. Check card.'):
                question = main_page.get_question_text()
            with allure.step(f'Question: {question}'):
                button_value, result = main_page.check_radio_buttons()
            with allure.step(f'Customer selected: {button_value}'):
                pass
            with allure.step(f'\n\nValue of button is: {result}'):
                pass
                correct_or_wrong = main_page.check_answer()
                correct_answer = main_page.check_correct_answer()
            with allure.step(f'Should be: {correct_answer}'):
                print(f'Should be: {correct_answer}')
            with allure.step(f'Result should be:{correct_answer}'):
                assert result is True, 'Clicked button is not selected'
                try:
                    assert button_value == correct_answer and correct_or_wrong == 'CORRECT'
                    print('#' * 10, "It's right answer.", '#' * 10)
                    print('\n')
                except Exception as ex:
                    print('\n', ex, '\n', '#' * 10, 'Wrong answer!', '#' * 10, '\n')
                main_page.click_next_card()
            with allure.step('*' * 90):
                pass

    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        amount_of_cards = main_page.get_amount_of_cards()
        data1 = {}
        data2 = {}
        for _ in range(amount_of_cards):
            current_card_number = main_page.get_current_card_number()
            question = main_page.get_question_text()
            data1[current_card_number] = question
            if question not in list(data2.values()):
                data2[current_card_number] = question
            main_page.click_next_card()
        pprint(data1)
        pprint(data2)
        assert data1 == data2, 'Question is repeated'

    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        amount_of_cards = main_page.get_amount_of_cards()
        data = {}
        for _ in range(amount_of_cards):
            current_card_number = main_page.get_current_card_number()
            question = main_page.get_question_text()
            data[current_card_number] = question
            assert 'args' not in question, 'Args is presence'
            main_page.click_next_card()


@allure.feature('To/at/in/into.')
class TestPrepositions_1_4:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_to_at_in_into'

    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        amount_of_cards = main_page.get_amount_of_cards()
        for i in range(amount_of_cards):
            current_card_number = main_page.get_current_card_number()
            with allure.step(f'\n{current_card_number}. Check card.'):
                question = main_page.get_question_text()
            with allure.step(f'Question: {question}'):
                button_value, result = main_page.check_radio_buttons()
            with allure.step(f'Customer selected: {button_value}'):
                pass
            with allure.step(f'\n\nValue of button is: {result}'):
                pass
                correct_or_wrong = main_page.check_answer()
                correct_answer = main_page.check_correct_answer()
            with allure.step(f'Should be: {correct_answer}'):
                print(f'Should be: {correct_answer}')
            with allure.step(f'Result should be:{correct_answer}'):
                assert result is True, 'Clicked button is not selected'
                try:
                    assert button_value == correct_answer and correct_or_wrong == 'CORRECT'
                    print('#' * 10, "It's right answer.", '#' * 10)
                    print('\n')
                except Exception as ex:
                    print('\n', ex, '\n', '#' * 10, 'Wrong answer!', '#' * 10, '\n')
                main_page.click_next_card()
            with allure.step('*' * 90):
                pass

    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        amount_of_cards = main_page.get_amount_of_cards()
        data1 = {}
        data2 = {}
        for _ in range(amount_of_cards):
            current_card_number = main_page.get_current_card_number()
            question = main_page.get_question_text()
            data1[current_card_number] = question
            if question not in list(data2.values()):
                data2[current_card_number] = question
            main_page.click_next_card()
        pprint(data1)
        pprint(data2)
        assert data1 == data2, 'Question is repeated'

    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        amount_of_cards = main_page.get_amount_of_cards()
        data = {}
        for _ in range(amount_of_cards):
            current_card_number = main_page.get_current_card_number()
            question = main_page.get_question_text()
            data[current_card_number] = question
            assert 'args' not in question, 'Args is presence'
            main_page.click_next_card()
