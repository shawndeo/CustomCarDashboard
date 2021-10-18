import streamlit as st
import pandas as pd
from sklearn import linear_model

st.title('Price a Custom Car')

data = pd.read_csv('BuildCar.csv')

st.warning("Please know that all of the data in the following data frame was manually collected from each vehicle manufacturer's site.")

st.header('Dataframe')

data = data[data['0-60 MPH'] > 0]
data = data[data['Engine Size (L)'] > 0]
data = data[data['HP'] > 0]

st.dataframe(data)

st.sidebar.title('Configurations')

select_body = st.sidebar.selectbox('Body:',
                                    ('Coupe', 'Convertible', 'Gran Coupe', 'Pickup', 'Roadster', 'Sedan', 'SUV', 'Wagon'))

select_drivetrain = st.sidebar.radio('Drivetrain: ',
                                    ('2WD', 'AWD', 'FWD', 'Hybrid', 'RWD'))
st.sidebar.warning('The Drivetrain attribute currently does not affect the model.')

select_engine = st.sidebar.selectbox('Engine:',
                                    ('Boxer 6', 'I4', 'I6', 'V6', 'V8', 'V12'))
st.sidebar.warning('The Engine attribute currently does not affect the model.')
select_060 = st.sidebar.slider('0-60 MPH Speed', 2.6, 7.1)
st.sidebar.info('Please note that a lower selection in 0-60 MPH Speed means that the car accelerates faster.')

select_engine_size = st.sidebar.slider('Engine Size', 1.5, 6.6)
select_hp = st.sidebar.number_input('Horsepower', 150, 807)
#st.sidebar.selectbox('Manufacturer Origin', ('Germany', 'Italy', 'Japan', 'USA'))

bodyCoupe = 0
bodyConvertible = 0
bodyGranCoupe = 0
bodyPickup = 0
bodyRoadster = 0
bodySedan = 0
bodySUV = 0
bodyWagon = 0

if select_body == 'Coupe':
    bodyCoupe = 1
elif select_body == 'Convertible':
    bodyConvertible = 1
elif select_body == 'Gran Coupe':
    bodyGranCoupe = 1
elif select_body == 'Pickup':
    bodyPickup = 1
elif select_body == 'Roadster':
    bodyRoadster = 1
elif select_body == 'Sedan':
    bodySedan = 1
elif select_body == 'SUV':
    bodySUV = 1
elif select_body == 'Wagon':
    bodyWagon = 1

st.header('Body Style')
st.write(f"""
bodyCoupe: {bodyCoupe} \n
bodyConvertible: {bodyConvertible} \n
bodyGranCoupe: {bodyGranCoupe} \n
bodyPickup: {bodyPickup} \n
bodyRoadster: {bodyRoadster} \n
bodySedan: {bodySedan} \n
bodySUV: {bodySUV} \n
bodyWagon: {bodyWagon}
""")

drivetrain2WD = 0
drivetrainAWD = 0
drivetrainFWD = 0
drivetrainHybrid = 0
drivetrainRWD = 0

if select_drivetrain == '2WD':
    drivetrain2WD = 1
elif select_drivetrain == 'AWD':
    drivetrainAWD = 1
elif select_drivetrain == 'FWD':
    drivetrainFWD = 1
elif select_drivetrain == 'Hybrid':
    drivetrainHybrid = 1
elif select_drivetrain == 'RWD':
    drivetrainRWD = 1


st.header('Drivetrain')
st.write(f"""
2WD: {drivetrain2WD} \n
AWD: {drivetrainAWD} \n
FWD: {drivetrainFWD} \n
Hybrid: {drivetrainHybrid} \n
RWD: {drivetrainRWD}
""")

st.header('0-60 MPH Speed:')
st.write(select_060)

st.header('Engine Size:')
st.write(select_engine_size)

st.header('Horsepower:')
st.write(select_hp)

reg = linear_model.LinearRegression()
reg.fit(data[['BodyCoupe', 'BodyConvertible', 'BodyGranCoupe', 'BodyPickup', 'BodyRoadster', 'BodySedan', 'BodySUV', 'BodyWagon',
                '0-60 MPH', 'Engine Size (L)', 'HP']], data['StartingMSRP'])

st.header('Coefficients:')
reg.coef_
st.write("""
00: Coupe \n
01: Convertible \n
02: GranCoupe \n
03: Pickup \n
04: Roadster \n
05: Sedan \n
06: SUV \n
07: Wagon \n
08: 0-60 Acceleration Speed \n
09: Engine Size (L) \n
10: Horsepower
""")

st.header('Intercept:')
reg.intercept_

st.header('Prediction:')
pred = reg.predict([[bodyCoupe, bodyConvertible, bodyGranCoupe, bodyPickup, bodyRoadster, bodySedan, bodySUV, bodyWagon, select_060, select_engine_size, select_hp]])
st.write(pred)

st.header('Notes')
st.write("""
 • 10/17/21 08:38PM: Not surprised that a vehicle being a Sedan, SUV or Wagon drops the price that much. I am surprised that Engine Size does seem to drop the price but maybe the data is skewed by the performance of cars with small 3L engines like the Porsches.
""")
