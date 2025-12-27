# Item Counter

A simple application that counts items from a comma-separated list. Available in two versions: a web-based interface and a desktop application.

## Features

- Count items from comma-separated input
- Automatically trims whitespace from items
- Filters out empty entries
- Clean, modern UI (web version)
- Simple desktop GUI (Python version)
- Press Enter to count (web version)

## Project Structure

```
CI/
├── index.html    # Web application interface
├── style.css     # Web application styles
├── script.js     # Web application logic
├── main.py       # Desktop application (Python/Tkinter)
└── README.md     # This file
```

## Web Version

### Usage

1. Open `index.html` in a web browser
2. Enter a comma-separated list of items (e.g., "CSS, JS, Python, Java")
3. Click the "Count" button or press Enter
4. The result displays the number of items

### Example

Input: `CSS, JS, Python, Java, HTML`

Output: `5`

## Desktop Version

### Requirements

- Python 3.x
- tkinter (usually included with Python)

### Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Enter a comma-separated list of items in the input field
3. Click the "Count" button
4. The result displays below the button

### Example

Input: `Apple, Banana, Cherry, Date`

Output: `4`

## How It Works

Both versions:
1. Take user input as a comma-separated string
2. Split the string by commas
3. Trim whitespace from each item
4. Filter out empty entries
5. Count and display the number of valid items

## Notes

- Empty strings and whitespace-only entries are ignored
- Leading and trailing spaces are automatically trimmed
- The web version supports keyboard shortcuts (Enter key)
- The desktop version uses Python's tkinter for the GUI

