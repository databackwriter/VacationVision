#####keep R tidy#####
rm(list=ls()) #clear variables
cat("\014")  #clear console
#####################
library(tidyverse)

#####supproiting functions#####
model.linear.string <- function(m){
  # writes out the model string so we can place on plot area
  # inspired by: https://stackoverflow.com/questions/7549694/adding-regression-line-equation-and-r2-on-graph
  m.coef <- coef(m)
  m.sum <- summary(m)
  m.list <- list(a =format(m.coef[1], digits=2), 
                 b =format(m.coef[2], digits=2),
                 r2 = format(m.sum$r.squared, digits = 3))
  r <- substitute(italic(y) == a +b %.% italic(x)*","~~italic(r)^2~"="~r2, m.list)
  return (as.character(as.expression(r)))
}
model.linear.plot <- function(df,title,xlocal=x,ylocal=y, linecol="black",pointcol="brown",lablocal=""){
  # plots scatter graph, plus line of best fit (to fix double calculation of model)
  p<-ggplot(data=df, aes(x=xlocal,y=ylocal)) +
    geom_smooth(method="lm", color=linecol, size=1, formula = y~x) +
    geom_point(size=1,color=pointcol) +
    geom_text(x = min(x), y = min(y), label = lablocal, parse = TRUE) +
    ggtitle(title)
  return(p)
}
model.linear.plot.make <- function(model.local.df,model.local.title,model.local.pointcol){
  model.local.linear <- lm(y~x, data=model.local.df)
  model.local.linear.string <- model.linear.string(model.local.linear)
  model.local.linear.plot <- model.linear.plot(df=model.local.df,title=model.local.title,pointcol=model.local.pointcol,lablocal=model.local.linear.string)
  return (model.local.linear.plot)
}

#####data build#####
# inspired by https://tomaztsql.wordpress.com/2016/01/04/generating-sample-data-in-r/
x <- rnorm(1000,10,5)
y <- sapply(x, function(x) rnorm(1,2*x+6,10))
model.main.df <- data.frame(x,y)
model.training.indices <-sample(1000, 400)
model.training.train<-model.main.df[model.training.indices, ]
model.training.test<-model.main.df[-model.training.indices, ]

#####plot data#####
p.main <-model.linear.plot.make(model.main.df,"main set", "brown")
p.train<-model.linear.plot.make(model.training.train,"train set", "red")
p.test<-model.linear.plot.make(model.training.test,"test set", "brown")

print(p.train)


# indices <-sample(1000, 400)
# 
# train<-model.main.df[indices, ]
# test<-model.main.df[-indices, ]
# 
# 
# fplot(df=train,title="TRAINING SET",xlocal=train$x,ylocal=train$y,pointcol="red")
# fplot(df=test,title="TEST SET",xlocal=test$x,ylocal=test$y,pointcol="blue")
# 
# model <- lm(y~x, data=train)
# model








