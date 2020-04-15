*** Settings ***
Library    ../Library/VccActions.py

Suite Setup    Vcc Suite Setup


*** Keywords ***
Vcc Suite Setup
    ${driver}=    User Login
    Set Suite Variable    ${driver}

*** Test Cases ***

Test_1 Right Panel Navigations
    [Documentation]    Validating operations on right panel
    Initialize Driver    ${driver}
    Click Assets
    Click Risk Events
    Click Context
    Click Alerts

Test_2 Bottom Panel Navigations
    [Documentation]    Validating operations on bottom panel
    Initialize Driver    ${driver}
    Select Items Panel
    Select Feeds Panel
    Select Timeline Panel
    Deselect Feeds Panel
    Deselect Feeds Panel
    Deselect Timeline Panel
    Deselect Items Panel

Test_3 Edit Building Item
    [Documentation]    Validating Edit property of Building items
    Initialize Driver    ${driver}
    Select Buildings
    Select Items Panel
    &{building_details}=    Get Building Item Details    1
    Log    ${building_details["Contact"]}
    Edit Building Contact Details
    Deselect Items Panel
    Select Buildings
    Select Buildings
    Select Items Panel
    &{building_details}=    Get Building Item Details    1
    Log    ${building_details["Contact"]}