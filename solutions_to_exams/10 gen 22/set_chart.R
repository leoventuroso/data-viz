library(UpSetR)

setwd('C://Users//ludov//data visualization//today exam')

df = read.csv(file = 'visits.csv')

upset(df, nintersects = 11, nsets = 9, order.by = 'freq',
      point.size = 3, line.size = 1)
