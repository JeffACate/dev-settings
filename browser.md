[back to home](https://www.github.com/JeffACate/dev-settings/) |
[vscode](https://www.github.com/JeffACate/dev-settings/blob/master/vscode.md)

## Browser Settings
* [Firefox](https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US)
    * [General Settings](about:preferences)
    * [Advanced settings](about:config)
        * [ ] browser.ctrlTab.recentlyUsedOrder = false
        * [ ] browser.link (type: neww)
            * [ ] open_newwindow = 1
            * [ ] open_newwindow.restriction = 0 
            * [ ] open_newwindow.override.external = 3
<!--         
        (A) browser.link.open_newwindow - for links in Firefox tabs

        This is the one that has a checkbox on the Preferences page:
        
        3 = divert new window to a new tab (default)
        2 = allow link to open a new window
        1 = force new window into same tab 

        (B) browse.link.open_newwindow.restriction - for links in Firefox tabs

        By default, if a page sets width, height, or toolbars for a popup, Firefox will let it be a separate window. To force those into a tab as well, you can change this preference to 0:

        0 = apply the setting under (A) to ALL new windows (even script windows with features) 
        2 = apply the setting under (A) to normal windows, but NOT to script windows with features (default)
        1 = override the setting under (A) and always use new windows 

        (C) browser.link.open_newwindow.override.external - for links in other programs

        -1 = apply the setting under (A) to external links (default)
        3 = open external links in a new tab in the last active window
        2 = open external links in a new window
        1 = open external links in the last active tab replacing the current page 
-->
### Add-ons
* Extensions
    * [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)
    * [Privacy Badger](https://privacybadger.org/)
    * [Cookie AutoDelete](https://addons.mozilla.org/en-US/firefox/addon/cookie-autodelete/)
    * [Decentraleyes](https://addons.mozilla.org/en-US/firefox/addon/decentraleyes/)
    * [Http-everywhere](https://www.eff.org/https-everywhere)
    * [Stylus](https://addons.mozilla.org/addon/tabliss?src=external-tabliss.io)
        * [Github Dark](moz-extension://9ed557e8-8284-4dba-9061-fd436898f88b/edit.html?id=1)
        * [Stack Overflow Dark](moz-extension://07ae76b8-2b28-46b6-974a-f0103da7dcae/edit.html)
    * [Tabliss.io](https://tabliss.io)
    * [JSON Viewer - Brave/Chrome](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?h1=en) 
        ```
        Theme: dracula-dark
        Add-ons
        {
            "prependHeader": true,
            "maxJsonSize": 1000,
            "alwaysFold": false,
            "alwaysRenderAllContent": false,
            "sortKeys": false,
            "clickableUrls": true,
            "wrapLinkWithAnchorTag": false,
            "openLinksInNewWindow": true,
            "autoHighlight": true
        }
        Structure:
        {
            "readOnly": true,
            "lineNumbers": true,
            "lineWrapping": true,
            "foldGutter": true,
            "tabSize": 4,
            "indentCStyle": false,
            "showArraySize": false
        }

        Custom Style:
        .CodeMirror {
            font-family: Anonymous Pro, Calibri,monaco, Consolas, Menlo, Courier, monospace;
            font-size: 16px;
            line-height: 1.5em;
        }

        ```


<!-- * Brave/Chrome
        * [Just Black](https://chrome.google.com/webstore/detail/just-black/aghfnjkcakhmadgdomlmlhhaocbkloab) -->
<!--
### Bookmarks

    * [Bullet Point text](Linked Address here)
        * Description of address above

    -[ ] empty to do 
-->
[back to home](https://www.github.com/JeffACate/dev-settings/) |
[vscode](https://www.github.com/JeffACate/dev-settings/blob/master/vscode.md)