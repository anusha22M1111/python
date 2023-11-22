#install.packages("dplyr")
library("dplyr")
dim(airquality)
str(airquality)
head(airquality)
x1=distinct(airquality)
x1
filter(airquality,Month == 9,Temp>90)
head(filter(airquality,!is.na(Ozone)),5)
arrange(airquality,Day,desc(Month))
mutate(airquality,temp_celsius=(Temp-32)*5/9)
head(select(airquality,Ozone,Day,Month),3)
summarise(airquality,max=max(Temp),min=min(Temp))
#pipe
airquality %>% group_by(Month) %>% filter(Month>4 & Month<8) %>% summarise(m=mean(Temp,na.rm=TRUE))

#example 1
glimpse(mtcars)
mtcars
sample(mtcars)
sample_frac(mtcars)
select(mtcars,mpg)
select(mtcars,starts_with("d"))
select(mtcars,mpg:disp,-cyl)
filter(mtcars,hp>125,mpg<15.0)
mutate(mtcars,nv=(wt+mpg))
summarise(mtcars,max=max(hp),min=min(hp))
mtcars%>%filter(hp>25)%>%arrange(mpg)
mtcars%>%filter(hp>25)%>%group_by(am)%>%summarise(avg=mean(wt))
