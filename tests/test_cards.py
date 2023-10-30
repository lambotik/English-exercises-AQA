import allure
import pytest
from pages.chapter1.prepositions.Prepositions import PrepositionsPages


@allure.feature('Test Prepositions OfT Time Page.')
class TestPrepositions_1_1:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_of_time'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    @allure.title('Check questions no repeated.')
    @pytest.mark.xfail
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('In/on time, at/in the end/beginning.')
class TestPrepositions_1_3:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_in_on_time_at_in_the_end'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated.'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('To/at/in/into.')
class TestPrepositions_1_4:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_to_at_in_into'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('Usage of "by" preposition.')
class TestPrepositions_1_6:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_by'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('Prepositions with nouns.')
class TestPrepositions_1_7:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_nouns'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('Prepositions with adjectives.')
class TestPrepositions_1_8:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_adjectives'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('Prepositions with adjectives 2.')
class TestPrepositions_1_9:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_adjectives2'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('Prepositions with verbs.')
class TestPrepositions_1_10:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        (main_page.check_args_is_not_presence(main_page))


@allure.feature('Prepositions with verbs (p2).')
class TestPrepositions_1_11:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs2'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('Prepositions with verbs (p3).')
class TestPrepositions_1_12:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs3'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('Prepositions with verbs (p4).')
class TestPrepositions_1_13:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs4'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)


@allure.feature('Prepositions with verbs (p5).')
class TestPrepositions_1_14:
    url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs5'

    @allure.title('Check main page options.')
    def test_check_main_options(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_main_options(main_page)

    # @pytest.mark.xfail
    @allure.title('Check questions no repeated.')
    def test_check_questions_no_repeated(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        data1, data2 = main_page.check_questions_no_repeated(main_page)
        assert data1 == data2, 'Question is repeated'

    @allure.title('Check args is not presence.')
    def test_args_is_not_presence(self, driver):
        main_page = PrepositionsPages(driver, self.url)
        main_page.open()
        main_page.check_args_is_not_presence(main_page)
