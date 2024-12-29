import urllib.parse

def url_decode_from_file(input_file, output_file):
    """
    从输入文件中读取URL编码的字符串，解码后写入到输出文件中。

    参数:
    input_file (str): 包含URL编码字符串的输入文件名。
    output_file (str): 存储解码后字符串的输出文件名。
    """
    try:
        # 打开输入文件读取内容
        with open(input_file, 'r', encoding='utf-8') as infile:
            encoded_string = infile.read().strip()  # 读取整个文件内容并去除首尾空白字符

        # 对URL编码的字符串进行解码
        decoded_string = urllib.parse.unquote(encoded_string)

        # 将解码后的字符串写入到输出文件中
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(decoded_string)

        print(f"解码成功，结果已写入到 {output_file}")

    except FileNotFoundError:
        print(f"错误：文件 {input_file} 未找到。")
    except Exception as e:
        print(f"发生错误：{e}")

# 示例用法
input_filename = 'rec1.txt'  # 输入文件名
output_filename = 'out.txt'  # 输出文件名
url_decode_from_file(input_filename, output_filename)