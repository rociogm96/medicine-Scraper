class CimaWebConfigurator:
    """
    This class can configure the terms about the website where the searcher is implemented.
    If the website changes its structure, the fields of this class must change.
    """

    def __init__(self):
        # Default values date 06/04/2022
        self.url = "https://cima.aemps.es/cima/publico/home.html"
        self.tag_search_box = "inputbuscadorsimple"
        self.tag_search_button = "btnBuscarSimple"
        self.sleep_time_charge = 5
        self.search_by = "id"

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_tag_search_box(self):
        return self.tag_search_box

    def set_tag_search_box(self, tag_search_box):
        self.tag_search_box = tag_search_box

    def get_tag_search_button(self):
        return self.tag_search_button

    def set_tag_search_button(self, tag_search_button):
        self.tag_search_button = tag_search_button

    def get_sleep_time_charge(self):
        return self.sleep_time_charge

    def set_sleep_time_charge(self, sleep_time_charge):
        self.sleep_time_charge = sleep_time_charge

    def get_search_by(self):
        return self.search_by

    def set_search_by(self, search_by):
        self.search_by = search_by
