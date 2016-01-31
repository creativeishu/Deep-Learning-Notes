# Mulilayer Neural Networks

A ** deep neural network** is described by a number of *layers* and *units* in each of these layers.
In a typical neural network, we have 
- Input layer
- Output layer
- A number of hidden layers.

The number units in input layer is equal to the dimension of the training data examples, and there is a unit in output layer corresponding to each output category. For a simple binary classification network, the number of units in output is 2, and for a regression network it is one.

## Linear Regression network
Consider the simples neural network, one which implements the linear regression model. In such network, there is no hidden layer, only input and output layers.
Consider the data which is is $3-$dimensional, i.e. each training example is a vector with 3-components. 
```
x = (x1, x2, x3)
```
and the target variable takes numerical floating values. 
Recall that the linear model is given by -
Y = AX + b