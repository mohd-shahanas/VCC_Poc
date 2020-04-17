*** Settings ***
Resource    ../Keywords/Setup_Keywords.txt

Suite Setup    Vcc Suite Setup
Test Setup    Vcc Test Setup

*** Test Cases ***

*** Test Cases ***

Test_06 Edit an Asset
    [Documentation]    Validating Edit property of Building items
    Disable All Assets
    Expand Assets
    Enable Buildings
    Select Items Panel
    &{building_details}=    Get Building Item Details    1
    Log    ${building_details["Contact"]}
    Edit Building Contact Details
    Deselect Items Panel
    Enable Buildings
    Enable Buildings
    Select Items Panel
    &{building_details}=    Get Building Item Details    1
    Log    ${building_details["Contact"]}
    Close Edit Window
    Deselect Items Panel
    Expand Alerts

Test_08 Menu - Create CheckList Template
    [Documentation]    Validating Create CheckList Template from Menu
    Click Menu
    Click Launch Apps Tab    Checklists
    Switch to New Window
    @{old_checklists}=    Get Item List
    Create New CheckList    title=UI Automation 01
    @{new_checklists}=    Get Item List
    Validate Created Item    ${old_checklists}    ${new_checklists}    UI Automation 01
    [Teardown]    Switch to Default Window

Test_14 Menu - Create Saved View
    [Documentation]    Validating Create New Saved View from Menu
    Click Menu
    Click Tools Tab    Saved Views
    @{old_views}=    Get Saved Views
    Create New Saved View    Testing 01
    @{new_views}=    Get Saved Views
    Validate Created Item    ${old_views}    ${new_views}    Testing 01
    Close Saved View Tab