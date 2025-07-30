import datetime



class Base():

    def __init__(self, driver):
        self.driver = driver



    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, print('Bad value word:', value_word, 'result:', result)
        print("Good value word:", value_word)

    """Method screenshot"""
    def get_screenshot(self, method):
        now_date = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot_'  + method + now_date + '.png'
        self.driver.save_screenshot('screen\\' + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method assert total cost"""
    def assert_total_cost(self, total_cost, result):
        print(total_cost, result)
        assert total_cost == result, print('Bad total cost:', total_cost, 'result:', result)
        print("Good value total cost:", total_cost)
