[back to home](https://www.github.com/JeffACate/dev-settings#development-environment) |
[terminal](https://www.github.com/JeffACate/dev-settings/blob/master/Windows/terminal.md#terminal-settings) |
[browser](https://www.github.com/JeffACate/dev-settings/blob/master/browser.md#browser-settings)

## VS Code Settings
* [VS Code](https://code.visualstudio.com/)
  * edit settings.json here linux-mint: ~/.config/Code/User/settings.json
  * edit settings.json here Windows: C:\Users\Jeff\AppData\Roaming\Code\User\settings.json
  
### Themes/Color
* Current theme:
  * [Just Black](https://marketplace.visualstudio.com/items?itemName=nur.just-black)
    * ext install nur.just-black
* Themes to try:
  * [Seti-Monokai](https://marketplace.visualstudio.com/items?itemName=SmukkeKim.theme-setimonokai)
  * [Seti-Black](https://marketplace.visualstudio.com/items?itemName=bobsparadox.seti-black)
  * [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
    * add to settings.json - "workbench.iconTheme": "vscode-icons",

### Extensions
  * See my full list of extensions [here](https://gist.github.com/w3cj/520eb023dd3531d1b654794f65aa434b).
* [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=coenraads.bracket-pair-colorizer)
  * Matching parenthesis and curly brackets to with colors
  * Instal with: Ctrl + P -> ext install CoenraadS.bracket-pair-colorizer
* [Auto Close Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag)
  * Automatically add HTML/XML close tag
* [Auto Rename Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag)
  * Automatically rename paired HTML/XML tag
* [FontSize ShortCuts](https://marketplace.visualstudio.com/items?itemName=fosshaas.fontsize-shortcuts)
  * Change the font size with keyboard shortcuts.

### IntelliSense/AutoComplete

* [IntelliSense for CSS class names in HTML](https://marketplace.visualstudio.com/items?itemName=Zignd.html-css-class-completion)
  * Provides CSS class name completion for the HTML class attribute based on the definitions found in your workspace or external files referenced through the link element
* [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense)
  * Autocompletes filenames
* [VS Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)
  * Collaborative editing, debugging, and more inside VS Code

### Useful/Extra

* [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost)
  * Display inline the size of the required/imported package
* [Quokka.js](https://marketplace.visualstudio.com/items?itemName=WallabyJs.quokka-vscode)
  * Evaluate code/logs inline and show results in the editor
* [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
  * Integrates ESLint JS
    ```
    "eslint.enable": true,
    // "files.exclude": { "**/.*": true },
    "eslint.validate": [
      {
        "language": "vue",
        "autoFix": true
      },
      {
          "language": "typescript",
          "autoFix": true
        },
      {
        "language": "html",
        "autoFix": true
      },
      {
        "language": "javascript",
        "autoFix": true
      }
    ], 
    ```
* [Beautify](https://marketplace.visualstudio.com/items?itemName=hookyqr.beautify)
  * Automatically format javascript, JSON, CSS, Sass, and HTML files.
  * add to settings.json
    ```
    "editor.tabSize": 2,
    "editor.detectIndentation": true,
    "[javascript]": {
      "editor.defaultFormatter": "HookyQR.beautify"
    },
    "[json]": {
      "editor.defaultFormatter": "HookyQR.beautify"
    },
    "[html]": {
      "editor.defaultFormatter": "HookyQR.beautify"
    },
    "[css]": {
      "editor.defaultFormatter": "HookyQR.beautify"
    },
    ```

### Settings
```
{
  "explorer.openEditors.visible": 0,
  "editor.snippetSuggestions": "top",
  "emmet.showAbbreviationSuggestions": false,
  "editor.formatOnPaste": false,
  "workbench.colorTheme": "Just Black",
  "window.zoomLevel": 0,
  "editor.fontLigatures": true,
  "terminal.integrated.fontSize": 16,
  "files.autoSave": "off",
  "editor.fontFamily": "'Anonymous Pro Regular','Anonymous Pro', Consolas",
  "markdown.preview.fontSize": 16,
  "editor.detectIndentation": true,
  "editor.minimap.enabled": false,
  "editor.fontSize": 16,

  // "files.exclude": { "**/.*": true },
  "eslint.validate": [
    {
      "language": "vue",
      "autoFix": true
    },
    {
        "language": "typescript",
        "autoFix": true
      },
    {
      "language": "html",
      "autoFix": true
    },
    {
      "language": "javascript",
      "autoFix": true
    }
  ],
  "workbench.startupEditor": "newUntitledFile",
  "editor.suggestSelection": "first",
  "editor.tokenColorCustomizations": {
    "textMateRules": [
      {
        "scope": [
          "comment",
          "comment.block"
        ],
        "settings": {
          "fontStyle": "italic",
          "foreground": "#ff1493"
        }
      },
      {
        "scope": [
          "keyword.operator.logical",
          "keyword.operator.arithmetic",
          "keyword.operator.assignment",
          "keyword.operator.bitwise"
        ],
        "settings": {
          "fontStyle": ""
        }
      }
    ]
  },
  "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
  "[scss]": {

    "editor.suggest.insertMode": "replace"
  }
}
```

[back to home](https://www.github.com/JeffACate/dev-settings#development-environment) |
[terminal](https://www.github.com/JeffACate/dev-settings/blob/master/Windows/terminal.md#terminal-settings) |
[browser](https://www.github.com/JeffACate/dev-settings/blob/master/browser.md#browser-settings)