import sys
import markdown

def convertHTML(input_file,output_file):
    try:
        with open(input_file,'r') as f:
            md_file = f.read()
            html_file =markdown.markdown(md_file) 
        with open(output_file,'w') as f2:
            f2.write(html_file)

            
    except FileNotFoundError:
        print("file is not found")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 main.py markdown inputfile outputfile")
        sys.exit(1)

    command,input_file,output_file = sys.argv[1:]

    if command != "markdown":
        print("Usage: command is markdown")
        sys.exit(1)

    convertHTML(input_file,output_file)

if __name__ == "__main__":
    main()