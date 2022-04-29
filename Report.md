# Final Project Report

**Project URL**: [Streamlit Application](https://share.streamlit.io/cmu-ids-2022/final-project-the-evaluators/main/my_component/__init__.py)

**Video URL**: [Video Presentation](https://drive.google.com/file/d/1wZm0hQv7E3lZ9IOPLl0j1T_6UTphbapW/view?usp=sharing)

Short (~250 words) abstract of the concrete data science problem and how the solutions addresses the problem.

## Introduction

Selecting the right course and building an appt schedule is very critical for all students to get the best of the degrees. However, the decision about which course to take can not only be done based on the course syllabus and course content at times. The best way is to see what the past students who had taken the course had to say. Thus, course evaluations are really important for prospective students. The current Carnegie Mellon University’s official website to view course evaluations is smartevals.com. We found that the current website was very prosaic and it was just very difficult to visualize information. There were significant problems in the current state of the website which we observed. Lack of tools to compare two courses, moreover if a course is offered by two professors there is no way to validate which is the better professor. Moreover, sometimes the course may be offered by multiple departments but to compare which department might be better, it is very difficult in the current interface of the website. Motivated by these drawbacks of our current website and having experienced them ourselves, we decided to work on this problem and build a comprehensive solution to address these challenges.

## Related Work

There has not been much work done around it and comprehensive course evaluation websites being developed are still in their infancy. There have been websites like Smartevals, Stellic, Ratemyprofessor which have tried to address these issues. However, they are still in the phase of inception. There is data being collected and aggregated to build comprehensive solutions, however it will take a long way till it reaches a substantial phase. Sometimes, the data speaks for itself however we felt it would be great if students could visualize this information in some way. Researchers and students at universities such as Carnegie Mellon, Massachusetts Institute of Technology, University of California, Berkeley and others have worked on such projects in the past as well. We analyzed and studied some of the public github repositories to study this related work.

## Methods

In this project, we used multiple methods to work with the data, develop the applications, and create visualizations.

### Dataset

The dataset we used in this project is exported from CMU’s faculty course evaluation website in April 2022. The dataset contains the students’ course evaluation survey responses from Spring, 2011 to Spring, 2022 (12 years). There are **55,639** instances in total which come from 9 schools, 62 departments, and 4,039 instructors at CMU.

### Data Processing

Before developing the application, we explored the dataset and decided to perform some data processing to clean the dataset and remove outliers. The data processing include:

- Remove outliers, which is the instance that has more than 325 total students in the class. From the observation, we found that there are 2 instances that have a number of total students more than a thousand which is unusual and could make the visualizations difficult to read, therefore, we decided to remove those outliers.
- Remove the instances which have too few students and responses. We decided to remove the instances that have a number of total students less than 5, and a response rate lower than 40%. If the results come from only a few students, they might not accurately represent the real quality of the course. Therefore, we decided to clean these data to prevent the visualizations from misleading the users.

After the data processing, the total number of instances is 35,896 instances.

### Visualization Methods

- Streamlit & React (Jenny):
  - Since we design to have several pages, we used [Streamlit Component](https://github.com/streamlit/component-template/) to set up a REACT front end and developed a navigation bar to change page content. The rest of the code is written in Python backend.
- Altair
  - Altair is a declarative statistical visualization library for Python, based on Vega and Vega-Lite. Altair offers a powerful and concise visualization grammar that enables you to build a wide range of statistical visualizations quickly. Altair, helps build pretty looking interactive visualizations, which can be customized greatly.
- Pandas
  - Pandas is an open-source library designed to make it simple and natural to deal with relational or labeled data. It includes a number of data structures and methods for working with numerical data and time series. This library is based on the NumPy Python library. Pandas is quick and has a high level of performance and productivity for its users.
- Apart from the above main tools, we used other existing python libraries such as datetime, seaborn, pandas_datareader, seaborn among others. Also, we use tools such as Google Colab, Spyder and jupyter notebook for programming of our application.

## Results

### System & Visualizations

The application is split into 4 pages based on the use cases and objectives of the visualizations.

#### **1) Homepage**

The homepage is the first page that the users will face, therefore, the goal of this page is to give an overview and trends of the CMU’s courses. We first display the top 5 rated courses (Figure 1), departments, and instructors to the users. Also, the courses explorer visualization (Figure 2) is provided at the bottom to allow the users to explore the trend of the course based on 2 metrics (overall course rate, and overall teaching rate) by themselves.

![](images/homepage-toprated.png) |  ![](images/homepage-explorer.png)
:--------------------------------:|:-----------------------------------:
_Figure 1- Top 5 rated section_   |  _Figure 2 - Courses explorer visualization_


#### **2) Compare Courses**

The goal of the compare courses page is to help the users make the decision of what courses to take among the courses they are interested in. There are 2 main visualizations provided on this page.

The first one is the “Compare courses based on different metrics” (Figure 3) which will allow users to compare their selected courses based on multiple metrics. The example use case of this visualization is:

- _“I want to take a Data Science for Product Managers course. Should I take the one from Heinz or the one from HCII? Which one is better?”_

The other one is the “Compare courses over time” (Figure 4). This visualization will allow users to see the changes in the overall rating of the courses over time. The example use case of this visualization is:

- _“An alumni from 2018 said good things about a course. Have the ratings gone down from that point?”_


![](images/compare-compare.png) |  ![](images/compare-progress.png)
:------------------------------:|:---------------------------------:
_Figure 3 - Compare courses_    |  _Figure 4 - Compare courses over time_


#### **3) Compare Departments**

The goal of this page is to allow the users to compare between departments. Similar to the compare courses page, there will be 2 main visualizations on this page. One is to compare departments based on different metrics, and the other is to compare the overall course rate of the departments over time. The ratings of each department are calculated by finding the average of all courses in that department. The example use cases of this page are:

- _“I want to do the minor degree, which departments or schools should I select?”_
- _“I can select courses from many departments, which departments should I start looking at?”_

#### **4) Compare Instructors**

The last page is the compare instructors page. Similar to both compare courses and compare departments page, the goal of this page is to compare the ratings of the instructors. There are 2 visualizations on this page. The first is to compare instructors based on different metrics, and the second is to compare the overall teaching rate of the instructors over time. Same as the compare departments page, the ratings of each instructor are the average of all courses that each instructor teaches. The example use case of this page is:

- _“There are two sections of the data science course taught by different instructors, which instructor teaches better?”_

### User Testing

We conducted user tests with two CMU master students. Both of them know the existence of the faculty course evaluation website but seldom use it because they find it difficult to navigate the website. They strongly agree that there is a need for a new website to help them better understand and make use of the FCE data.

One participant has two similar courses on the waitlist and has been struggling with deciding which one to take, so this participant immediately went to the “compare courses” page and started to search for these two courses. From the first visualization, the participant quickly learned that course A has a higher rating for most of the metrics than course B. From the second visualization, the participant realized that the rating for course B was decreasing over the past few years because of an instructor change. As a result, the participant considered taking course A instead. This participant also mentioned that having an “import from waitlist” feature from the SIO system and providing course information for the incoming semester would be helpful for the students.

The other participant really liked the “explore more” section and discovered that a course that he wanted to take in the fall is among the courses that have the largest workload. The participant was surprised to see it and was considering a schedule change to accommodate the workload. The participant was also interested in comparing the courses and instructors he had in the past. He found that one instructor's rating was higher than what he expected. After checking the detailed information, he realized that the number of students’ responses was so low that the ratings could be biased. He appreciated that our website is showing this information which could inform users about potential errors and biases in the FCE data.

To conclude, both of the participants loved our ideas and agreed that our website would help CMU students to make more informed decisions on course selection.

## Discussion

With the current FCE dataset, searching through courses to find the ratings is a difficult task. SIO shows ratings for each course when user is planning their semester schedule, but there is there is no direct comparison of courses available.

With our app, users can easily compare ratings of courses that they’re interested in. Our app is useful to answer questions like -

    _“Should I take Data Science for Product Managers from Heinz, or from HCII?”_


    _“Are all my courses this semester intensive? What is the course load according to students?”_


    _“An alumni from 2018 said good things about a course. Have the ratings gone down from that point?”_

So to summarize our app allows users to play around selecting different features and criteria to see different courses, instructors, and department ratings, along with seeing the student perceived courseload/week to make decisions on what courses to take.

This is especially helpful when students need to choose between very similar courses, by different instructors in different departments.

## Future Work

We envision this app to become a one-stop-shop for course planning. By integrating this into the current course scheduling system used by CMU, we can add a very important feature - that is comparing the course quality and ratings based on criteria of interest - into their course planning.

To make this more useful, it can be extended to include course content comparison. This can be done when the course content data becomes steadily available. With course content comparison, users can not only compare ratings but also the overview of the course content to get information quickly for comparison, rather than searching up courses individually.
