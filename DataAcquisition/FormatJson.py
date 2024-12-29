import json
import sys

## Usage: python FormatJson.py <input_file_path> <output_file_path>
## Explanation: 
## This script takes in a JSON file and formats it using the `json.dumps()` method with the `indent` parameter set to 4 and the `ensure_ascii` parameter set to False.
## The formatted JSON data is then written to a new file specified by the `output_file_path` parameter.

def format_json_file(input_file_path, output_file_path):
    try:
        # 从文件中读取JSON数据
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            json_data = input_file.read()
        
        # 解析JSON数据
        parsed_json = json.loads(json_data)
        
        # 格式化JSON数据
        formatted_json = json.dumps(parsed_json, indent=4, ensure_ascii=False)
        
        # 将格式化后的JSON数据写入输出文件
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(formatted_json)
        
        print(f"Formatted JSON has been written to {output_file_path}")
    
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    
    except json.JSONDecodeError as jde_error:
        print(f"Error decoding JSON: {jde_error}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python FormatJson.py <input_file_path> <output_file_path>")
        return

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    
    format_json_file(input_file_path, output_file_path)

if __name__ == "__main__":
    main()