# Magic formula knn

train = read.csv("C:/Fintech/Training_Data.csv")
test = read.csv("C:/Fintech/Test_Data.csv")
head(test)
n_test = dim(test)[1]

set.seed(2022)
rows = sample(nrow(train))
train = train[rows,]
head(train)

train.x = train[,c("roc", "ey")]
test.x = test[,c("roc", "ey")]
train.y = train[,c("label")]
test.y = test[,c("label")]

s = seq(0,100,5)
s[1] = 1# To change the first element from 0 to 1. This is number of neighbours
accuracy = rep(0, length(s))
accuracy

## Start looping!!!
for (i in 1:length(s)){
	correct = 0
	knn.pred = knn(train.x, test.x, train.y, k=s[i])
	correct = correct + sum(knn.pred==test.y)
	accuracy[i] = correct/n_test
}

## Plot graph 1!
plot(s, accuracy, type='b')