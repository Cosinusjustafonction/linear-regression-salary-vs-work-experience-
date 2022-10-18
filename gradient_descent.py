import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Salary_Data.csv')

def loss_function(m , b , points) :
    totale_error = 0

    for i in range(len(points)) :
        x = points.iloc[i].YearsExperience
        y = points.iloc[i].Salary
        totale_error += (y - (m*x + b))**2
    totale_error / float(len(points))



def gradien_descent(m_now , b_now , points , L) :
    m_gradient = 0
    b_gradient = 0

    n = int(len(points)*80/100)

    for i in range(n) :

        x = points.iloc[i].YearsExperience
        y = points.iloc[i].Salary

        m_gradient += -(2/n)* (y - (m_now*x + b_now))*x
        b_gradient += -(2/n) * (y - (m_now*x + b_now))
    m = m_now - m_gradient * L
    b = b_now - b_gradient* L
    return m , b
m = 0
b = 0
L = 0.0001
epochs = 1000

for i in range(epochs) :
    m ,b  = gradien_descent(m , b , df , L)

print(m,b)
plt.scatter(df.YearsExperience , df.Salary,color='black')
plt.plot(list(range(0,10)), [m*x + b for x in range(0,10)], color='red')
plt.show()
def predict(yearsexperience) :
    return m*yearsexperience + b


a = 0
def curve(a,b) :
    return m*a+b
for i in range(int((len(df)*20)/100)) :
    x = df.iloc[i].Salary - predict(df.iloc[i].YearsExperience)
    a+=x

print((a/int(len(df)*20)))