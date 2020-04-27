*** Settings ***
Resource    ../Keywords/Setup_Keywords.txt

Suite Setup    Vcc Suite Setup


Test Setup    Vcc Test Setup
Test Teardown    Run Keyword If Test Failed    Refresh Home Page

*** Test Cases ***

Test_01 Acknowledge an Alert
    [Documentation]    Validating Acknowledge functionality of an Alert
    Enable Alerts
    ${selected_alert_title}=    Select Visible Alert
    Click Alert Specific Menu Item    Acknowledge
    Add Acknowledge Details
    Sleep    5s
    ${alert_present}=    Check Alert Present    ${selected_alert_title}
    Verify Object Equal    ${alert_present}    ${False}

Test_03 Activate Risk Event
    [Documentation]    Validating Activating Risk Event
    Disable Alerts
    Disable All Risk Events
    Expand Risk Events
    Activate Inrix Traffic
    ${feed_panel_count}=    Get Feed Count    RISK EVENTS
    Select Items Panel
    ${item_panel_count}=    Get Item Count
    Deativate Inrix Traffic
    Verify Object Equal    ${feed_panel_count}    ${item_panel_count}

Test_04 Activate Asset
    [Documentation]    Validating Activating Asset
    Disable All Assets
    Expand Assets
    Activate Buildings Feed
    Activate Travel Feed
    ${feed_panel_count}=    Get Feed Count    ASSETS
    Select Items Panel
    ${item_panel_count}=    Get Item Count
    Verify Object Equal    ${feed_panel_count}    ${item_panel_count}
    [Teardown]    Run Keywords    Deativate Buildings Feed
    ...           AND             Deactivate Travel Feed
    ...           AND             Deselect Items Panel

Test_06 Edit an Asset
    [Documentation]    Validating Edit property of Building items
    Disable All Assets
    Expand Assets
    Activate Buildings Feed
    Select Items Panel
    &{building_details}=    Get Building Item Details    1
    ${old_value}    Set Variable    ${building_details["Contact"]}
    Edit Building Contact Details
    Deselect Items Panel
    Deativate Buildings Feed
    Activate Buildings Feed
    Select Items Panel
    &{building_details}=    Get Building Item Details    1
    ${new_value}    Set Variable    ${building_details["Contact"]}
    Close Edit Window
    Deselect Items Panel
    Expand Alerts
    Verify Object Not Equal    ${old_value}    ${new_value}


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
    ...           AND            Switch to Default Window

Test_09 Menu - Create Note
    [Documentation]    Validating Create note from Menu
    Click Menu
    Click Launch Apps Tab    Notes
    Switch to New Window
    @{old_notes}=    Get Item List
    Create New Note    title=UI Automation 01
    @{new_notes}=    Get Item List
    Validate Created Item    ${old_notes}    ${new_notes}    UI Automation 01
    [Teardown]    Run Keywords    Remove Item From List    1
    ...           AND            Switch to Default Window

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

Test_12 Send Message from Menu
    [Documentation]    Validating Send Message functionality
    Enable Alerts
    ${selected_alert_title}=    Select Visible Alert
    Click Alert Specific Menu Item    Send Email
    Add Email Details And Send
    Sleep    5s

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
    [Teardown]    Run Keywords    Delete Saved View    Testing 01
    ...           AND             Close Saved View Tab

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
