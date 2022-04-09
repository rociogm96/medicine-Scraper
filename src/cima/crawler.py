from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from src.cima import searcher


class Crawler:
    """
    This class represent the crawler of terms
    for a medicament through the cima web.

    It needs to be passed a string with the
    search string as parameter.
    """

    def __init__(self, terms):
        self._browser = self._get_results_page(terms)
        self.xpath_amount_registers = '//*[@id="numResultados"]'
        self.xpath_register = "//div/div[1]/div[1]/div[1]/div[1][@class='col-md-12 col-xs-12 list-group-item-text']"

    def get_xpath_amount_registers(self):
        return self.xpath_amount_registers

    def set_xpath_amount_registers(self, xpath_amount_registers):
        self.xpath_amount_registers = xpath_amount_registers

    def get_xpath_register(self):
        return self.xpath_register

    def set_xpath_register(self, xpath_register):
        self.xpath_register = xpath_register

    @staticmethod
    def _get_results_page(search_terms):
        """
        Uses the web navigator parameters established on web_config
        and returns an object type:
        class selenium.webdriver.edge.webdriver.WebDriver.

        This contains results page from the search made with cima,
        the medicine searcher from the Spanish Medicament Agency and
        Sanitary Products (Agencia Española del Medicamento y Productos
        Sanitarios AEMPS).
        """
        web_config = searcher.CimaWebConfigurator()

        # Get the parameters of the web configuration
        url = web_config.get_url()
        by_term = web_config.get_search_by()
        tag_search_box = web_config.get_tag_search_box()
        tag_search_button = web_config.get_tag_search_button()
        t = web_config.get_sleep_time_charge()

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.set_window_size(
            1920, 1080
        )  # Windows size must be fixed because of the responsive webpage design.
        browser.get(url)
        search_box = browser.find_element(by=by_term, value=tag_search_box)
        search_box.send_keys(search_terms)
        # Notice that by_term are the same for search_boz and button. This could be changed for future page versions.
        button = browser.find_element(by=by_term, value=tag_search_button)
        button.click()

        # Waiting for the search produces results
        sleep(t)

        # Created a webdriver Attribute
        return browser

    def get_amount_results(self):
        """
        This method gets the value of results from the top
        left indicator on the response webpage.

        That is faster than counting all the elements when
        getting the length from the list of reference numbers.
        """
        return int(
            self._browser.find_element(By.XPATH, self.xpath_amount_registers).text
        )

    def get_list_references(self):
        """
        A list of strings with the code of each medicament
        is returned.

        The method consults the reference numbers of each
        medicament, which are results from the search and
        collects them in a list of strings.
        """
        amount_results = self.get_amount_results()

        def get_registers():
            """
            Function got involved in the method get_list_reference.
            This function consults all the register numbers using
            the Xpath.

            This function cannot be called from outside
            """
            return self._browser.find_elements(By.XPATH, self.xpath_register)

        registers = get_registers()

        # Scroll is done until there are as reference numbers as the amount of results
        while len(registers) < amount_results:
            self._browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            sleep(2)
            registers = get_registers()

        registers_list = []

        for reg in registers:
            registers_list.append(reg.text.split(": ")[1])

        return registers_list

    def __del__(self):
        """
        When the object is deleted, the destructor closes the web navigator.
        """
        self._browser.close()
