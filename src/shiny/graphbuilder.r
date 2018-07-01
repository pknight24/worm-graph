library(ggnet)
library(network)
library(sna)
library(ggplot2)
library(dplyr)

df <- read.csv("adjacency_matrix.csv")

build.graph <- function(regex.vec, data = df)
{
  names <- data$X
  matches = c()
  for (reg in regex.vec)
  {
    matches <- c(matches, grep(reg, names, perl = TRUE, value = TRUE))
  }
  matches <- unique(matches)
  filtered.df <- filter(data, X %in% matches) %>% select(matches)
  filtered.df$Neuron <- matches
  net <- network(filtered.df)
  network.vertex.names(net) <- matches
  net
  
}

show.graph <- function(n)
{
  ggnet2(n, color = "blue", size = 1, label = TRUE, label.size = 2, alpha = 0.75)
}

