import re
from pathlib import Path

# 使用前，将中英本地化文件放在该.py文件的同一目录下！
# 包括“TF_VR_MoveLine“在内的3个词条会报缺失，因为英文版本里的换行方式不规范，没有用换行符

loc_file_a = "tf_schinese.txt"
loc_file_b = "tf_english.txt"


def parse_loc_file(file_path):
    entries = {}

    # 正则表达式：
    # group 1 = key, ([^"\n]+)
    # group 2 = text, ([^"\n]*)
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


def compare_keys(file_a, file_b):
    keys_a = set(file_a.keys())
    keys_b = set(file_b.keys())

    only_in_a = keys_a - keys_b
    only_in_b = keys_b - keys_a
    both_keys = keys_a & keys_b

    return sorted(only_in_a), sorted(only_in_b), sorted(both_keys)


def main():
    # 读取并解析文件
    dict_a = parse_loc_file(Path(loc_file_a))
    dict_b = parse_loc_file(Path(loc_file_b))

    # 比对
    only_a, only_b, both = compare_keys(dict_a, dict_b)

    print(f"检测到{loc_file_a}词条数：{len(dict_a)}")
    print(f"检测到{loc_file_b}词条数：{len(dict_b)}\n")

    print(f"{loc_file_a}中存在但{loc_file_b}缺失的词条（共 {len(only_a)} 个）：")
    for key in only_a:
        print(f"{key}")

    print(f"\n{loc_file_b}中存在但{loc_file_a}缺失的词条（共 {len(only_b)} 个）：")
    for key in only_b:
        print(f"{key}")


if __name__ == "__main__":
    main()
