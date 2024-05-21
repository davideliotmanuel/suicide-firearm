# Load necessary libraries
library(dplyr)
library(effectsize)

# Create the dataset
data <- data.frame(
  State = c("Montana", "South Dakota", "Alaska", "Wyoming", "Idaho", "New Mexico", "Colorado", "Kansas", "Utah", "Oklahoma", "North Dakota", "Nevada", "Nebraska", "Arizona", "Oregon", "Washington", "Iowa", "Indiana", "South Carolina", "Kentucky", "Missouri", "Arkansas", "Georgia", "Virginia", "Texas", "Maine", "Tennessee", "Hawaii", "Louisiana", "North Carolina", "Minnesota", "Wisconsin", "West Virginia", "Ohio", "Michigan", "New Hampshire", "Mississippi", "Alabama", "Illinois", "Florida", "Pennsylvania", "Maryland", "California", "Connecticut", "Massachusetts", "New Jersey", "New York", "Delaware", "Rhode Island", "Vermont"),
  CrudeRate = c(30.2, 27.2, 26.1, 21.4, 17.8, 16.4, 15.8, 14.7, 14.6, 13.7, 13.1, 12.6, 11.6, 11.6, 11.2, 11, 10.9, 10.8, 10.6, 10.3, 10.3, 10.1, 10.1, 10, 9.9, 9.2, 9.2, 9.2, 9.2, 9, 9, 8.7, 8.7, 8.6, 8.6, 8.2, 8, 7.9, 7.6, 7.5, 7.4, 7.3, 5.5, 4.9, 4.8, 4.4, 4.2, NA, NA, NA)
)

# Categorize states by gun control laws
states_with_gun_control <- c("California", "Colorado", "Connecticut", "Delaware", "Hawaii", "Illinois", "Massachusetts", "Maryland", "Maine", "Minnesota", "New Jersey", "New York", "North Carolina", "Rhode Island", "Texas", "Virginia", "Vermont", "Washington", "Wisconsin")
data <- data %>%
  mutate(GunControlLaw = ifelse(State %in% states_with_gun_control, 1, 0))

# Separate the data into two groups based on gun control laws
with_gun_control <- filter(data, GunControlLaw == 1)$CrudeRate
without_gun_control <- filter(data, GunControlLaw == 0)$CrudeRate

# Calculate means
mean_with_gun_control <- mean(with_gun_control, na.rm = TRUE)
mean_without_gun_control <- mean(without_gun_control, na.rm = TRUE)

# Perform t-test
t_test_result <- t.test(with_gun_control, without_gun_control)

# Calculate effect size (Cohen's d) using effectsize package
cohen_d_result <- cohens_d(with_gun_control, without_gun_control)

# Print the results
cat("Mean Suicide Rate (per 100,000) for States with Gun Control Laws:\n")
print(mean_with_gun_control)
cat("\nMean Suicide Rate (per 100,000) for States without Gun Control Laws:\n")
print(mean_without_gun_control)
cat("T-test Results:\n")
print(t_test_result)
cat("\nEffect Size (Cohen's d):\n")
print(cohen_d_result)
