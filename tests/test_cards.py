import os

import allure
import pytest
from pages.chapter1.prepositions.Prepositions import PrepositionsPages


@allure.suite('Chapter 1')
class TestChapter1:
    @allure.sub_suite('1.1. Test Prepositions Of Time Page.')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_of_time')
    class TestPrepositions_1_1:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_of_time'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            allure.dynamic.parameter("work-dir", os.getcwd(), excluded=True)
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @pytest.mark.xfail
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)


    @allure.sub_suite('1.2. Test Put the correct preposition!')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_of_places')
    class TestPrepositions_1_2:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_of_places'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            allure.dynamic.parameter("work-dir", os.getcwd(), excluded=True)
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @pytest.mark.xfail
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)

    @allure.sub_suite('1.3. In/on time, at/in the end/beginning.')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_in_on_time_at_in_the_end')
    class TestPrepositions_1_3:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_in_on_time_at_in_the_end'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated.'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)

    @allure.sub_suite('1.4. To/at/in/into.')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_to_at_in_into')
    class TestPrepositions_1_4:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_to_at_in_into'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)


    @allure.sub_suite('1.5. On/in/at (other uses).')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_on_in_at')
    class TestPrepositions_1_5:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_on_in_at'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)

    @allure.sub_suite('1.6. Usage of "by" preposition.')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_by')
    class TestPrepositions_1_6:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_by'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        @allure.title('Check questions no repeated.')
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)

    @allure.sub_suite('1.7. Prepositions with nouns.')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_with_nouns')
    class TestPrepositions_1_7:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_nouns'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)

    @allure.sub_suite('1.8. Prepositions with adjectives.')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_with_adjectives')
    class TestPrepositions_1_8:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_adjectives'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)

    @allure.sub_suite('1.9. Prepositions with adjectives 2.')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_with_adjectives2')
    class TestPrepositions_1_9:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_adjectives2'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)

    @allure.sub_suite('1.10. Prepositions with verbs.')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs')
    class TestPrepositions_1_10:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            (main_page.check_args_is_not_presence(main_page))

    @allure.sub_suite('1.11. Prepositions with verbs (p2).')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs2')
    class TestPrepositions_1_11:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs2'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)

    @allure.sub_suite('1.12. Prepositions with verbs (p3).')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs3')
    class TestPrepositions_1_12:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs3'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)

    @allure.sub_suite('1.13. Prepositions with verbs (p4).')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs4')
    class TestPrepositions_1_13:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs4'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)

    @allure.sub_suite('1.14. Prepositions with verbs (p5).')
    @allure.link('https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs5')
    class TestPrepositions_1_14:
        url = 'https://english.areso.pro/lesson.html?lesson=prepositions_with_verbs5'

        @allure.title('test_check_main_options')
        @allure.description('Check main page options.')
        @allure.severity('NORMAL')
        @allure.id(1)
        def test_check_main_options(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_main_options(main_page)

        # @pytest.mark.xfail
        @allure.title('test_check_questions_no_repeated')
        @allure.description('Check questions no repeated.')
        @allure.severity('NORMAL')
        @allure.id(2)
        def test_check_questions_no_repeated(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            data1, data2 = main_page.check_questions_no_repeated(main_page)
            assert data1 == data2, 'Question is repeated'

        @allure.title('test_args_is_not_presence')
        @allure.description('Check args is not presence.')
        @allure.severity('NORMAL')
        @allure.id(3)
        def test_args_is_not_presence(self, driver):
            main_page = PrepositionsPages(driver, self.url)
            main_page.open()
            main_page.check_args_is_not_presence(main_page)
