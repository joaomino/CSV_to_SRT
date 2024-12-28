import csv

# Input and output file names
csv_file = "subtitles.csv"  # Your CSV file
srt_file = "subtitles.srt"  # Output SRT file

# Read the CSV and write to SRT
with open(csv_file, "r", encoding="utf-8") as csvfile, open(srt_file, "w", encoding="utf-8") as srtfile:
    reader = csv.DictReader(csvfile, delimiter=';')  # Use ; as the delimiter
    for row in reader:
        srtfile.write(f"{row['Index']}\n")
        srtfile.write(f"{row['Start Time']} --> {row['End Time']}\n")
        srtfile.write(f"{row['Text']}\n\n")

print("Conversion complete!")