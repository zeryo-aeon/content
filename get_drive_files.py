import gdown
import os
import json

def main():
    all_file_details = []
    
    # Load folder configurations from separate JSON file
    try:
        with open('folders.json', 'r', encoding='utf-8') as f:
            folders = json.load(f)
    except Exception as e:
        print(f"Error reading folders.json: {e}")
        return

    for folder in folders:
        folder_url = folder["url"]
        base_path = folder["base_path"]
        
        print(f"Processing folder for base_path: {base_path}")
        
        try:
            # Download/list files
            files = gdown.download_folder(
                folder_url,
                quiet=True,
                skip_download=True
            )
            
            if files:
                for file in files:
                    file_name = os.path.basename(file.path)
                    if file_name.lower().endswith((".pdf", ".png", ".jpeg")):
                        all_file_details.append({
                            "file_name": file_name,
                            "file_id": file.id,
                            "path": base_path + '/' + file.path
                        })
            
            print(f"Processed {base_path}")
        except Exception as e:
            print(f"Error processing {base_path}: {e}")

    # Save all combined output to content.json
    output_filename = "content.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(all_file_details, f, indent=2)
    
    print(f"\nSaved total of {len(all_file_details)} files to {output_filename}")

if __name__ == "__main__":
    main()
