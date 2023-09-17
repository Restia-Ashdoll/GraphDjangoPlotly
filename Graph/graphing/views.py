from django.shortcuts import render
import pandas as pd
import plotly.express as px
import numpy as np
from . import forms


# Create your views here.

def index(request):
    df = pd.read_csv("static/guardbandcore-6.csv")

    if request.method == 'POST':
        form = forms.ColumnSelectionForm(request.POST)
        if form.is_valid():
            selected_columns = form.cleaned_data['selected_columns']
            if len(selected_columns) >= 2:
                fig = px.line(df,y=df.columns[selected_columns[0:]])
                return render(request, "plot.html", {'fig' : fig.to_html()})
    else:
        form = forms.ColumnSelectionForm
    return render(request, "graphing/index.html", {"form" : form})

    # df = pd.read_csv("static/guardbandcore-6.csv")
    #
    # fig = px.line(df, y="CPU0 CORES CORE1 Voltage", title="Core Voltage", width=1700, height=900)
    # fig.write_html("static/pmlog.html")
    # return render(request, "graphing/index.html")


   # def select_columns(request):
   #     if request.method == 'POST':
   #         form = ColumnSelectionForm(request.POST)
   #         if form.is_valid():
   #             selected_columns = form.cleaned_data['selected_columns']
   #             if len(selected_columns) >= 2:
   #                 fig = px.line(df, x=df.columns[selected_columns[0]], y=df.columns[selected_columns[1:]])
   #                 return render(request, 'plot.html', {'fig': fig.to_html()})
   #     else:
   #         form = ColumnSelectionForm()
   #
   #     return render(request, 'select_columns.html', {'form': form})


