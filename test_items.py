link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_should_see_add_to_busket_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("#add_to_basket_form")
    assert button, f"There is no button {button}"