from django.shortcuts import render

from joblib import load
model = load('./savedmodels/model.joblib')

# Create your views here.
def predictor(request):
    return render(request, 'index.html')

def forminfo(request):
    sub_metering_1 = request.GET['sub_metering_1']
    sub_metering_2 = request.GET['sub_metering_2']
    sub_metering_3 = request.GET['sub_metering_3']
    #day = request.GET['day']
    #month = request.GET['month']
    date = request.GET['date']
    day = (date[-2:])
    month = (date[-4:-3])
    #hour = request.GET['hour']
    #minute = request.GET['minute']
    time = request.GET['time']
    hour = time[1:2]
    minute = time[3:]
    rf_pred = model.predict([[sub_metering_1, sub_metering_2, sub_metering_3, day, month, hour, minute],])
    final = rf_pred[0].round(3)
    return render(request, 'result.html', {'result' : final})