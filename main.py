import streamlit
import pandas

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

###
# streamlit.set_page_config(layout="wide")
streamlit.title("Deteksi Dini Status Risiko Diabetes")
streamlit.write("Posbindu Masjid Al Amin Mejing Kidul")
###

## Title
streamlit.write("Mohon isi data sesuai dengan petunjuk yang disediakan.")
##

### BUILD MODEL WITH "SIX (6)" INDEPENDENT VARIABLE BASED ON mRMR METHOD
## Read CSV & Define Feature
df = pandas.read_csv('https://raw.githubusercontent.com/danisnurman/psbnd2/main/diabetes_binary_5050split_health_indicators_BRFSS2015.csv')
# streamlit.dataframe(df, use_container_width=True)
#

feature_cols = ['Diabetes_binary', 'HighChol', 'HighBP', 'BMI', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Age']
df = df[feature_cols]

## Data Discretization & Transformation
for index in range(df.shape[0]):
    if df.loc[index,'BMI'] < 18.5:
        df.loc[index,'BMI'] = 1
    elif (df.loc[index,'BMI'] >= 18.5) & (df.loc[index,'BMI'] <= 24.9):
        df.loc[index,'BMI'] = 2
    elif (df.loc[index,'BMI'] >= 25.0) & (df.loc[index,'BMI'] <= 29.9):
        df.loc[index,'BMI'] = 3
    elif (df.loc[index,'BMI'] >= 30.0) & (df.loc[index,'BMI'] <= 100.0):
        df.loc[index,'BMI'] = 4
    else:
        df.loc[index,'BMI'] = 1000

df['Diabetes_binary'] = df['Diabetes_binary'].astype('int64')
df['HighChol'] = df['HighChol'].astype('int64')
df['HighBP'] = df['HighBP'].astype('int64')
df['BMI'] = df['BMI'].astype('int64')
df['Stroke'] = df['Stroke'].astype('int64')
df['HeartDiseaseorAttack'] = df['HeartDiseaseorAttack'].astype('int64')
df['PhysActivity'] = df['PhysActivity'].astype('int64')
df['Age'] = df['Age'].astype('int64')

## Split the data
X = df.drop(columns=['Diabetes_binary'])
y = df.Diabetes_binary

## Predictions
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## Classifier
clf = DecisionTreeClassifier()

## Perform training
clf = clf.fit(X_train, y_train)

## Predict result from dataset
y_pred = clf.predict(X_test)

## Calculate the accuracy score
acc_score = round((accuracy_score(y_test, y_pred)*100),2)
streamlit.write("")
streamlit.write("Model Accuracy : ", acc_score, "%")
streamlit.write("")

### GET VARIABLE INPUT FROM USER

## High Chol
streamlit.write("1. Apakah Anda dinyatakan mengalami kolesterol tinggi oleh petugas Posbindu?")
cholCat = streamlit.number_input(label="Jawaban (0=tidak, 1=ya)", min_value=0, max_value=1, key=1)
def showCholStatus(cholCat):
    if (cholCat == 0):
        cholStatus = "Normal"
    elif (cholCat == 1):
        cholStatus = "Tinggi"
    else:
        cholStatus = "ERROR!"
    return cholStatus
cholStatus = showCholStatus(cholCat)
streamlit.write("Status kolesterol: ", cholStatus)

# # Chol Status Function
# def checkCholStatus(cholesterol):
#     if(cholesterol>=50.0 and cholesterol<=200):
#         cholStatus = "Normal"
#         cholCat = 0
#     else:
#         cholStatus = "Tinggi"
#         cholCat = 1
#     return cholStatus, cholCat
# #

# cholStatus, cholCat = checkCholStatus(cholesterol)
# streamlit.write("Status kolesterol: ", cholStatus)
# streamlit.write("Kategori kolesterol: ", cholCat)
## End of High Chol

streamlit.write("")

## High Blood Pressure
streamlit.write("2. Apakah Anda dinyatakan mengalami tekanan darah tinggi oleh petugas Posbindu?")
bloodPressure = streamlit.number_input(label="Jawaban (0=tidak, 1=ya)", min_value=0, max_value=1, key=2)
def showBPStatus(bloodPressure):
    if(bloodPressure == 0):
        bpStatus = "Normal"
    elif(bloodPressure == 1):
        bpStatus = "Tinggi"
    else:
        bpStatus = "ERROR!"
    return bpStatus
bpStatus = showBPStatus(bloodPressure)
streamlit.write("Status tekanan darah: ", bpStatus)
## End of High Blood Pressure

streamlit.write("")

### BMI
# User Input
streamlit.write("3. Apa status Indeks Massa Tubuh (IMT) Anda berdasarkan pemeriksaan oleh petugas Posbindu?")
bmiCategory = streamlit.number_input(label="Jawaban (skala: 1 = Berat badan kurang, 2 = Normal, 3 = Kegemukan, 4 = Obesitas)", min_value=1, max_value=4, key=3)

## // BMI Counting Function
# weight = streamlit.number_input(label="Mohon masukkan hasil pengukuran berat badan (dalam kg)", min_value=10.0, max_value=200.0, step=.1, format="%0.1f", key=31)
# height = streamlit.number_input(label="Mohon masukkan hasil pengukuran tinggi badan (dalam cm)", min_value=10.0, max_value=200.0, step=.1, format="%0.1f", key=32)
# bmi = weight / ((height/100)*(height/100))
# bmi = round(bmi, 1)
#

## BMI Status Function
# def checkBMIStatus(bmi):
#     if(bmi>=10.0 and bmi<18.5):
#         bmiStatus = "Berat badan kurang"
#         bmiCat = 1
#     elif(bmi>=18.5 and bmi<=24.9):
#         bmiStatus = "Normal"
#         bmiCat = 2
#     elif(bmi>=25.0 and bmi<=29.9):
#         bmiStatus = "Kegemukan"
#         bmiCat = 3
#     elif(bmi>=30.0 and bmi<=34.9):
#         bmiStatus = "Obesitas"
#         bmiCat = 4
#     elif(bmi>=35.0 and bmi<=100.0):
#         bmiStatus = "Obesitas berat"
#         bmiCat = 5
#     else:
#         bmiStatus = ""
#         bmiCat = 0
#     return bmiStatus, bmiCat
#
# bmiStatus, bmiCat = checkBMIStatus(bmi)
## Dont show BMI if above 100
# if(bmi<100):
#     streamlit.write("IMT anda: ", bmi)
#     streamlit.write("Status IMT: ", bmiStatus)
# else:
#     streamlit.write("IMT anda:")
# // End of BMI Counting Function

## BMI Category Function
def checkBMIStatus(bmi):
    if(bmi == 1):
        bmiStatus = "Berat badan kurang"
    elif(bmi == 2):
        bmiStatus = "Normal"
    elif(bmi == 3):
        bmiStatus = "Kegemukan"
    elif(bmi == 4):
        bmiStatus = "Obesitas"
    else:
        bmiStatus = "ERROR!"
    return bmiStatus
bmiStatus = checkBMIStatus(bmiCategory)
streamlit.write("Kategori IMT: ", bmiStatus)
## End of BMI Category Function
### End of BMI

streamlit.write("")

## Stroke
streamlit.write("4. Apakah anda pernah mengalami stroke?")
stroke = streamlit.number_input(label="Jawaban (0=tidak, 1=ya)", min_value=0, max_value=1, key=4)
def showStrokeStatus(stroke):
    if(stroke == 0):
        strokeStatus = "Negative Stroke"
    elif(stroke == 1):
        strokeStatus = "Positive Stroke"
    else:
        strokeStatus = "ERROR!"
    return strokeStatus
strokeStatus = showStrokeStatus(stroke)
streamlit.write("Status tekanan darah: ", strokeStatus)
## End of Stroke

streamlit.write("")

## Heart Disease or Attack
streamlit.write("5. Apakah anda memiliki penyakit jantung koroner (PJK) atau infark miokard (MI)?")
heartDiseaseorAttack = streamlit.number_input(label="Jawaban (0=tidak, 1=ya)", min_value=0, max_value=1, key=5)
def showHDStatus(heartDiseaseorAttack):
    if(heartDiseaseorAttack == 0):
        hdStatus = "Negative Heart Disease or Attack"
    elif(heartDiseaseorAttack == 1):
        hdStatus = "Positive Heart Disease or Attack"
    else:
        hdStatus = "ERROR!"
    return hdStatus
hdStatus = showHDStatus(heartDiseaseorAttack)
streamlit.write("Status penyakit jantung: ", hdStatus)
## End of Heart Disease or Attack

streamlit.write("")

## Physical Activity
streamlit.write("6. Apakah anda melakukan aktivitas fisik atau olahraga selama 30 hari terakhir selain dari pekerjaan rutin anda?")
physAct = streamlit.number_input(label="Jawaban (0=tidak, 1=ya)", min_value=0, max_value=1, key=6)
def showPhysActStatus(physAct):
    if(physAct == 0):
        physActStatus = "Tidak"
    elif(physAct == 1):
        physActStatus = "Ya"
    else:
        physActStatus = "ERROR!"
    return physActStatus
physActStatus = showPhysActStatus(physAct)
streamlit.write("Aktivitas Fisik: ", physActStatus)
## End of Physical Activity

streamlit.write("")

## Age Categorization
streamlit.write("7. Berapa kategori usia Anda?")
# age = streamlit.number_input(label="Jawaban (scale 18-120)", min_value=18, max_value=120, step=1, key=7)
ageCat = streamlit.number_input(label="Jawaban (scale 1-14)", min_value=1, max_value=14, step=1, key=7)
def showAgeCategory(ageCat):
    if(ageCat == 1):
        ageCategory = "(1) 18-24 tahun"
    elif(ageCat == 2):
        ageCategory = "(2) 25-29 tahun"
    elif(ageCat == 3):
        ageCategory = "(3) 30-34 tahun"
    elif(ageCat == 4):
        ageCategory = "(4) 35-39 tahun"
    elif(ageCat == 5):
        ageCategory = "(5) 40-44 tahun"
    elif(ageCat == 6):
        ageCategory = "(6) 45-49 tahun"
    elif(ageCat == 7):
        ageCategory = "(7) 50-54 tahun"
    elif(ageCat == 8):
        ageCategory = "(8) 55-59 tahun"
    elif(ageCat == 9):
        ageCategory = "(9) 60-64 tahun"
    elif(ageCat == 10):
        ageCategory = "(10) 65-69 tahun"
    elif(ageCat == 11):
        ageCategory = "(11) 70-74 tahun"
    elif(ageCat == 12):
        ageCategory = "(12) 75-79 tahun"
    elif(ageCat == 13):
        ageCategory = "(13) 80 tahun atau lebih"
    else:
        ageCategory = "(14) Tidak tahu/menolak untuk menjawab"
    return ageCategory
ageCategory = showAgeCategory(ageCat)
streamlit.write("Kategori usia: ", ageCategory)
## End of Age Categorization

streamlit.write("")

### End of GET VARIABLE INPUT FROM USER

## POST Data
dataFromUser = [[generalHealth, bloodPressure, bmiCategory, cholCat, ageCat, physAct]]
# streamlit.write(dataFromUser)

## Predict New Data
result = clf.predict(dataFromUser)

## Check Diabetes Risk
if(result==0):
    streamlit.write("Status Diabetes: Tidak Berisiko.")
elif(result==1):
    streamlit.write("Status Diabetes: BERISIKO!")
else:
    streamlit.write("Error!")
###