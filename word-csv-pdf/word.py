import numpy as np
import pdfkit

# csv文件原路径（这里采用相对路径，也可以使用绝对路径）
path = "word.csv"
# 以bytes形式导入文件
word = np.loadtxt(path, dtype=np.string_, delimiter=",")
# 打乱顺序
np.random.shuffle(word)
# 将bytes形式转化成UTF-8形式
lines = np.array([s.decode("UTF-8") for s in word])

# 设置表的宽度
td_width = 600
td_width1 = 100

# 表的模板
content = (
    '<table align="center" width="%s" border="1" cellspacing="0px" style="border-collapse:collapse">'
    % (td_width * len(lines[0].split(",")))
)
# 构造html文件
for i in range(len(lines)):
    tr = (
        "<tr>"
        + "".join(
            ['<td width="%d">%s</td>' % (td_width1, _) for _ in lines[i].split(",")]
        )
        + '<td width="%d">' % td_width1
        + "</td>"
        + '<td width="%d">' % td_width1
        + "</td>"
        + '<td width="%d">' % td_width1
        + "</td>"
        + '<td width="%d">' % td_width1
        + "</td>"
        + '<td width="%d">' % td_width1
        + "</td>"
        + "</tr>"
    )
    content += tr
content += "</table>"
html = (
    '<html><head><meta charset="UTF-8"><style>{font-family:Times New Roman}</style></head>'
    '<body><div align="left">%s</div></body></html>' % content
)

# 生成html文件
f = open("temp.html", "w", encoding="utf-8")
f.write(html)

# 转换为PDF
pdfkit.from_string(html, "test.pdf")
