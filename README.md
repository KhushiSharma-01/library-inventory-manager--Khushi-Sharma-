# Library Inventory Manager

## Overview
This is a command-line library inventory manager built using Python.  
It allows campus library staff to manage books efficiently with the following features:

- Add new books
- Search books by title or ISBN
- Issue and return books
- Display all books
- Data persistence using JSON
- Logging of load/save operations
- Exception handling for file operations
- Modular, package-based structure

---

## Folder Structure
library-inventory-manager/ ├── cli/ │   └── main.py           
# JSON version CLI ├── library_manager/ │   ├── init.py       
# Required for package │   ├── book.py            
# Book class │   └── inventory.py       
# LibraryInventory class + JSON persistence + logging ├── tests/            
# Book catalog ├── main_old.py          
# TXT version CLI (old) ├── README.md        
# Project overview ├── requirements.txt      
# Optional dependencies └── .gitignore

---

## How to Run

1. Open terminal in the **root folder** (`library-inventory-manager`).

2. **Run JSON version (step 3–5)**:

```bash
python cli/main.py


Summary
- main_old.py → Demonstrates TXT version workflow (Step 1–2)
- cli/main.py → JSON version workflow with logging and persistence (Step 3–5)
- Folder structure demonstrates proper packaging and modular code (Step 6)

##Screenshots

1. screenshots\Screenshot (49).png
2. screenshots\Screenshot (50).png
3. screenshots\Screenshot (51).png
4. screenshots\Screenshot (52).png
5. screenshots\Screenshot (54).png
6. screenshots\Screenshot (55).png
7. screenshots\Screenshot (56).png
8. screenshots\Screenshot (57).png
9. screenshots\Screenshot (58).png
10. screenshots\Screenshot (60).png
11. screenshots\Screenshot (61).png
