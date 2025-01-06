import os

from selene import browser, be, have, by
import time


def test_ui_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').click().type("Test")
    browser.element('#lastName').click().type("User")
    browser.element('#userEmail').click().type("testemail@yandex.ru")
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').click().type("4456723492")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('May')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1989')).click()
    browser.element(by.text("8")).click()
    browser.element("#subjectsInput").type('Biology').press_enter().type("Chemistry").press_enter()
    browser.element('[for=hobbies-checkbox-2]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../test-pic/test-fox.jpg'))
    browser.element('#currentAddress').set('Navi Shin, 1566')
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()

    browser.element('#submit').click()

    browser.element(".modal-body").should(have.text("Test User"))
    browser.element(".modal-body").should(have.text("testemail@yandex.ru"))
    browser.element(".modal-body").should(have.text("Female"))
    browser.element(".modal-body").should(have.text("4456723492"))
    browser.element(".modal-body").should(have.text("08 May,1989"))
    browser.element(".modal-body").should(have.text("Biology, Chemistry"))
    browser.element(".modal-body").should(have.text("Reading"))
    browser.element(".modal-body").should(have.text("test-fox.jpg"))
    browser.element(".modal-body").should(have.text("Navi Shin, 1566"))
    browser.element(".modal-body").should(have.text("NCR Delhi"))

