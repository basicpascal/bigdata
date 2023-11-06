import pandas as pd
import plotly.graph_objs as go

# Укажите полный путь к файлу
file_path = 'airports.csv'

# Загрузка данных из CSV-файла
df = pd.read_csv(file_path)

# Создание столбчатой диаграммы
data = [go.Bar(
    x=df['name'],
    y=df['elevation_ft'],
    marker_line_width=2,            # Толщина границ столбцов
    marker_line_color='black',      # Цвет границ столбцов
)]

layout = go.Layout(
    title=dict(text='Аэропорты', x=0.5, y=1, xanchor='center', yanchor='top', font=dict(size=20)),
    xaxis=dict(title='Название аэропорта', tickangle=315, titlefont=dict(size=16), tickfont=dict(size=14)),
    yaxis=dict(title='Высота аэропорта', titlefont=dict(size=16), tickfont=dict(size=14)),
    width=700,  # Ширина графика
    height=700,  # Высота графика
    coloraxis=dict(colorscale='Viridis'),  # Цветовая шкала
    margin=dict(l=0, r=0, b=0, t=0),  # Убираем отступы
    xaxis_showgrid=True, yaxis_showgrid=True,  # Включаем сетку
    xaxis_gridwidth=2, yaxis_gridwidth=2,  # Толщина линий сетки
    xaxis_gridcolor='ivory', yaxis_gridcolor='ivory'  # Цвет сетки
)

fig = go.Figure(data=data, layout=layout)

# Отобразить диаграмму
fig.show()
