from pages.chapter1.prepositions.Prepositions_of_time import PrepositionsOfTimePage


class TestPrepositionsOfTimePage:
    def test_check_main_page(self, driver):
        main_page = PrepositionsOfTimePage(driver, 'https://english.areso.pro/lesson.html?lesson=prepositions_of_time')
        main_page.open()
        amount_of_cards = main_page.get_amount_of_cards()
        print(amount_of_cards)
        for i in range(amount_of_cards):
            current_card_number = main_page.get_current_card_number()
            print(f'\nCard number {current_card_number}/{amount_of_cards}')
            main_page.get_question_text()
            button_value, result = main_page.check_radio_buttons()
            correct_or_wrong = main_page.check_answer()
            correct_answer = main_page.check_correct_answer()
            assert result is True, 'Clicked button is not selected'
            try:
                assert button_value == correct_answer and correct_or_wrong == 'CORRECT'
            except Exception as ex:
                print(ex, '#'*10, '\nWrong answer!\n','#'*10)
            main_page.click_next_card()




