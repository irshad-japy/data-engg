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


def getcanvas_one():
    canvas_one = widgets.Output()
    return canvas_one


def getcanvas_two():
    canvas_two = widgets.Output()
    return canvas_two


def getcanvas_three():
    canvas_three = widgets.Output()
    return canvas_three


canvas_one = getcanvas_one()
canvas_two = getcanvas_two()
canvas_three = getcanvas_three()


def get_dropdown1():
    value_stream_dropdown = al.ui.widget_selection.ComboBox(
        label='Select value stream: ', options=['bridge', 'rating'])
    return value_stream_dropdown


def get_dropdown2():
    value_stream_dropdown = al.ui.widget_selection.ComboBox(
        label='Select category: ', options=['april', 'june'])
    return value_stream_dropdown


def get_dropdown3():
    value_stream_dropdown = al.ui.widget_selection.ComboBox(
        label='Select csvfile: ', options=['april_abc.csv', 'april_bcd.csv'])
    return value_stream_dropdown


def get_dropdown4():
    value_stream_dropdown = al.ui.widget_selection.ComboBox(
        label='Select csvfile: ', options=['june_abc.csv', 'june_bcd.csv'])
    return value_stream_dropdown


def get_dropdown5():
    value_stream_dropdown = al.ui.widget_selection.ComboBox(
        label='Select csvfile: ', options=['def.csv', 'efg.csv'])
    return value_stream_dropdown


def get_dropdown6():
    value_stream_dropdown = al.ui.widget_selection.ComboBox(
        label='Select metric1-xaxis: ', options=['col1', 'col2'])
    return value_stream_dropdown


def get_dropdown7():
    value_stream_dropdown = al.ui.widget_selection.ComboBox(
        label='Select metric2-yaxis: ', options=['col3', 'col4'])
    return value_stream_dropdown


dropdown1 = get_dropdown1()
dropdown2 = get_dropdown2()
dropdown3 = get_dropdown3()
dropdown4 = get_dropdown4()
dropdown5 = get_dropdown5()
dropdown6 = get_dropdown6()
dropdown7 = get_dropdown7()

keepall = al.ui.checkbox(label='keep all', default_value=True)


def callback_function1(b):
    if dropdown1.value[0] == 'bridge':
        if not keepall.value:
            canvas_two.clear_output(wait=False)
        with canvas_two:
            print('1' * 30)
            display(dropdown2.show())
    else:
        if not keepall.value:
            canvas_two.clear_output(wait=False)
        if not keepall.value:
            canvas_three.clear_output(wait=False)
        with canvas_two:
            print('2' * 30)
            display(dropdown5.show())
            display(dropdown6.show())
            display(dropdown7.show())


def callback_function2(b):
    # if not keepall.value:
    #     canvas_two.clear_output(wait=False)
    with canvas_three:
        if not keepall.value:
            canvas_three.clear_output(wait=False)
        print(dropdown2.value)
        if len(dropdown2.value) != 0 and dropdown2.value[0] == 'april':
            # if not keepall.value:
            #     canvas_two.clear_output(wait=False)
            display(dropdown3.show())
            display(dropdown6.show())
            display(dropdown7.show())
        elif len(dropdown2.value) != 0 and dropdown2.value[0] == 'june':
            # if not keepall.value:
            #     canvas_two.clear_output(wait=False)
            display(dropdown4.show())
            display(dropdown6.show())
            display(dropdown7.show())


def callback_function3(b):
    with canvas_one:
        print('4' * 30)
        display(dropdown4.show())


dropdown1.add_observer(callback_function1, names='value')
dropdown2.add_observer(callback_function2, names='value')
# dropdown3.add_observer(callback_function3, names='value')

display(dropdown1.show())
display(canvas_one)
display(canvas_two)
display(canvas_three)
display(keepall.show())
