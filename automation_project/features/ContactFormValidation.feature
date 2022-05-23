#lang = en-GB

@contact-form-validation @priority.critical
Feature: Contact Form User Input Validation

    This feature aims to test the validation functionality if the contact form.

    @smoke
    Scenario: filled-out form can be submitted sucessfully
    Given I go to the contact form
    And I fill it out completely 
    When I submit the form 
    Then I should see a confirmation page

    @smoke @runner.continue_after_failed_step
    Scenario: cannot submit form without filling out the Subject field
    Given I go to the contact form
    And I fill out all but the Subject field
    When I submit the form 
    Then I should see an error message asking me to fill out the Subject field

    @smoke @runner.continue_after_failed_step
    Scenario: cannot submit form without filling out the Email field
    Given I go to the contact form
    And I fill out all but the Email field
    When I submit the form 
    Then I should see an error message asking me to correctly fill out the Email field

    @smoke @runner.continue_after_failed_step
    Scenario: cannot submit form without filling out the Order field
    Given I go to the contact form
    And I fill out all but the Order field
    When I submit the form 
    Then I should see an error message asking me to fill out the Order field

    @smoke @runner.continue_after_failed_step
    Scenario: cannot submit form without filling out the File field
    Given I go to the contact form
    And I fill out all but the File field
    When I submit the form 
    Then I should see an error message asking me to fill out the File field

    @smoke @runner.continue_after_failed_step
    Scenario: cannot submit form without filling out the Message field
    Given I go to the contact form
    And I fill out all but the Message field
    When I submit the form 
    Then I should see an error message asking me to fill out the Message field

    @smoke @runner.continue_after_failed_step
    Scenario: emails must be in the form email@domain.xxx
    Given I go to the contact form
    And I fill out the email field with an invalid email
    When I submit the form 
    Then I should see an error message asking me to correctly fill out the Email field