# CSV_to_SRT

Convert CSV to SRT

## Requirements:
- Python installed on your device

## To convert an Excel file into an SRT (SubRip Subtitle) file, follow these steps:

### Step 1: Format Your Excel Data
Ensure your Excel file has the necessary subtitle information. Each subtitle in an SRT file includes:

- **Index**: A sequential number.
- **Timecode**: Start and end times in the format `hh:mm:ss,mmm --> hh:mm:ss,mmm`.
- **Text**: Subtitle content.

Your Excel columns should look like this:

| Index | Start Time      | End Time        | Text           |
|-------|-----------------|-----------------|----------------|
| 1     | 00:00:01,000    | 00:00:04,000    | Hello, world!  |

### Step 2: Save Excel as CSV
1. Open your Excel file.
2. Click **File > Save As** and choose **CSV (Comma delimited) (.csv)**.
3. Save it as subtitles.csv

### Step 3: Run the Script
1. Place the script in the same directory as your CSV file.
2. Run the script in a terminal or command prompt:

   ```bash
   python convert_csv_to_srt.py
