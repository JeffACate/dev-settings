[back to home](https://www.github.com/JeffACate/dev-settings#development-environment) |
[browser](https://www.github.com/JeffACate/dev-settings/blob/master/browser.md#browser-settings) |
[vscode](https://www.github.com/JeffACate/dev-settings/blob/master/vscode.md#vs-code-settings)

## Terminal Settings
* [Git for Windows - Mintty terminal](https://gitforwindows.org/)
    * [ ] Update shell settings 
        ```
        code ~/.bashrc
        alias a='alias'
        alias e='exit'
        alias l='ls -lah'
        alias rmdir='rm -rf'
        alias mk='touch'

        alias c='cd ~/current/'
        alias p='cd ~/current/post-grad/'
        alias r='cd ~/current/post-grad/Repos'
        p
        ```
    * [ ] First-Time Git Setup
        ```
        git config --list --show-origin
        git config --global user.name "User Name"
        git config --global user.email myemail@address.com
        git config --global core.editor "code --wait"
        ```

[back to home](https://www.github.com/JeffACate/dev-settings#development-environment) |
[browser](https://www.github.com/JeffACate/dev-settings/blob/master/browser.md#browser-settings) |
[vscode](https://www.github.com/JeffACate/dev-settings/blob/master/vscode.md#vs-code-settings)