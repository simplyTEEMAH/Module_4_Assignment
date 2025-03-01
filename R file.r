library(ggplot2)
netflix_data <- read.csv("netflix_data.csv")
#use ggplot2 to visualise the most watched genre
print(ggplot(netflix_data, aes(x = type, fill = type)) + 
        geom_bar() +
        theme_minimal() +
        ggtitle("Most Watched Genre"))
