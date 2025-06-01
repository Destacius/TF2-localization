import re
from pathlib import Path

# 使用前，将本地化文件放在该.py文件的同一目录下！
# loc_file_input = "tf_schinese.txt"
loc_file_input = ["tf_schinese.txt", "tf_proto_obj_defs_schinese.txt", "tf_quests_schinese.txt"]
keyword_text = "猛鬼车站"  # ÜberCharge, TF_Map_

mode = 1  # 0 = search key, 1 = search value


def search_key(loc_dict, keyword):
    results = {}
    for key, value in loc_dict.items():
        if keyword in key:
            results[key] = value
    return results


def search_value(loc_dict, keyword):
    results = {}
    for key, value in loc_dict.items():
        if keyword in value:
            results[key] = value
    return results


def parse_loc_file(file_path):
    entries = {}

    # 正则表达式：group 1 = key, group 2 = text
    pattern = re.compile(r'^\s*"([^"\n]+)"\s+"([^"\n]*)"')

    with open(file_path, encoding="utf-16") as localization_file:
        for line in localization_file:
            line = line.strip()
            if not line or line.startswith("//"):
                continue

            match = pattern.match(line)
            if match:
                key, text = match.groups()
                if text.strip() == "":
                    continue  # 跳过空白项
                entries[key] = text

    return dict(entries)


def main():
    # # 读取文件
    # loc_file = Path(loc_file_input)
    # loc_file_content = parse_loc_file(loc_file)
    #
    # if mode == 1:
    #     matched_entries = search_value(loc_file_content, keyword_text)
    # elif mode == 0:
    #     matched_entries = search_key(loc_file_content, keyword_text)
    #
    # print(f"包含关键词“{keyword_text}”的词条（共 {len(matched_entries)} 项）：\n")
    # for key, value in matched_entries.items():
    #     print(f"{key}")
    #     # print(f"{key}: {value}")

    for file in loc_file_input:
        loc_file = Path(file)
        loc_file_content = parse_loc_file(loc_file)

        matched_entries = search_value(loc_file_content, keyword_text)
        print(f"\n文件“{file}”，包含关键词“{keyword_text}”的词条（共 {len(matched_entries)} 项）：\n")
        for key, value in matched_entries.items():
            print(f"{key}")
            # print(f"{key}: {value}")


if __name__ == "__main__":
    main()
