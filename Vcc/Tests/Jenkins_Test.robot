*** Settings ***
Resource    ../Keywords/Setup_Keywords.txt

Suite Setup    Vcc Suite Setup
Test Setup    Vcc Test Setup

*** Test Cases ***

*** Test Cases ***

Test_04 Activate Asset
    [Documentation]    Validating Activating Asset
    Disable All Assets
    Expand Assets
    Enable Buildings
    Enable Travel
    ${feed_panel_count}=    Get Feed Count    ASSETS
    Select Items Panel
    ${item_panel_count}=    Get Item Count
    Should Be True    ${feed_panel_count} == ${item_panel_count}

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