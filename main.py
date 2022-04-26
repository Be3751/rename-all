import os
import sys
import glob

def main():
    # 標準入力から対象ディレクトリ名と変換後ファイル名を取得
    target_dir, conv_file = sys.argv[1], sys.argv[2]
    print(f"target directory: {target_dir}, converted file name: {conv_file}")

    # コマンドライン引数が不足していた場合のエラーハンドリング
    if(target_dir == None or conv_file == None):
        pass

    # 対象ディレクトリ内のファイル名を取得
    target_files = glob.glob(f"./{target_dir}/*")
    print(target_files)

    # ディレクトリを除く

    # 所望の拡張子を持つファイル以外が混入していないかを検閲
    checked_files = rm_undesired_files(target_files)

    # 変換後ファイル名と識別番号を組み合わせたファイル名で対象ファイル名を上書き
    

def rm_undesired_files(file_list, extensions):
    """
    所望の拡張子を持つファイル以外が混入していないかを検閲
    :param file_list: ファイル名のリスト, extension: 所望の拡張子
    :return 所望の拡張子を持つファイルのみのリスト
    """
    for file in file_list:
        for ext in extensions:
            if not file.endswith(ext):
                file_list.remove(file)
    
    return file_list

def rename_with_id(target_file, conv_file, id):
    conv_file_id = conv_file + id
    os.rename(target_file, conv_file)

if __name__ == "__main__":
    main()