from django.shortcuts import render, redirect
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from .models import HousingData

def home(request):
    return render(request, 'home.html')

def predict(request):
    if (request.method == 'POST'):
        var1 = request.POST['Income']
        var2 = float(request.POST['Age'])
        var3 = float(request.POST['Rooms'])
        var4 = float(request.POST['Bedrooms'])
        var5 = float(request.POST['Population'])
        var6 = request.POST['Income1']
        var7 = float(request.POST['Age1'])
        var8 = float(request.POST['Rooms1'])
        var9 = float(request.POST['Bedrooms1'])
        var10 = float(request.POST['Population1'])
        df = pd.DataFrame(list(HousingData.objects.values('id', 'LotArea', 'MasVnrArea', 'BsmtUnfSF', 'TotalBsmtSF', 'FstFlrSF', 'SndFlrSF', 'GrLivArea', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'SalePrice')))
        df.set_index('id', inplace = True)
        df.dropna(inplace = True)
        df['MasVnrArea'] = pd.to_numeric(df['MasVnrArea'], errors = 'coerce')
        df['MasVnrArea'] = df['MasVnrArea'].astype('int64')
        X_var = df[['LotArea', 'MasVnrArea', 'BsmtUnfSF', 'TotalBsmtSF', 'FstFlrSF', 'SndFlrSF', 'GrLivArea', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF']].values
        y_var = df['SalePrice'].values
        X_train, X_test, Y_train, Y_test = train_test_split(X_var, y_var, test_size = 0.2, random_state = 0)
        ols = LinearRegression()
        ols.fit(X_train, Y_train)
        ols_yhat = ols.predict(np.array([var1, var2, var3, var4, var5, var6, var7, var8, var9, var10]).reshape(1, -1))
        request.session['_old_post'] = int(ols_yhat[0])
        return redirect('prediction')
    else:
        return render(request, 'predict.html')

def prediction(request):
    old_post = request.session.get('_old_post')
    context = {
        'predict_num' : old_post
    }
    return render(request, 'prediction.html', context)