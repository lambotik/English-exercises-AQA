# import time
#
# from pages.base_page import BasePage
#
#
# class MainPage(BasePage):
#
#     def check_urls(self):
#         list_of_games = self.elements_are_presence(self.locators.LIST_OF_GAMES)
#         data = []
#         [data.append(i.get_attribute('href')) for i in list_of_games]
#         print(*data, sep='\n')
#         return data
#
#     def check_all_urls(self):
#         self.element_is_presence_and_clickable(self.locators.LOGO).click()








