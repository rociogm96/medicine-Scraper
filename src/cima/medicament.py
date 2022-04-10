import datetime
import re
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


class WebMedicament:
    """
    Class used to obtain the website of a specific medicament.
    """

    def __init__(self, registration_n):
        self.registration_n = registration_n
        self.base_url = "https://cima.aemps.es/cima/publico/detalle.html?nregistro="
        self.product_url = self.base_url + str(self.registration_n)
        self.bs_medicament = self.get_bs_medicament()

    def get_url(self):
        return self.product_url

    def get_bs_medicament(self):
        """
        Returns a BeautifulSoup Object where the medicament's page
        is contained.

        The parameters for the search are configured in this method.
        """

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.set_window_size(
            1920, 1080
        )  # Windows size must be fixed because of the responsive webpage design.
        browser.get(self.product_url)

        # Wait till tag with id "nregistroID" appears.
        WebDriverWait(browser, 30).until(ec.presence_of_element_located((By.ID, "nregistroId")))

        page = browser.page_source
        browser.close()
        return BeautifulSoup(page, "html.parser")


class Medicament:
    """
    This class represents the medicine or sanitary product
     that has been obtained by their registration number.
    """

    def __init__(self, registration_number):
        self.soup_medicament = WebMedicament(registration_number).bs_medicament
        self.registration_number = int(registration_number)
        self.name = self.set_name()
        self.company = self.set_company()
        self.authorization_date = self.set_authorization_date()
        self.commercialized = self.set_commercialized()
        self.pharmaceutical_dose_form = self.set_pharmaceutical_dose_form()
        self.routes_administration = self.set_routes_administration()
        self.strength = self.set_strength()
        self.active_ingredients = self.set_active_ingredients()
        self.excipients = self.set_excipients()
        self.characteristics = self.set_characteristics()
        self.atc_codes = self.set_atc_codes()
        self.images_url = self.set_image_url()

    def set_name(self):
        """
        Set the value of the name attribute
        with the name of the medicament.
        """
        id_value = "nombreMedicamento"
        return self.soup_medicament.find(id=id_value).text

    def set_company(self):
        """
        Set the value of the company attribute
        with the name of the company that
        produces the medicament.
        """
        id_value = "nombrelab"
        return self.soup_medicament.find(id=id_value).text

    def set_authorization_date(self):
        """
        Set the authorization date attribute with
        a datetime object which represents the
        authorization date of the medicament.
        """
        id_value = "estadoXS"
        string = self.soup_medicament.find(id=id_value).findChild().text
        return datetime.datetime.strptime(string, "( %d/%m/%Y )").date()

    def set_commercialized(self):
        """
        Set the value of the attribute commercialized
        with a boolean true or false, depending on if the product
        is currently being sold or not.
        """
        id_value = "estadocomerc"
        string = self.soup_medicament.find(id=id_value).text
        # Check if the medicament is currently commercialized.
        if string == "Comercializado":
            return True

        return False

    def set_pharmaceutical_dose_form(self):
        """
        Set the value of the attribute pharmaceutical_
        dose_form with a list of strings that contains
        all the forms of that medicament.
        """
        id_value = "formas"
        string = self.soup_medicament.find(id=id_value)

        return [i.text for i in string.findChild()]

    def set_routes_administration(self):
        """
        Set the value of the routes_administration
        with a list of strings that contains all the
        routes of administration for that medicament.
        """
        id_value = "viasadministracion"
        string = self.soup_medicament.find(id=id_value)

        return [i.text for i in string.findChild()]

    def set_strength(self):
        """
        Set the value of the strength with a list of
        floats that contains the different strengthens
        for that medicament.

        All is expressed in milligrams.
        """
        id_value = "dosis"
        string = self.soup_medicament.find(id=id_value)
        list_strengthens = []
        for i in string.findChild():
            list_strengthens.append(re.findall(r"\d+(?:\.\d+)?", i.text))

        # Flats the possible multilevel list and convert the values from str to float
        return [float(item) for sublist in list_strengthens for item in sublist]

    def set_active_ingredients(self):
        """
        Set the value of the active_ingredients with a list of
        strings that contains the different actives for that
        medicament.
        """
        id_value = "pactivosList"
        string = self.soup_medicament.find(id=id_value)

        return [i.text for i in string.findChild()]

    def set_excipients(self):
        """
        Set the value of the excipients with a list of
        strings that contains the different excipients
        for that medicament.
        """
        id_value = "excipientesList"
        string = self.soup_medicament.find(id=id_value)

        return [i.text for i in string.findChild()]

    def set_characteristics(self):
        """
        Set the value of the characteristics with a list of
        strings that contains the different characteristics
        for that medicament.
        """
        id_value = "caracteristicasList"
        string = self.soup_medicament.find(id=id_value)

        return [i.text for i in string.findChild()]

    def set_atc_codes(self):
        """
        Set the value of the atc_codes with a list of
        strings that contains the different atc_codes
        for that medicament.
        """
        id_value = "atcList"
        string = self.soup_medicament.find(id=id_value)

        return [i.text for i in string.findChild()]

    def set_image_url(self):
        """
        Set the list with the values of the urls that
        lead to the medicament's images if they exist
        """
        id_value = "boxImages"
        string = self.soup_medicament.find(id=id_value)

        urls = []

        for img in string.find_all("img"):
            urls.append(img["src"])

        return urls

    @property
    def get_all_info(self):
        """This method returns all the information for
        a medicament in a dictionary.
        """
        return {
            "registration_number": self.registration_number,
            "name": self.name,
            "company": self.company,
            "authorization_date": self.authorization_date,
            "commercialized": self.commercialized,
            "pharmaceutical_dose_form": self.pharmaceutical_dose_form,
            "routes_administration": self.routes_administration,
            "strength": self.strength,
            "active_ingredients": self.active_ingredients,
            "excipients": self.excipients,
            "characteristics": self.characteristics,
            "atc_codes": self.atc_codes,
            "images_url": self.images_url,
        }
