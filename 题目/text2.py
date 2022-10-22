a = input("请输入内容：")
ans = 0
for i in range(len(a)):
    if a[i] == " ":
        print(f"第{i}个元素为空")
        ans += 1

if ans == 0:
    print("不存在空元素")

