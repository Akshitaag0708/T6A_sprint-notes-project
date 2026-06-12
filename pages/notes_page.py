from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class NotesPage(BasePage):

    ADD_NOTE = (By.XPATH,"//button[.='+ Add Note']")

    CATEGORY = (By.ID,"category")

    TITLE = (By.ID,"title")

    DESCRIPTION = (By.ID,"description")

    SAVE_BTN = (By.XPATH,"(//button[@type='submit'])[2]")

    CREATED_NOTE_TITLE = (By.XPATH,"(//div[@class='card']//div[2])[1]")

    CREATED_NOTE_DESCRIPTION = (By.XPATH,"(//div[@class='card-body d-flex flex-column']//p[1])[1]")

    EDIT_BTN = (By.XPATH,"(//button[.='Edit'])[1]")

    EDIT_CATEGORY = (By.ID,"category")

    EDIT_SAVE_BTN = (By.XPATH,"//button[.='Save']")

    DELETE_BTN = (By.XPATH,"(//button[@class='btn btn-outline-danger'])[2]")

    DELETE_CONFIRM_BTN = (By.XPATH,"//button[@class='btn btn-danger']")

    EDIT_TITLE = (By.XPATH,"//input[@id='title']")

    EDIT_DESCRIPTION = (By.XPATH , "//textarea[@id='description']")

    def create_note(self,category,title,description):

        self.scroll_by_offset()
        self.click(self.ADD_NOTE)
        dropdown = self.wait.until(lambda d: d.find_element(*self.CATEGORY))
        Select(dropdown).select_by_visible_text(category)
        self.type(self.TITLE, title)
        self.type(self.DESCRIPTION, description)
        self.click(self.SAVE_BTN)


        sleep(4)

        # self.wait.until(
        #     lambda d: title in [
        #         t.text for t in d.find_elements(*self.ALL_NOTE_TITLES)
        #     ]
        # )

    def get_created_note_title(self):
        return self.get_text(self.CREATED_NOTE_TITLE)


    def get_created_note_description(self):
        return self.get_text(self.CREATED_NOTE_DESCRIPTION)

    ALL_NOTE_TITLES = (By.XPATH,"//div[@class='card-header fw-bold text-truncate']")

    def refresh_page(self):
        self.driver.refresh()

    def get_all_note_titles(self):

        elements = self.driver.find_elements(*self.ALL_NOTE_TITLES)

        return [element.text for element in elements]

    def edit_note(self,category,title,description):

        self.scroll_by_offset()
        edit_btn = self.wait.until(EC.visibility_of_element_located(self.EDIT_BTN))
        self.driver.execute_script("arguments[0].click();",edit_btn)

        dropdown = self.wait.until(lambda d: d.find_element(*self.EDIT_CATEGORY))
        Select(dropdown).select_by_visible_text(category)

        title_field = self.wait.until(EC.visibility_of_element_located(self.EDIT_TITLE))

        title_field.clear()
        title_field.send_keys(title)

        description_field = self.wait.until(EC.visibility_of_element_located(self.EDIT_DESCRIPTION))

        description_field.clear()
        description_field.send_keys(description)

        self.click(self.EDIT_SAVE_BTN)

    def delete_note(self):

        self.scroll_by_offset()

        delete_btn = self.wait.until(EC.element_to_be_clickable(self.DELETE_BTN))

        self.driver.execute_script("arguments[0].click();",delete_btn)

        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.DELETE_CONFIRM_BTN))

        confirm_btn.click()

    # def debug_all_titles(self):
    #     titles = self.driver.find_elements(
    #         By.XPATH,
    #         "//div[@class='card-header fw-bold text-truncate']"
    #     )
    #
    #     for i, title in enumerate(titles, start=1):
    #         print(f"{i} -> {title.text}")