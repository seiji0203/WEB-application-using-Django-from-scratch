import streamlit as st
import numpy as np
import pandas as pd

st.title('web')

st.write('Hello individuals, How you guys doing? I am seiji nice to meet you :) ')

df = pd.DataFrame({
     '一列目': [1, 2, 3, 4],
    '二列目':[10, 20, 30, 40]
    })


# st.write(df)でもできる
st.dataframe(df.style.highlight_max(axis=0))
# 静的なフレーム st.table(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))



# 
# 章
## 節
### 項

# ```
#PYTHON
# import numpy as np
# import pandas as pd
# ```
#

# https://docs.streamlit.io/en/stable/api.html#

# df = pd.DataFrame(
#     np.random.rand(30, 2),
#    columns=['a', 'b', 'c']
#  )
# 乱数を正規分布に従って発生させたものを表として表示　st.table(df.style.highlight_max(axis=0))
# 線グラフ　st.line_chart(df)
# 線グラフの下を塗ってくれる　st.area＿chart(df)
# 棒グラフ　st.bar(df)

# df = pd.DataFrame(
#      np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
 )
# 中身確認　df
# st.map(df)

# from PIL import Image

# img = Image.open('Seiji.jpeg')
# st.image(img, caption='Seiji', use_column_width=True)


