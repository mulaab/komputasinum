require(lsr)
emphColLight <- rgb(.5,.5,1)
emphCol <- rgb(0,0,1)

means <- vector()
cilow <- vector()
cihigh <- vector()
N <- 50
nn <- 25
for( i in 1:N ) {
  x <- rnorm(nn,100,15)
  means[i] <- mean(x)
  ci <- ciMean(x)
  cilow[i] <- ci[1]
  cihigh[i] <- ci[2]
}


