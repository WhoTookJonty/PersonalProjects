# pyinstaller --noconfirm --onedir --windowed --add-data "c:\users\jonty\appdata\local\programs\python\python310\lib\site-packages/customtkinter;customtkinter/" --add-data "InventoryEdits/images/*.png;InventoryEdits/images/" automate.py

from InventoryEdits.StarRezAutomation import main

if __name__ == "__main__":
    main()