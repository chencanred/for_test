import base64,sys
from distutils import file_util
from io import BytesIO

def file_to_txt(p_file_input_full_path,p_file_output_full_path):
    with open(p_file_input_full_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())

    text_file = open(p_file_output_full_path, "w")
    text_file.write(data.decode("utf-8"))
    text_file.close()

def txt_to_file(p_file_output_txt_full_path,p_file_output_full_path):
    print(p_file_output_txt_full_path)
    text_file = open(p_file_output_txt_full_path, "r")
    base64str = text_file.read()
    bytes_data = base64str.encode("utf-8")
    text_file.close()

    f = open(p_file_output_full_path, 'wb')
    _bytes = base64.b64decode(bytes_data)
    f.write(_bytes)
    f.close()

while True:
    print("选择功能")
    print("[1]档案转出Base64内容")
    print("[2]Base64内容的档案还原成档案")
    print("[Q]离开")
    action_flag = input("请输入要执行的功能代号（1,2,Q）:")
    if action_flag == "Q":
        print("Bye!")
        sys.exit()
    elif action_flag == "1":    
        str_input_file_full_path = input("请输入要转换档案完整路径(File 2 Base64)：")
        print(str_input_file_full_path[0:str_input_file_full_path.rfind('\\')+1])
        str_out_file_full_path = str_input_file_full_path[0:str_input_file_full_path.rfind('\\')+1] + str_input_file_full_path[str_input_file_full_path.rfind('\\')+1:]+".txt"
        print("输出完成路径：",str_out_file_full_path)
        print("")
        file_to_txt(str_input_file_full_path,str_out_file_full_path)
        print("Success")
    elif action_flag == "2":    
        str_input_file_full_path = input("请输入要转换档案完整路径(Base64 2 File)：")        
        str_out_file_full_path = input("请输入要输出档案完整路径：")        
        txt_to_file(str_input_file_full_path,str_out_file_full_path)
        print("Success")