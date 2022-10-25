library("magrittr")
df <-  select(iris, Petal.Length, Species) %>% filter(Species == "setosa")
ggplot(data = df, aes(x = Petal.Length, fill = Species)) + geom_histogram(binwidth = 0.1) + geom_vline(aes(xintercept = 1.462, linetype = "mean"))  + geom_vline(aes(xintercept = 1.114672, linetype = "mean - 2sd")) + scale_linetype_manual(values = c(1, 10), name = "Sample stats") + xlab("Petal Length [cm]") + ylab("Count") + theme_ur


dattab <- trees %>%
  arrange(Height) %>%
  summarise(heights = list(Height))
kbl(dattab, col.names = c("Height [in]"), caption = "Observations of $m = 31$ felled black cherry trees.", booktabs = T) %>%
 kable_styling(latex_options = c("striped", "hold_position")) %>%
  column_spec(1, width = "150mm")



