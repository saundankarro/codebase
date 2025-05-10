import re

def remove_suffix(text):
    return re.sub(r"_\d_\d_\d.", '.', text)

txt = "test_0_0_0.csv"

print(f"Text = {txt}")

new_txt = remove_suffix(txt)
print(f"New Text = {new_txt}")

txt_2 = 'test_20250405_0_0_0.csv'
print(f"Test 2 = {remove_suffix(txt_2)}")


txt_3 = 'test_20250405_2025_20252002_20243.csv'
print(f"Test 3 = {remove_suffix(txt_3)}")