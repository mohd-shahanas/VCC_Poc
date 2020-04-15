*** Settings ***
Resource    ../Keywords/Setup_Keywords.txt

Suite Setup    Vcc Suite Setup
Test Setup    Vcc Test Setup

*** Test Cases ***

Test_13 Excel Report from Menu
    [Documentation]    Validating Excel Report from Menu
    Click Menu
    Sleep    20
    