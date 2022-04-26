import os
import sys
import glob

def main():
    target_dir, head_id = sys.argv[1], int(sys.argv[2])
    if head_id == None:
        head_id = 1
    elif target_dir == None:
        print("Please include first param followed by main.py.")
        return

    print(f"Are you sure to rename all files in this directory into {target_dir}?: [Y/n]")
    intention = input()

    if intention == "n":
        return
    elif intention == "Y":
        target_files = glob.glob(f"./{target_dir}/*")

        for id, target_file_path in enumerate(target_files):
            rename_with_id(target_file_path, target_dir, str(head_id + id))
    else:
        print("Please input Y or n.")

def rm_undesired_files(file_list, extensions):
    """
    所望の拡張子を持つファイル以外が混入していないかを検閲
    :param file_list: ファイル名のリスト, extension: 所望の拡張子
    :return 所望の拡張子を持つファイルのみのリスト
    """
    for file in file_list:
        print(file)
        for ext in extensions:
            if not file.endswith(ext):
                file_list.remove(file)
                break
    return file_list

def rename_with_id(target_file_path, conv_file_name, id):
    """
    対象のファイルを識別番号付きでリネーム
    :param target_file_path: リネーム対象ファイルのパス, conv_file_name: 変換後のファイル名（拡張子なし）
    :return 所望の拡張子を持つファイルのみのリスト
    """
    # 0~9までは01, 02, ..., 09と0を付与する
    if int(id) < 10:
        id = "0" + id
    
    base_dir_pair = os.path.split(target_file_path) 
    dir_name, extension = base_dir_pair[0], base_dir_pair[1].split(".", 1)[1] # ディレクトリまでのパスと拡張子を抽出
    conv_file_path = f"{dir_name}/{conv_file_name}_{id}.{extension}"

    if os.path.isfile(target_file_path):
        os.rename(target_file_path, conv_file_path)
        print(f"renamed '{target_file_path}' into '{conv_file_path}'.")
    else:
        print("No such file.")

if __name__ == "__main__":
    main()