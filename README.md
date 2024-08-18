# dec-tree-py
Python package for Visual Studio Code extension dec-tree-vscode for Decision Tree

This repository contains Python part of VSCode TypeScript extension.

![vscode_typescript_python](https://github.com/user-attachments/assets/18133ada-0085-4687-945b-ea7f7aca54b9)

child_process.py is called from TypeScript. child_channel.py, child_message.py, child_exec.py are utility classes to support recieving code from TS.

child_message is in json object form containing lists of Python imports, declarations, code and return part for TS invocations.

m_settings.py singleton stores all VSCode extension settings.

m_classifier.py is sklearn module DecisionTreeClassifier sample code implementation for VSCode extension.
