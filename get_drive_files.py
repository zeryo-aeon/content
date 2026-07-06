import gdown
import os
import json
import hashlib
import tempfile
import shutil


def calculate_md5(file_path):
    """Calculate MD5 hash of a file."""
    md5 = hashlib.md5()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            md5.update(chunk)

    return md5.hexdigest()


def main(folder, output):
    all_file_details = []

    try:
        with open(folder, "r", encoding="utf-8") as f:
            folders = json.load(f)
    except Exception as e:
        print(f"Error reading {folder}: {e}")
        return

    # Temporary directory for downloads
    temp_dir = tempfile.mkdtemp(prefix="gdown_md5_")

    try:
        for folder_info in folders:
            folder_url = folder_info["url"]
            base_path = folder_info["base_path"]

            print(f"\nProcessing: {base_path}")

            try:
                # List files only
                files = gdown.download_folder(
                    folder_url,
                    quiet=True,
                    skip_download=True
                )

                if not files:
                    continue

                for file in files:
                    file_name = os.path.basename(file.path)

                    if not file_name.lower().endswith((".pdf", ".png", ".jpeg")):
                        continue

                    md5_hash = None

                    try:
                        # Download file temporarily
                        temp_file = os.path.join(temp_dir, file_name)

                        gdown.download(
                            id=file.id,
                            output=temp_file,
                            quiet=True
                        )

                        if os.path.exists(temp_file):
                            md5_hash = calculate_md5(temp_file)
                            os.remove(temp_file)

                    except Exception as e:
                        print(f"MD5 failed for {file_name}: {e}")

                    all_file_details.append({
                        "file_name": file_name,
                        "file_id": file.id,
                        "path": file.path,
                        "md5": md5_hash
                    })

                print(f"Processed {base_path}")

            except Exception as e:
                print(f"Error processing {base_path}: {e}")

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    output_filename = output if output.endswith(".json") else output + ".json"

    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(all_file_details, f, indent=2)

    print(f"\nSaved {len(all_file_details)} files to {output_filename}")


if __name__ == "__main__":
    main("folders.json", "content.json")
