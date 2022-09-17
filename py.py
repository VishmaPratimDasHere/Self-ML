from sklearn.datasets import load_iris

dataset = load_iris()

print(dataset)

print(dataset.target)

x=dataset.data
y=dataset.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y) # 
print(x_train, x_test, y_train, y_test)