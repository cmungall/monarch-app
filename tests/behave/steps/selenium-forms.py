####
#### Steps for operating on the various forms and their results.
####

from behave import *

###
### radio button click
###

@given('I click the "{id}" radio button')
def step_impl(context, id):
    webelt = context.browser.find_element_by_id(id)
    webelt.click()

###
### Submission.
###

## Submit analyze phenotype.
@when('I submit analyze phenotype')
def step_impl(context):
    webelt = context.browser.find_element_by_id('analyze-submit')
    webelt.click()

## Submit navbar search.
@given('I submit navbar search')
def step_impl(context):
    #print(context.browser.title)
    webelt = context.browser.find_element_by_id('search_form')
    webelt.submit()

###
### Example for input for a possible text area form.
###

@given('I input "{text}" into the textarea "{eid}"')
def step_impl(context, text, eid):
    webelt = context.browser.find_element_by_id(eid)
    webelt.send_keys(text)
    
@given('I input the following text into the textarea "{eid}"')
def step_impl(context, eid):
    input_box_text = context.text
    webelt = context.browser.find_element_by_id(eid)
    webelt.send_keys(input_box_text)

@when('I submit the form by clicking XPath "{xpath}"')
def step_impl(context, xpath):
    ## xpath like "/html/body/div[2]/div[4]/div/div/form/div[2]/button"
    webelt = context.browser.find_element_by_xpath(xpath)
    webelt.click()
