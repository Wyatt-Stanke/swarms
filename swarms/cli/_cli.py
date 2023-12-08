# import argparse
# import sys

# def run_file():
#     parser = argparse.ArgumentParser(description='Swarms CLI')
#     parser.add_argument('file_name', help='Python file containing Swarms code to run')
    
#     # Help message for the -h flag is automatically generated by argparse
#     parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0')
    
#     # Check deployments for a given model
#     parser.add_argument('-c', '--check', help='Check deployments for a given agent')

#     args = parser.parse_args()

#     # Execute the specified file
#     try:
#         with open(args.file_name, 'r') as file:
#             exec(file.read(), globals())
#     except FileNotFoundError:
#         print(f"Error: File '{args.file_name}' not found.")
#         sys.exit(1)
#     except Exception as e:
#         print(f"Error executing file '{args.file_name}': {e}")
#         sys.exit(1)

# if __name__ == '__main__':
#     main()

# swarms/cli/_cli.py
import sys
import subprocess

def run_file():
    if len(sys.argv) != 3 or sys.argv[1] != "run":
        print("Usage: swarms run file_name.py")
        sys.exit(1)

    file_name = sys.argv[2]
    subprocess.run(["python", file_name], check=True)