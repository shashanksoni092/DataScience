                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              m ##### Normality Test##################
#Hypothesis Testing
```{r}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
library(readxl)

######## Promotion.xlsx data ###################

Promotion <- read_excel(file.choose())    # Promotion.xlsx
Promotion1 <- Promotion[0:250,4:5]

attach(Promotion)
`Type of promotion`
attach(Promotion1)
colnames(Promotion1) <- c("InterestRateWaiver","StandardPromotion")
# Changing column names
View(Promotion1)
attach(Promotion1)

#############Normality test###############

shapiro.test(InterestRateWaiver)
qqnorm(InterestRateWaiver)
# p-value = 0.2246 >0.05 so p high null fly => It follows normal distribution

shapiro.test(StandardPromotion)
qqnorm(StandardPromotion)
# p-value = 0.1916 >0.05 so p high null fly => It follows normal distribution

#############Variance test###############

var.test(InterestRateWaiver,StandardPromotion)#variance test
# p-value = 0.653 > 0.05 so p high null fly => Equal variances

############2 sample T Test ##################

t.test(InterestRateWaiver,StandardPromotion,alternative = "two.sided",conf.level = 0.95,correct = TRUE)#two sample T.Test
# alternative = "two.sided" means we are checking for equal and unequal
# means
# null Hypothesis -> Equal means
# Alternate Hypothesis -> Unequal Hypothesis
# p-value = 0.02523 < 0.05 accept alternate Hypothesis 
# unequal means

t.test(InterestRateWaiver,StandardPromotion,alternative = "greater",var.equal = T)

# alternative = "greater means true difference is greater than 0
# Null Hypothesis -> (InterestRateWaiver-StandardPromotion) < 0
# Alternative Hypothesis -> (StandardPromotion - InterestRateWaiver) > 0
# p-value = 0.01211 < 0.05 => p low null go => accept alternate hypothesis
# InterestRateWaiver better promotion than StandardPromotion


###################Proportional T Test(RB data)##########

Johnytalkers <- read_excel(file.choose())   # JohnyTalkers.xlsx
View(Johnytalkers) 
attach(Johnytalkers)
table(Person)
table(Icecream)

table1 <- table(Icecream,Person)
table1
?prop.test
prop.test(x=c(58,152),n=c(480,740),conf.level = 0.95,alternative = "two.sided")
# two. sided -> means checking for equal proportions of Adults and children under purchased
# p-value = 6.261e-05 < 0.05 accept alternate hypothesis i.e.
# Unequal proportions 
 
# p-value = 0.999 >0.05 accept null hypothesis 
# so proportion of Children > proportion of children 
# Do not launch the ice cream shop


#########Chi Square(Bahaman Research)#################

Bahaman <- read_excel(file.choose()) # Bahaman.xlsx
View(Bahaman)
attach(Bahaman)
x<-table(Country,Defective)
x
?chisq.test
chisq.test(table(Country,Defective))
# p-value = 0.6315 > 0.05  => Accept null hypothesis
chisq.test(x)
# => All countries have equal proportions 

#############Anova (Contract_Renewal Data )##########

CRD <- read_excel(file.choose())   # ContractRenewal_Data(unstacked).xlsx
View(CRD)
Stacked_Data <- stack(CRD)
View(Stacked_Data)
attach(Stacked_Data)
Anova_results <- aov(values~ind,data = Stacked_Data)
summary(Anova_results)
# p-value = 0.104 > 0.05 accept null hypothesis 
# All Proportions all equal 


# Customer order form 
# Unstacked data 

cof<-read_excel(file.choose()) # customer_order(unstacked).xlsx
View(cof) # countries are in their own columns; so we need to stack the data 
stacked_cof<-stack(cof)
attach(stacked_cof)
View(stacked_cof)
table(stacked_cof$ind,stacked_cof$values)








shapiro.test(CRD$`Supplier C`)
qqnorm(CRD$`Supplier C`)
# p-value = 0.1916 >0.05 so p high null fly => It follows normal distribution

#############Variance test###############

var.test(CRD$`Supplier B`,CRD$`Supplier C`)#variance test
# p-value = 0.653 > 0.05 so p high null fly => Equal variances


```



