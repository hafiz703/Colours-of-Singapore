library(data.table)
library(rgl)
#colors <- read.csv("average.csv", stringsAsFactors = F) 
#colors <- read.csv("Flickr/Mode/averageMode.csv", stringsAsFactors = F) 
#colors <- read.csv("Flickr/noGrey/averageNoGrey.csv", stringsAsFactors = F) 
colors <- read.csv("Flickr/100x100/average-max-100x100.csv", stringsAsFactors = F) 
#colors <- read.csv("colors.csv", stringsAsFactors = F)

dtColors <- setDT(colors)

dtColors <- dtColors[R != 'NA',,]
dtColors <- dtColors[R != '0' & G != '0' & B != '0',,]

#clusters <- kmeans(dtColors[,1:3],8)
#clusters <- kmeans(dtColors[,1:3],12,algorithm="Lloyd",iter.max = 100)
#clusters <- kmeans(dtColors[,1:3],12,algorithm="MacQueen",iter.max = 70)

dtColors$cluster <- as.factor(clusters$cluster)
plot3d(dtColors[,1:3], col=dtColors$cluster, main="k-means clusters")

## tabulate the avg R,G and B for eachh cluster
Colors.clusterAvg <- dtColors[,list(R.avg = mean(R),G.avg = mean(G),B.avg = mean(B)),by=cluster,]
Colors.clusterAvg <- Colors.clusterAvg[,hexColor := rgb(Colors.clusterAvg[,R.avg], Colors.clusterAvg[,G.avg], Colors.clusterAvg[,B.avg], maxColorValue=255),]

#avgColorPerHex <- dtColors[ ,list(R.avg = mean(R),G.avg = mean(G),B.avg = mean(B)),by=.(Lat,Lon)]
#avgColorPerHex <- avgColorPerHex[,avgHexColor := rgb(avgColorPerHex[,R.avg], avgColorPerHex[,G.avg], avgColorPerHex[,B.avg], maxColorValue=255),]

#function to get mode
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

#function to get mode
getCluster <- function(hue) {
  if (hue > 11/12.0 || hue <= 1/12.0) {
    return('Red')
  } else if (hue > 1/12.0 && hue <= 3/12.0) {
    return('Yellow')
  } else if (hue > 3/12.0 && hue <= 5/12.0) {
    return('Green')
  } else if (hue > 5/12.0 && hue <= 7/12.0) {
    return('Cyan')
  } else if (hue > 7/12.0 && hue <= 9/12.0) {
    return('Blue')
  } else {
    return('Magenta')
  }
}


#clusterColors <- dtColors[ ,list(cluster = getmode(cluster)),by=.(Lat,Lon)]
#clusterColors <- merge(clusterColors, Colors.clusterAvg, by = "cluster")
#clusterColors <- clusterColors[,list(cluster,Lat,Lon,hexColor),]

#fwrite(clusterColors, "hexWith100x100Clusters.csv")

#fwrite(dtColors, "colorsMode.csv")
#fwrite(Colors.clusterAvg, "clusterMode.csv")
#fwrite(avgColorPerHex, "avgColorPerHex.csv")

# convert RGB to HSV and transpose matrix to get H,S and V as columns 
test <- t(rgb2hsv(dtColors[,R], dtColors[,G], dtColors[,B], maxColorValue = 255))
test <- data.table(test)
test <- test[,cluster := getCluster(h),]
#test <- test[,list(h,s,v,cluster = getCluster(h)),]

## can verify avg with summary
summary(dtColors[cluster == 1,,])
summary(avgColorPerHex$avgHexColor)

library(plotly)
library(dplyr)

p <- plot_ly(data = dtColors,x = ~R, y = ~G, z = ~B, type = "scatter3d", mode = "markers", color = ~cluster, text = ~paste("R: ", R, '<br>G:', G, '<br>B:', B), hoverinfo = "text") %>%      layout(title = "3D Scatter plot of mode colors of hex of Singapore using Flickr photos",            scene = list(xaxis = list(title = "Red",range = c(0,255)),yaxis = list(title = "Green",range = c(0,255)),zaxis = list(title = "Blue",range = c(0,255))))
p

#p1 <- plot_ly(data = dtColors,x = ~Lon, y = ~Lat, z = ~cluster, type = "scatter3d", mode = "markers", color = ~cluster, text = ~paste("R: ", R, '<br>G:', G, '<br>B:', B), hoverinfo = "text") %>%      layout(title = "3D Scatter plot of average colors of hex of Singapore using Flickr photos",            scene = list(xaxis = list(title = "Lon"),yaxis = list(title = "Lat"),zaxis = list(title = "Cluster")))
#p1