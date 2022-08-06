# Introduction

Chi-square tests of independence test whether two [qualitative variables](/blog/variable-types-and-examples/#qualitative) are independent, that is, whether there exists a relationship between two categorical variables. In other words, this test is used to determine whether the values of one of the 2 qualitative variables depend on the values of the other qualitative variable.

If the test shows no association between the two variables (i.e., the variables are independent), it means that knowing the value of one variable gives no information about the value of the other variable. On the contrary, if the test shows a relationship between the variables (i.e., the variables are dependent), it means that knowing the value of one variable provides information about the value of the other variable.

This article focuses on how to perform a Chi-square test of independence by hand and how to interpret the results with a concrete example. To learn how to do this test in R, read the article "[Chi-square test of independence in R](/blog/chi-square-test-of-independence-in-r/)".

# Hypotheses

The Chi-square test of independence is a [hypothesis test](/blog/hypothesis-test-by-hand/) so it has a null ($H_0$) and an alternative hypothesis ($H_1$):

* $H_0$ : the variables are independent, there is **no** relationship between the two categorical variables. Knowing the value of one variable does not help to predict the value of the other variable
* $H_1$ : the variables are dependent, there is a relationship between the two categorical variables. Knowing the value of one variable helps to predict the value of the other variable

# How the test works?

The Chi-square test of independence works by comparing the observed frequencies (so the frequencies observed in your sample) to the expected frequencies if there was no relationship between the two categorical variables (so the expected frequencies if the null hypothesis was true).

If the difference between the observed frequencies and the expected frequencies is **small**, we cannot reject the null hypothesis of independence and thus we cannot reject the fact that the two **variables are not related**. On the other hand, if the difference between the observed frequencies and the expected frequencies is **large**, we can reject the null hypothesis of independence and thus we can conclude that the two **variables are related**.

The threshold between a small and large difference is a value that comes from the Chi-square distribution (hence the name of the test). This value, referred as the critical value, depends on the significance level $\alpha$ (usually set equal to 5%) and on the degrees of freedom. This critical value can be found in the statistical table of the Chi-square distribution. More on this critical value and the degrees of freedom later in the article.

# Example

For our example, we want to determine whether there is a statistically significant association between smoking and being a professional athlete. Smoking can only be "yes" or "no" and being a professional athlete can only be "yes" or "no". The two variables of interest are qualitative variables so we need to use a Chi-square test of independence, and the data have been collected on 28 persons.

Note that we chose binary variables (binary variables = qualitative variables with two levels) for the sake of easiness, but the Chi-square test of independence can also be performed on qualitative variables with more than two levels. For instance, if the variable smoking had three levels: (i) non-smokers, (ii) moderate smokers and (iii) heavy smokers, the steps and the interpretation of the results of the test are similar than with two levels.

