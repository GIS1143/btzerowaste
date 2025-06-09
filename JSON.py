import pandas as pd

# โหลดไฟล์ Excel ทั้งหมดทุกชีท
file_path = "นักเรียนทั้งหมด.xlsx"
xls = pd.ExcelFile(file_path)

# เตรียมลิสต์ไว้รวมข้อมูลจากทุกชีท
all_data = []

# วนลูปทุกชีท
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, usecols=["Unnamed: 1", "Unnamed: 3"])
    df.columns = ["id", "name"]
    all_data.append(df)

# รวมทุกชีทเป็น DataFrame เดียว
combined_df = pd.concat(all_data, ignore_index=True)

# ลบแถวที่ไม่มีรหัสหรือชื่อ
combined_df.dropna(subset=["id", "name"], inplace=True)

# แปลงเป็น JSON
json_data = combined_df.to_json(orient="records", force_ascii=False)

# บันทึกเป็นไฟล์ JSON
with open("students.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

print("🔥 ไฟล์ JSON รวมทุกชีทถูกสร้างแล้ว!")
