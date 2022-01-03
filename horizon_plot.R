# Horizon Chart

library(ggplot2) # for data frame
library(ggHoriPlot)


df = ggplot2::economics

df['date'] = lapply(df['date'], as.Date)

df = subset(df, select = c('date', 'psavert'))

fig <- ggplot(df) +
  geom_horizon(aes(date, psavert, fill = ..Cutpoints..)) +
  theme_void() +
  scale_fill_hcl() +
  ggtitle('Horizon plot') +
  labs(x=("Year"), y=("psavert")) +
  scale_colour_manual(values = date, labels=c(expression(italic('Ascidiella aspersa')), expression(italic('Ciona intestinalis')))) +
  theme_bw()



fig

