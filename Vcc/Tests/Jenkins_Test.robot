*** Settings ***
Resource    ../Keywords/Setup_Keywords.txt

Suite Setup    Vcc Suite Setup
Test Setup    Vcc Test Setup

*** Test Cases ***

Test_01 Acknowledge an Alert
    [Documentation]    Validating Acknowledge functionality of an Alert
    Enable Alerts
    ${selected_alert_title}=    Select Visible Alert    1
    Click Alert Specific Menu Item    Acknowledge
    Add Acknowledge Details
    Sleep    5s
    ${alert_present}=    Check Alert Present    ${selected_alert_title}
    Should Be True    ${alert_present} == False

Test_06 Edit an Asset
    [Documentation]    Validating Edit property of Building items
    Disable All Assets
    Expand Assets
    Activate Buildings Feed
    Select Items Panel
    &{building_details}=    Get Building Item Details    1
    ${old_value}    Set Variable    ${building_details["Contact"]}
    Edit Building Contact Details
    &{building_details}=    Get Building Item Details    1
    ${interim_value}    Set Variable    ${building_details["Contact"]}
    Close Edit Window
    Deselect Items Panel
    Deativate Buildings Feed
    Activate Buildings Feed
    Select Items Panel
    &{building_details}=    Get Building Item Details    1
    ${new_value}    Set Variable    ${building_details["Contact"]}
    Close Edit Window
    Deselect Items Panel
    Expand Alerts
    Should Not Be Equal    ${old_value}    ${new_value}
    Should Not Be Equal    ${old_value}    ${interim_value}

Test_08 Menu - Create CheckList Template
    [Documentation]    Validating Create CheckList Template from Menu
    Click Menu
    Click Launch Apps Tab    Checklists
    Sleep    30
    Switch to New Window
    @{old_checklists}=    Get Item List
    Create New CheckList    title=UI Automation 01
    @{new_checklists}=    Get Item List
    Validate Created Item    ${old_checklists}    ${new_checklists}    UI Automation 01
    [Teardown]    Run Keywords    Remove Item From List    1
    ...           AND             Switch to Default Window

