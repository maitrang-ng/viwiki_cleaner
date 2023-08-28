import argparse
from cleaner import open_folder, clean_text

def main(folder_path, n1, n2 ):
    file_paths = open_folder(folder_path)

    for i in range(int(n1), int(n2)):
        # Specify the file path
        input_file_path = file_paths[i]
        clean_text(input_file_path)

    # with open(output_file, 'w', encoding='utf-8') as f:
    #     f.write(content)

    # print("Manipulated content saved to", output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Manipulate and save text from input file to output file')
    
    parser.add_argument('input', help='Input folder path', default="/mnt/c/Users/maitr/Downloads/vi_corpus/vi_corpus")
    parser.add_argument('n1', help='Row number for starting process')
    parser.add_argument('n2', help='Row number for ending process')
    #parser.add_argument('output', help='Output file path')

    args = parser.parse_args()
    main(args.input, args.n1, args.n2)





