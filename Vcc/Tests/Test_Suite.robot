*** Settings ***
Resource    ../Keywords/Setup_Keywords.txt

Suite Setup    Vcc Suite Setup
Test Setup    Vcc Test Setup

*** Test Cases ***

Test_13 Excel Report from Menu
    [Documentation]    Validating Excel Report from Menu


*** comment ***
Test_08 Menu - Create CheckList Template
    [Documentation]    Validating Create CheckList Template from Menu
    Click Menu
    Click Launch Apps Tab    Checklists
    Switch to New Window
    @{old_checklists}=    Get Item List
    Create New CheckList    title=UI Automation 01
    @{new_checklists}=    Get Item List
    Validate Created Item    ${old_checklists}    ${new_checklists}    UI Automation 01
    Switch to Default Window

Test_09 Menu - Create Note
    [Documentation]    Validating Create note from Menu
    Click Menu
    Click Launch Apps Tab    Notes
    Switch to New Window
    @{old_notes}=    Get Item List
    Create New Note    title=UI Automation 01
    @{new_notes}=    Get Item List
    Validate Created Item    ${old_notes}    ${new_notes}    UI Automation 01
    Switch to Default Window

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

Test_13 Excel Report from Menu
    [Documentation]    Validating Excel Report from Menu
    Enable Alerts
    Disable All Assets
    Disable All Risk Events
    Disable All Context
    Click Menu
    Click Tools Tab    Excel Report
    Sleep    20
    Click Download
    Sleep    20
    Validate File Exists    Visual Command Center Report.xlsx


Test_14 Menu - Create Saved View
    [Documentation]    Validating Create New Saved View from Menu
    Click Menu
    Click Tools Tab    Saved Views
    @{old_views}=    Get Saved Views
    Create New Saved View    Testing 01
    @{new_views}=    Get Saved Views
    Validate Created Item    ${old_views}    ${new_views}    Testing 01
    Close Saved View Tab

Test_15 Menu - Asset Map Export
    [Documentation]    Validating Asset Map Export Feature
    Enable Alerts
    Enable Buildings
    Enable Travel
    Click Menu
    Click Tools Tab    Export Map Image
    Sleep    20
    Click Download
    Sleep    20
    Validate File Exists    VCC Map View.jpg