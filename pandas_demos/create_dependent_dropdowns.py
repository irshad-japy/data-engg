import analyticslab as al
import altair as alt
import ipywidgets as widgets
import pandas as pd
import os
import io
import glob
from IPython.display import display

path = os.getcwd()
value_stream_name = ''
vs_category_type = ''
print(path)

csvfile_dropdown = al.ui.widget_selection.ComboBox(label='Select csvfile: ',
                                                   options=['Hubble.csv', 'Investor Model.csv', 'QE.csv'])
xaxis_dropdown = al.ui.widget_selection.ComboBox(label='Select metric1-xaxis: ', options=['x-axis metric'])
yaxis_dropdown = al.ui.widget_selection.ComboBox(label='Select metric2-yaxis: ', options=['y-axis metric'])
canvas_one = widgets.Output()


def update(*args):
    print('3' * 30)
    path = os.getcwd()
    print(csvfile_dropdown.value)
    df = list_of_xaxis_data(path)
    with canvas_one:
        print('4' * 30)
        xaxis_dropdown.options = list(df.columns)
        yaxis_dropdown.options = list(df.columns)


def list_of_axis_data(columns):
    csvfile_location = path + '/' + 'bridge' + '/' + 'april' + '/' + 'QE.csv'
    csv_data = pd.read_csv(csvfile_location)
    df = pd.DataFrame(csv_data)
    return df[columns]


csvfile_dropdown.add_observer(update)


def random_function():
    print('1' * 30)
    with canvas_one:
        print('2' * 30)
        display(csvfile_dropdown.show())
        display(xaxis_dropdown.show())
        display(yaxis_dropdown.show())


widgets.interact(random_function, x=csvfile_dropdown, y=xaxis_dropdown, z=yaxis_dropdown);

display(canvas_one)
