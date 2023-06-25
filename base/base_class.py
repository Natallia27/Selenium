import pytz
from datetime import datetime

class Base():

    def __init__(self, driver_g):
        self.driver_g = driver_g

    def get_current_url(self):
        """
        Method Get current url
        """
        get_url = self.driver_g.current_url
        print("Current url " + get_url)

    def get_assert_word(self, word, result):
        """
        Method Assert word
        """
        value_word = word.text
        assert value_word == result
        print('Good word')

    def get_screenshot(self):
        """
        Method Screenshot
        """

    # Устанавливаем временную зону для Варшавы
        timezone = pytz.timezone("Europe/Warsaw")

    # Получаем текущее время в Варшаве

        now_date = datetime.now(timezone).strftime(" Time in Warsaw %Y-%m-%d %H-%M")
        name_screenshot = 'screenshot' + now_date + '.png'

        self.driver_g.save_screenshot('C:\\Users\\natal\\PycharmProjects\\main_project\\screen\\' + name_screenshot)

    def get_assert_url(self, result):
        """
        Method Assert url
        """
        get_url = self.driver_g.current_url
        assert get_url == result
        print('Good url')