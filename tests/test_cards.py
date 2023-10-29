import allure
import pytest
from pages.chapter1.prepositions.Prepositions import PrepositionsPages


@allure.feature('Test Prepositions OfT Time Page.')
class TestPrepositions_1_1:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_of_time'

    @allure.title('test_check_main_page')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)
        
    
    @allure.title('test_check_questions_no_repeated')
    @pytest.mark.xfail
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('test_args_is_not_presence')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('In/on time, at/in the end/beginning.')
class TestPrepositions_1_3:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_in_on_time_at_in_the_end'

    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)
        
    @pytest.mark.xfail
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('To/at/in/into.')
class TestPrepositions_1_4:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_to_at_in_into'

    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)
        
    @pytest.mark.xfail
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)
