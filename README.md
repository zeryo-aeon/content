# Content Repository

This repository serves as a centralized storage for various content materials.

## File Structure

The repository uses a modular approach where different content categories are managed in separate JSON files.

-   **content.json**: The main index file that aggregates information from all content categories.
-   **crypto.json**: Contains information about cryptocurrency-related content.
-   **folders.json**: A configuration file that defines the Google Drive folders to be processed and their corresponding base paths.

## Scripts

-   `get_drive_files.py`: A Python script that fetches file metadata from Google Drive folders specified in `folders.json` and updates `content.json`.

## Usage

To update the content index, run the following command:

```bash
python get_drive_files.py
```

This script will:
1.  Read the folder configurations from `folders.json`.
2.  Fetch file details from each specified Google Drive folder.
3.  Consolidate the information into `content.json`.

### Adding New Content

To add a new category of content:
1.  Add the Google Drive folder URL and a unique `base_path` (e.g., `blockchain`, `ai`) to `folders.json`.
2.  Run `python get_drive_files.py` to update `content.json`.

The script will automatically create a new JSON file for the new category (e.g., `blockchain.json`) if needed, or append to `content.json`.