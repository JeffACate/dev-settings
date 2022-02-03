# from https://gist.github.com/w3cj/520eb023dd3531d1b654794f65aa434b?permalink_comment_id=3591362#gistcomment-3591362
import os
with open('vscode-extensions.txt') as f:
    for line in f:
        os.system('code --install-extension ' + line)
