# Reflection

For this milestone our group has successfully implemented a working skeleton of our proposed dashboard in R.

### App Overview

We have a map visualization that displays the count of mental health conditions by each state in the US. While our initial proposal stated that we would be working with the entire dataset including other countries, our EDA showed that the majority of the data was US data. Knowing this fact and the added ease of integration with the map visualization, we decided to narrow our dashboard focus to the US. 

We have two other charts at the moment that bring to life two questions that were asked in the survey. There are four different filtering options in the form of a drop down for state, a range slider for age, and two checkbox filters for gender and self-employed status. 

All four filters are used as callbacks for the two charts and one map. The age, gender and self-employed filters are also used as callbacks for the map.

### App Strengths and Limitations

At this stage, we believe what our dashboard does well is the simplicity of the visualizations. At a glance users are able to understand what is being shown quite clearly.


For future milestones, we aim to implement the following improvements to the dashboard:

-   Aesthetic changes to make the dashboard more visually pleasing, including improved layout and themes for the charts and filters.

-   Add content to the second tab if we find more useful visualizations to bring to life more anlaysis from the data

-   Update the map drop down to be a multi-selection dropdown.

-   Two way integration between map and some charts, ie when states are selected from the map, the chart use those selections as a filter.

-   Age slider - the exact range 18-75 appear to be a bit off, so we will play around with the styling of this in next milestone.
