# Final Project Proposal

**GitHub Repo URL**: **[https://github.com/CMU-IDS-2022/final-project-the-evaluators](https://github.com/CMU-IDS-2022/final-project-the-evaluators)**

## Team Name: The Evaluators 



* Jingyi (Jenny) Song
* Tadpol Rachatasumrit
* Princy Sasapara
* Urvish Thakker


---


## **Description**

**Domain**: University Course Evaluations

**Stakeholders**: Students, Course Instructors, Department Heads


## **Research Question**:



* How to equip students with all the required knowledge to make an informed decision while selecting university courses and planning their semester? 
* How to help them compare different courses based on different criterias like course goals, instructor’s feedback, student reviews, courseload etc?
* How to equip instructors and university department heads to easily view, analyze and understand the course quality, and criterias to improve?


## **Ideas：**



* Search and filter the courses.
* Compare courses.
    * Overall data visualization of the selected courses.
    * Head to head courses comparison.
    * The data can be compared by: _Hrs per week, Interest in student learning, clearly explain course requirements, clear learning objectives goals, instructor provides feedback to students to improve, explains subject matter of course, show respect for all students _
* Visualize the progress of each course through years. 
    * Many courses have been offered for many years, some of them are getting better score, some of them might get worse. By visualizing the progress of the course, we can see the trend of the course, and how well each professor does.



## **Data**

The data will be exported from CMU’s Faculty Course Evaluations (FCE) website.  

Link to FCE website: **[https://mwfo3.smartevals.com/Reporting/Students/Wizard.aspx?Type=Sections&FiveYearsOnly=True](https://mwfo3.smartevals.com/Reporting/Students/Wizard.aspx?Type=Sections&FiveYearsOnly=True)**

## **Data Exploration**



## **System Design and Visualizations**


<img width="517" alt="Screen Shot 2022-04-15 at 7 20 24 PM" src="https://user-images.githubusercontent.com/51781106/163651920-3aa0fe7b-fcf5-4fb3-a513-51d2c5e616d9.png">

### Compare Course Rating

The goal of these visualizations is to help users decide which courses to take among the courses they are interested in. There will be three components for this part:

1. Search Panel
   Users can search for the courses they want to compare in these visualizations.
2. Latest Year Compare - Compare only the latest year ratings of each course.
   * Type: Bar chart
   * Encoding:
      * x-axis: rating type
      * y-axis: rating value
      * color: course
   * Interaction:
      * Users can select the ratings they want to compare from the list aside from the graph.
3. Rating Over Time - Compare one rating over time.
   * Type: Line graph
   * Encoding:
      * x-axis: date
      * y-axis: rating value
      * color: course
      * line type: instructor
   *Interaction:
      * Users can select a rating they want to compare from the dropdown menu.

<img width="506" alt="Screen Shot 2022-04-15 at 7 37 42 PM" src="https://user-images.githubusercontent.com/51781106/163652788-160689f5-5bc0-4d13-9831-11a6b63f0aed.png">



### Course Rating vs Teacher Rating
These visualizations aim to give an overview of CMU course ratings. There will be 2 visualizations:

1. Overall Teacher Rate X Overall Course Rate 
   * Type: Scatter plot
   * Encoding:
      * x-axis: Overall Course Rating
      * y-axis: Overall Teacher Rating
      * color: Department
      * size: Hrs per week
      * circle: Course
    * Interaction:
      * Filter courses by department - users can filter to see only the list of departments they want by checking the checkboxes on the side.

2. Hrs. Per Week
   * Type: 1-axis scatter plot
   * Encoding:
      * x-axis: Hrs per week
      * color: department (same as the first visualization)
   * Interaction
      * Brush filter - users can brush the graph to filter only the range “hrs per week” they want to focus on. The filter will be applied to the first 
<img width="486" alt="Screen Shot 2022-04-15 at 7 38 17 PM" src="https://user-images.githubusercontent.com/51781106/163652791-bd509da3-fae9-4b4e-80bd-0fbd53e36af3.png">

3. Hrs per Week panel
This visualization will show the sum amount of “hrs per week of the selected courses”. The goal of this visualization is to show the commitment (hrs per week) they will have to give if they decide to register for all the selected courses. This visualization will be on the fixed panel so that the users will always see it.
   * Type: 1-axis bar chart.
   * Encoding:
      * x-axis: sum of “hrs per week”
      * color: Courses


<img width="347" alt="Screen Shot 2022-04-15 at 7 38 37 PM" src="https://user-images.githubusercontent.com/51781106/163653257-4bac3b44-940c-47c5-ad0e-4c5505aaae9a.png">




