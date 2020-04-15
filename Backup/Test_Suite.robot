*** Settings ***
Resource    ../Keywords/Setup_Keywords.txt

Suite Setup    Vcc Suite Setup
Test Setup    Vcc Test Setup


*** Test Cases ***
Test_1 Right Panel Navigations
    [Documentation]    Validating operations on right panel

    Click Assets
    Click Risk Events
    Click Context
    Click Alerts

Test_2 Bottom Panel Navigations
    [Documentation]    Validating operations on bottom panel

    Select Items Panel
    Select Feeds Panel
    Select Timeline Panel
    Deselect Feeds Panel
    Deselect Feeds Panel
    Deselect Timeline Panel
    Deselect Items Panel

Test_3 Edit Building Item
    [Documentation]    Validating Edit property of Building items

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

Test_4 Alert Count Validation
    [Documentation]    Validating alert count

    Click Alerts
    Sleep    20
    ${visible_cnt}=    GET ALERT VISIBLE COUNT
    ${total_cnt}=    GET ALERT TOTAL COUNT
    Display Visible Alerts

