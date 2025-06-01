import csv

# 使用前，将csv表格放在该.py文件的同一目录下！
excel_input = "crowdin.csv"
dict_result = {}
checked_keys = set()

# 各类统计
total_rows = 0
valid_rows = 0
duplicate_rows = 0
empty_rows = 0
short_rows = 0


# 打开工作簿
with open(excel_input, newline='', encoding='gb18030') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过表头
    for row_num, row in enumerate(reader, start=2):
        total_rows += 1

        if len(row) >= 2:
            key = row[0].strip()
            value = row[1].strip()

            if not key or not value:
                print(f"空值 → 第 {row_num} 行：{key}")
                empty_rows += 1
                continue

            if key in checked_keys:
                print(f"重复key → 第 {row_num} 行：{key}")
                duplicate_rows += 1

            checked_keys.add(key)
            dict_result[key] = value
            valid_rows += 1

        else:
            print(f"列数不足 → 第 {row_num} 行：{key}")
            short_rows += 1

print(len(dict_result))
print(dict_result)

