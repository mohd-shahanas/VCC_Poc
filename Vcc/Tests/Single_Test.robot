*** Settings ***
Resource    ../Keywords/Setup_Keywords.txt

Suite Setup    Vcc Suite Setup


Test Setup    Vcc Test Setup
Test Teardown    Run Keyword If Test Failed    Refresh Home Page

*** Test Cases ***

Test_15 Menu - Export Map Image
    [Documentation]    Validating Export Map Image Feature
    Enable Alerts
    Disable All Assets
    Expand Assets
    Activate Buildings Feed
    Activate Travel Feed
    Click Menu
    Click Tools Tab    Export Map Image
    Sleep    20
    Click Download
    Sleep    20
    Validate File Exists    VCC Map View.jpg
