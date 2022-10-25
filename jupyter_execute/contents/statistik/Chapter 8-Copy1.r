fWeights <- read.csv("femaleMiceWeights.csv")
head(fWeights) 

plot(0:10, 0:10, type = "n", axes = FALSE, xlab = "", ylab = "")
symbols(x = c(2.5, 2.5, 2.5) , y = c(7.5, 7.5, 7.5), circles = c(1, 2, 3) ,add = TRUE)
symbols(x = c(7.5, 7.5, 7.5) , y = c(7.5, 7.5, 7.5), circles = c(1, 2, 3) ,add = TRUE)
symbols(x = c(2.5, 2.5, 2.5) , y = c(2.5, 2.5, 2.5), circles = c(1, 2, 3) ,add = TRUE)
symbols(x = c(7.5,7.5, 7.5) , y = c(2.5,2.5,2.5), circles = c(1,2,3) ,add = TRUE)
points(x=c(2.4, 2.6, 2.3, 2.5, 2.7, 2.4, 2.6), 
       y=c(7.3, 7.3, 7.5, 7.5, 7.5, 7.7, 7.7), pch = 19)
points(x=c(7.9, 8.1, 7.8, 8, 8.2, 7.9, 8.1) , 
       y=c(8.3, 8.3, 8.5, 8.5, 8.5, 8.7, 8.7), pch = 19)
points(x=c(1.4, 3.6, 2.3, 1.5, 2.7, 2.4, 3.6), 
       y=c(2.2, 1.8, 3.1, 2.7, 2.5, 1.5, 3.2), pch = 19)
points(x=c(8, 8.5, 9.1, 8.2, 8.4, 8.6, 9) , 
       y=c(2.8, 2.1, 2.7, 2.9, 3.3, 3.1, 3.5), pch = 19)
text(2.5, 10, "Low Variance, Low Bias")
text(7.5, 10, "Low Variance, High Bias")
text(2.5, 5, "High Variance, Low Bias")
text(7.5, 5, "High Variance, High Bias")


f <- function(x){sqrt(2/(x - 1))*gamma(x/2)/gamma((x - 1)/2)}
p <- ggplot(data.frame(x = c(2, 50)), aes(x = x))
p + stat_function(fun = f) +
   labs(x = "n", y = expression(frac(sqrt(2)*phantom(0)*Gamma*
      bgroup("(",frac(n, 2),")"), sqrt(n - 1)*phantom(0)*Gamma*
      bgroup("(",frac(n - 1, 2),")")))) +
   geom_hline(yintercept = 1, lty = "dashed") +
   theme_bw()













