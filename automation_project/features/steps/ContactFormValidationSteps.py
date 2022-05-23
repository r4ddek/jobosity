import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Define base URL
base_url = "http://automationpractice.com/"

# Define locators
contact_link_CSS_selector = '#contact-link'
success_msg_xpath = '//p[contains(@class, \'alert alert-success\')]'
subject_selector_xpath = '//select[contains(@class, \'form-control\')]'
email_field_xpath = '//input[contains(@class, \'form-control\') and @id=\'email\']'
order_field_xpath = '//input[contains(@class, \'form-control\') and @id=\'id_order\']'
file_field_xpath = '//input[contains(@class, \'form-control\') and @id=\'fileUpload\']'
message_field_xpath = '//textarea[contains(@class, \'form-control\') and @id=\'message\']'
send_button_xpath = '//button[contains(@class, \'button btn btn-default button-medium\')]'
err_msg_xpath = '//div[contains(@class, \'alert alert-danger\')]//*[contains(text(), '


@given(u'I go to the contact form')
def step_impl(context):
    context.browser.get(base_url)
    contact_link_button = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, contact_link_CSS_selector)))
    contact_link_button.click()


@given(u'I fill it out completely')
def step_impl(context):
    subject_selector = context.browser.find_element_by_xpath(
        subject_selector_xpath)
    subject_selector.click()
    subject_selector.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

    email_field = context.browser.find_element_by_xpath(email_field_xpath)
    email_field.send_keys('test@jobosity.com')

    order_field = context.browser.find_element_by_xpath(order_field_xpath)
    order_field.send_keys('1010101010')

    file_field = context.browser.find_element_by_xpath(file_field_xpath)
    path_parent = os.path.dirname(os.getcwd())
    # print(path_parent)
    file_field.send_keys(path_parent + '\\requirements.txt')

    message_field = context.browser.find_element_by_xpath(message_field_xpath)
    message_field.send_keys("This is a message.")


@when(u'I submit the form')
def step_impl(context):
    send_button = context.browser.find_element_by_xpath(send_button_xpath)
    send_button.click()


@then(u'I should see a confirmation page')
def step_impl(context):
    WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, success_msg_xpath)))


@given(u'I fill out all but the Subject field')
def step_iml(context):
    email_field = context.browser.find_element_by_xpath(email_field_xpath)
    email_field.send_keys('test@jobosity.com')

    order_field = context.browser.find_element_by_xpath(order_field_xpath)
    order_field.send_keys('1010101010')

    file_field = context.browser.find_element_by_xpath(file_field_xpath)
    path_parent = os.path.dirname(os.getcwd())
    file_field.send_keys(path_parent + '\\requirements.txt')

    message_field = context.browser.find_element_by_xpath(message_field_xpath)
    message_field.send_keys("This is a message.")


@then(u'I should see an error message asking me to fill out the Subject field')
def step_impl(context):
    err_msg = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, err_msg_xpath + '\'subject\')]')))
    err_msg.text == "Please select a subject from the list provided."


@given(u'I fill out all but the Email field')
def step_iml(context):
    subject_selector = context.browser.find_element_by_xpath(
        subject_selector_xpath)
    subject_selector.click()
    subject_selector.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

    order_field = context.browser.find_element_by_xpath(order_field_xpath)
    order_field.send_keys('1010101010')

    file_field = context.browser.find_element_by_xpath(file_field_xpath)
    path_parent = os.path.dirname(os.getcwd())
    file_field.send_keys(path_parent + '\\requirements.txt')

    message_field = context.browser.find_element_by_xpath(message_field_xpath)
    message_field.send_keys("This is a message.")


@then(u'I should see an error message asking me to correctly fill out the Email field')
def step_impl(context):
    err_msg = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, err_msg_xpath + '\'email\')]')))
    err_msg.text == "Invalid email address."

@given(u'I fill out all but the Order field')
def step_iml(context):
    subject_selector = context.browser.find_element_by_xpath(
        subject_selector_xpath)
    subject_selector.click()
    subject_selector.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

    email_field = context.browser.find_element_by_xpath(email_field_xpath)
    email_field.send_keys('test@jobosity.com')

    file_field = context.browser.find_element_by_xpath(file_field_xpath)
    path_parent = os.path.dirname(os.getcwd())
    file_field.send_keys(path_parent + '\\requirements.txt')

    message_field = context.browser.find_element_by_xpath(message_field_xpath)
    message_field.send_keys("This is a message.")


@then(u'I should see an error message asking me to fill out the Order field')
def step_impl(context):
    err_msg = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, err_msg_xpath + '\'order\')]')))
    err_msg.text == "Invalid order reference."

@given(u'I fill out all but the File field')
def step_iml(context):
    subject_selector = context.browser.find_element_by_xpath(
        subject_selector_xpath)
    subject_selector.click()
    subject_selector.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

    email_field = context.browser.find_element_by_xpath(email_field_xpath)
    email_field.send_keys('test@jobosity.com')

    order_field = context.browser.find_element_by_xpath(order_field_xpath)
    order_field.send_keys('1010101010')

    message_field = context.browser.find_element_by_xpath(message_field_xpath)
    message_field.send_keys("This is a message.")


@then(u'I should see an error message asking me to fill out the File field')
def step_impl(context):
    err_msg = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, err_msg_xpath + '\'file\')]')))
    err_msg.text == "Please attach a valid file."

@given(u'I fill out all but the Message field')
def step_iml(context):
    subject_selector = context.browser.find_element_by_xpath(
        subject_selector_xpath)
    subject_selector.click()
    subject_selector.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

    email_field = context.browser.find_element_by_xpath(email_field_xpath)
    email_field.send_keys('test@jobosity.com')

    order_field = context.browser.find_element_by_xpath(order_field_xpath)
    order_field.send_keys('1010101010')

    file_field = context.browser.find_element_by_xpath(file_field_xpath)
    path_parent = os.path.dirname(os.getcwd())
    file_field.send_keys(path_parent + '\\requirements.txt')


@then(u'I should see an error message asking me to fill out the Message field')
def step_impl(context):
    err_msg = WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, err_msg_xpath + '\'message\')]')))
    err_msg.text == "The message cannot be blank."

@given(u'I fill out the email field with an invalid email')
def step_impl(context):
    email_field = context.browser.find_element_by_xpath(email_field_xpath)
    email_field.send_keys('test.jobosity.com')