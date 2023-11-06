import pandas as pd
import plotly.graph_objs as go

# Укажите полный путь к файлу на диске D:
file_path = 'airports.csv'

# Загрузка данных из CSV-файла
df = pd.read_csv(file_path)

# Ограничение количества значений до 15
df = df.head(15)

# Создание круговой диаграммы
data = [go.Pie(
    labels=df['name'],
    values=df['elevation_ft'],        marker=dict(line=dict(color='black', width=2)),  # Выделение границ чёрной линией
    textinfo='label+percent',  # Включить текст с метками и процентами
)]

layout = go.Layout(
    title=dict(text='Аэропорты', x=0.5, y=1, xanchor='center', yanchor='top', font=dict(size=20)),
    width=700,  # Ширина графика
    height=700,  # Высота графика
    margin=dict(l=0, r=0, b=0, t=0),  # Убираем отступы
)

fig = go.Figure(data=data, layout=layout)

# Отобразить круговую диаграмму
fig.show()
