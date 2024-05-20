# PK Encoder/Decoder

This repository contains a Python script for encoding and decoding text files to and from `.pk` files using Python's `pickle` module. 

## Files

- `pk_encoder_decoder.py`: The main script for encoding and decoding files.
- `sample.txt`: A sample text file used to demonstrate the encoding and decoding process.

## Requirements

- Python 3.x

## Usage

### Encode a Text File

To encode a text file (e.g., `sample.txt`), run the following command:

```bash
python pk_encoder_decoder.py sample.txt encode
```
This command will create a file named sample.txt.pk in the same directory.

### Decode a PK File
To decode a .pk file (e.g., sample.txt.pk), run the following command:

```bash
python pk_encoder_decoder.py sample.txt.pk decode
```
This command will create a file named sample_decoded.txt in the same directory, containing the original text.

### Example
Ensure you have Python 3 installed.

Clone the repository or download the files.

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

Run the encoding script:

```bash
python pk_encoder_decoder.py sample.txt encode
```
You should see an output indicating that the data has been encoded and saved to sample.txt.pk.

Run the decoding script:

```bash
python pk_encoder_decoder.py sample.txt.pk decode
```
You should see an output indicating that the data has been decoded and saved to sample_decoded.txt.

Check the contents of sample_decoded.txt to verify it matches the original sample.txt.

### Notes
Ensure the file path provided to the script exists and is accessible.
The script assumes text files for encoding. If you need to encode other types of data, adjust the reading and writing parts of the script accordingly.
