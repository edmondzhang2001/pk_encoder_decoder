import pickle
import sys
import os

def encode_to_pk(data, file_path):
    """
    Encode data to a .pk file.
    
    :param data: The data to encode (any serializable Python object).
    :param file_path: The path to the .pk file.
    """
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)

def decode_from_pk(file_path):
    """
    Decode data from a .pk file.
    
    :param file_path: The path to the .pk file.
    :return: The decoded data.
    """
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

def main():
    if len(sys.argv) != 3:
        print("Usage: python pk_encoder_decoder.py <file_path> <encode|decode>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    action = sys.argv[2].lower()

    if action not in ["encode", "decode"]:
        print("Invalid action. Use 'encode' or 'decode'.")
        sys.exit(1)
    
    if action == "encode":
        # Read data from the file and encode it
        with open(file_path, 'r') as file:
            data = file.read()
        output_path = file_path + '.pk'
        encode_to_pk(data, output_path)
        print(f"Data encoded and saved to {output_path}")
    
    elif action == "decode":
        if not file_path.endswith('.pk'):
            print("The input file must be a .pk file for decoding.")
            sys.exit(1)
        
        # Decode data from the .pk file
        decoded_data = decode_from_pk(file_path)
        output_path = file_path.replace('.pk', '_decoded.txt')
        with open(output_path, 'w') as file:
            file.write(decoded_data)
        print(f"Data decoded and saved to {output_path}")

if __name__ == "__main__":
    main()
