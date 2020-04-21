*** Settings ***
Resource    ../Keywords/Setup_Keywords.txt

Suite Setup    Vcc Suite Setup
Test Setup    Vcc Test Setup

*** Test Cases ***

Test_11 Menu - Scale Bar
    [Documentation]    Validating Deactivate and activate functionality of Scale Bar

    Click Menu
    ${scale_bar_enable_status}=    Is Preference Tab Selected    Scale Bar
    Should be True    ${scale_bar_enable_status} == True
    Deselect Preference Tab    Scale Bar
    Click Menu
    ${scale_bar_display}=    Get Scalebar Display Status
    Should be True    ${scale_bar_display} == False
    Click Menu
    Select Preference Tab    Scale Bar
    Click Menu
    ${scale_bar_display}=    Get Scalebar Display Status
    Should be True    ${scale_bar_display} == True
