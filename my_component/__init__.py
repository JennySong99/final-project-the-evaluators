import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "my_component",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("my_component", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def my_component(currPage):
    """Create a new instance of "my_component".

    Parameters
    ----------
    name: str
        The name of the thing we're saying hello to. The component will display
        the text "Hello, {name}!"
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(currPage=currPage)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/__init__.py`
if _RELEASE:
    import streamlit as st
    import pandas as pd
    import altair as alt
    import numpy as np
    from utils import get_course_df
    # from utils import get_instructor_df
    from utils import get_instructor_by_year_df
    from utils import get_instructor_all_year_df
    from utils import get_dept_df
    from utils import get_course_df2
    from utils import get_dept_df2
    from utils import get_dept_all_year_df
    from utils import options_map_to_columns

    # st.set_page_config(layout="wide")
    st.set_page_config(
     page_title="Course Explorer",
     page_icon="📚",
    )

    # ------------------------------------------------------- #
    # Data Preparation.
    # ------------------------------------------------------- #

    numeric_columns = [
        'hrs_per_week',
        'total_students',
        'responses',
        'response_rate',
        'interest_in_student_learning',
        'clearly_explain_course_requirements',
        'clear_learning_objectives_and_goals',
        'instructor_provides_feedback',
        'demonstrate_importance_of_subject_matter',
        'explains_subject_matter_of_course',
        'show_respect_for_all_students',
        'overall_teaching_rate',
        'overall_course_rate'
    ]

    @st.cache  # add caching so we load the data only once
    def load_data():
        # Load the yelp data.
        fce_data_url = "./fce-data.csv"
        raw_df = pd.read_csv(fce_data_url)
        df = raw_df
        df.dropna(inplace=True)
        # Convert numeric columns
        for nc in numeric_columns:
            df[nc] = pd.to_numeric(df[nc])

        # Filter data
        df = df[(df['total_students'] > 5) & (df['total_students'] <= 325)] # Remove Outlier
        df = df[df['response_rate'] > 0.4]
        df = df[df['college'] != 'Teaching Assistants']

        # df['overall_rate'] = df[(df['overall_course_rate'] + df['overall_teaching_rate'] + df['show_respect_for_all_students']) / 3]
        return df

    # Dataframes
    # To create a new dataframe for each visualization, use the df as a main. Copy using df.copy() and modify the copy dataframe.
    # Do not modify main df dataframe.
    df = load_data()
    course_df = get_course_df(df)
    course_df["course_name_code_year"] = course_df["year"].astype(str) + ' ' + course_df["semester"] + ' '  + course_df["num"].astype(str) + ' ' + course_df["course_name"]
    course_df["course_name_code"] = course_df["num"].astype(str) + ' ' + course_df["course_name"]
    course_df2 = get_course_df2(course_df)
    # instructor_df = get_instructor_df(df)
    instructor_df_by_year = get_instructor_by_year_df(df)
    instructor_df_all_year = get_instructor_all_year_df(df)
    dept_df = get_dept_df(df)
    dept_df["dept_name_college"] = dept_df["dept"] + ' '  + dept_df["college"]
    dept_df2 = get_dept_df2(dept_df)
    dept_all_year_df = get_dept_all_year_df(df)
    options_map_to_column = options_map_to_columns
    # ------------------------------------------------------- #
    # Main
    # ------------------------------------------------------- #


    curr_state = my_component(0)
    curr_page = 0
    if curr_state:
        curr_page = curr_state["currPage"]
   
    if curr_page == 0:
        # -- Header -- #
        st.header("What Courses to take?")
        st.markdown("Because your time is precious, and the tuition is high, please make the right decision.")
        st.markdown("Learn about CMU courses from the faculty course evaluation data. Explore and compare courses you are interested in before making the decision.")

        st.markdown("""---""")
        # -- Top Trend Section -- #
        trend_cols = st.columns(3)
        top_courses = course_df.sort_values('overall_course_rate', ascending=False).head(5)
        top_instructors = instructor_df_all_year.sort_values('overall_teaching_rate', ascending=False).head(5)
        top_depts = dept_all_year_df.sort_values(['overall_course_rate', 'overall_teaching_rate'], ascending=False).head(5)
        with trend_cols[0]:
            st.subheader("Top Courses")
            for index, row in top_courses.iterrows():
                st.markdown(row['course_name'])
        with trend_cols[1]:
            st.subheader("Top Instructors")
            for index, row in top_instructors.iterrows():
                st.markdown(row['instructor'])
        with trend_cols[2]:
            st.subheader("Top Department")
            for index, row in top_depts.iterrows():
                st.markdown(row['dept'] + ' - ' + row['college'])

        st.markdown("""---""")
        # -- Explore Section -- #
        st.subheader("Explore by yourself")
        st.markdown("Filter the courses and learn how well the coures and the instructors. Selecting the course on the graph to see the workload. Brushing the bottom graph to filter only course with right workload.")

        # -- Filters -- #
        filter_cols = st.columns(3)
        year_filters=[]
        sem_filters=[]
        course_level_filters=[]
        college_filters=[]
        cols = st.columns(3)
        with filter_cols[0]:
            years_options = course_df['year'].unique()
            year_filters = st.multiselect(
                "Select years",
                years_options,
                [2022, 2021]
            )
        with filter_cols[1]:
            course_level_options = course_df['course_level'].unique()
            course_level_filters = st.multiselect(
                "Select course lebel",
                course_level_options,
                ['Graduate', 'Undergraduate']
            )
        with filter_cols[2]:
            semester_options = course_df['semester'].unique()
            sem_filters = st.multiselect(
                "Select semester",
                semester_options,
                ['Spring', 'Fall']
            )
        college_options = course_df['college'].unique()
        college_filters = st.multiselect(
            "Select schools",
            college_options,
            ['School of Computer Science', 'Tepper School of Business', 'Heinz College']
        )
        course_df_filter = course_df
        course_df_filter = course_df_filter[course_df_filter['year'].isin(year_filters)]
        course_df_filter = course_df_filter[course_df_filter['semester'].isin(sem_filters)]
        course_df_filter = course_df_filter[course_df_filter['course_level'].isin(course_level_filters)]
        course_df_filter = course_df_filter[course_df_filter['college'].isin(college_filters)]

        # -- Scatter Plots -- #
        explore_brush = alt.selection_interval()
        selector = alt.selection_single(empty='all', fields=['num'])
        legend_selector = alt.selection_multi(fields=['college'], bind='legend')

        base_scatter = alt.Chart(course_df_filter)
        home_main_scatter = base_scatter.mark_circle(opacity=0.7, size=40).encode(
            alt.Y("overall_teaching_rate:Q", sort="ascending", title="Overall Teaching Rate"),
            alt.X("overall_course_rate:Q", title="Overall Course Rate"),
            color=alt.condition(selector, 'college', alt.value('lightgray')),
            opacity=alt.condition(legend_selector, alt.value(0.7), alt.value(0.05)),
            tooltip=[
                alt.Tooltip("num", title="Course Number"),
                alt.Tooltip("course_name", title="Course Name"),
                alt.Tooltip("hrs_per_week", title="Hrs per Week", format=".2f"),
                alt.Tooltip('year', title="Year")
            ]
        ).properties(
            width=600,
            height=400,
        ).add_selection(
            selector,
            legend_selector
        ).transform_filter(
            explore_brush
        )

        hrs_per_week_scatter = base_scatter.mark_circle(opacity=0.7, size=40).encode(
            alt.X("hrs_per_week:Q", sort="ascending", title="Hrs per Week"),
            color=alt.condition(selector, 'college', alt.value('lightgray')),
            tooltip=["num", "course_name", "instructor", "hrs_per_week", "year"],
            opacity=alt.condition(legend_selector, alt.value(0.7), alt.value(0.05))
        ).properties(
            width=600,
            height=50
        ).add_selection(
            explore_brush,
            legend_selector
        ).transform_filter(
            selector
        )

        st.write(home_main_scatter & hrs_per_week_scatter)
    elif curr_page == 1:
        st.header("Compare Courses")
        #--- 1. COURSE SEARCH dataprep----#

        #Adding concatenation to distinguish same course names
        # course_df["course_name_code_year"] = course_df["year"].astype(str) + ' ' + course_df["semester"] + ' '  + course_df["num"].astype(str) + ' ' + course_df["course_name"]
        # course_df["course_name_code"] = course_df["num"].astype(str) + ' ' + course_df["course_name"]
        #Creating  a list of latest courses for the search
        course_list = course_df.loc[course_df['year']> 2020]['course_name_code_year'].to_list()

        #---- COURSE SEARCH Streamlit component---#
        #options is the name of the array that contains selected options
        course_options = st.multiselect('Select courses for comparison', course_list)
        courseCodeArray = [" ".join(course_string.split(' ')[2:]) for course_string in course_options]
       
        options = st.multiselect(
        'Please Select Features You Want to Compare',
        ['Overall teaching rate','Overall course rate', 'Interest in student learning', 'Clearly explain course requirements', 'Clear learning objectives & goals', 'Demonstrate importance of subject matter','Instructor provides feedback to students to improve','Explains subject matter of course','Show respect for all students'],
        ['Overall teaching rate','Overall course rate'])
 

        # convert options to column names
        options_columns = [options_map_to_column[option] for option in options]
        # print(options_columns)
        # print(course_options)

        course_options_length = len(course_options)

        

        if(course_options_length>0):
            
            # filter_df1 = course_df.groupby(['course_name_code_year', 'instructor'])[options_columns].mean().reset_index()
            # st.write(filter_df1)
            # filter_df = filter_df1.loc[course_df['course_name_code_year'].isin(course_options)]
            # reshaped_filter_df = filter_df.melt(id_vars=['course_name_code_year', 'instructor', 'responses'], var_name = 'Judge Parameter', value_name = 'Rating').sort_values(by='course_name_code_year').reset_index(drop=True)
            
            filter_df1 = course_df2.loc[course_df2['course_name_code_year'].isin(course_options)]
            columns_filter = options_columns + ['course_name_code_year', 'instructor_combined', 'hrs_per_week', 'responses']

            filter_df1 = filter_df1[columns_filter]
            reshaped_filter_df = filter_df1.melt(id_vars=['course_name_code_year', 'instructor_combined', 'hrs_per_week', 'responses'], var_name = 'Judge Parameter', value_name = 'Rating').sort_values(by='course_name_code_year').reset_index(drop=True)
           
            with st.expander("See Detailed Course Info"):
                # cols = st.columns(course_options_length)

                for index, row in filter_df1.iterrows():
                    course_name = row['course_name_code_year']
                    instructor = row['instructor_combined']
                    hrs_per_week = row['hrs_per_week']
                    responses = row['responses']
                    st.text("Name: {} \n Instructor: {} \n Hrs per Week: {:.2f} \n Responses: {:d}".format(course_name, instructor, hrs_per_week, int(responses)))
                    # st.text("Name: "+ course_name + "\n"+ "Instructor: "+ instructor + "\n"+ "Hrs per Week: "+ str(hrs_per_week) + "\n"+ "Responses: "+ str(responses))
                    
           
            st.markdown("""---""")
            # first chart
            st.subheader("Compare courses based on different metrics")
            
            
            selection_legend = alt.selection_multi(fields=['course_name_code_year'], bind='legend')

            compare_course_ratings = alt.Chart(reshaped_filter_df).mark_bar(tooltip=True).transform_calculate(
                y="split(datum.y, '_')"
            ).encode(
                y=alt.Y('course_name_code_year:O', type="nominal", axis=alt.Axis(title=None, labels=False)),
                x=alt.X('Rating:Q',axis=alt.Axis(grid=False)),
                color=alt.Color('course_name_code_year:N',legend=alt.Legend(title="Course Name", labelFontSize=12)),
                opacity=alt.condition(selection_legend, alt.value(1), alt.value(0.2)),
                row=alt.Row('Judge Parameter:N', header=alt.Header(labelAngle=0, labelAlign="left", labelFontSize=8)),
                tooltip = [alt.Tooltip(field = "course_name_code_year", title = "Course Name", type = "nominal"),
                        alt.Tooltip(field = "Rating", title ="Rating", type = "quantitative", format=".2f"),
                        alt.Tooltip(field = "instructor_combined", title ="Instructor", type = "nominal"),
                        alt.Tooltip(field = "responses", title ="Responses", type = "quantitative")
                ],
            ).properties(
                title="Compare Ratings for Selected Courses", 
                width=400,
            ).configure_title(
                anchor='middle',
            ).add_selection(
                selection_legend
            ).configure_legend(labelLimit= 0)


            st.altair_chart(compare_course_ratings)

            st.markdown("""---""")

            # second chart
            st.subheader("Compare courses over time")

            # course_df2 = course_df.groupby(['course_name_code','year']).agg(
            #     course_name=('course_name', 'max'), 
            #     responses=('responses', 'mean'), 
            #     num=('num', 'max'), 
            #     instructor_combined=('instructor', lambda x: ' - '.join(x)), 
            #     overall_course_rate=('overall_course_rate', 'mean'))

            # course_df2 = course_df2.reset_index()
            # st.write(course_df2.head(50))
            filter_df2 = course_df2.loc[course_df2['course_name_code'].isin(courseCodeArray)]
            # st.write(filter_df2)
            selection_legend = alt.selection_multi(fields=['course_name_code'], bind='legend')


            compare_rating_over_years = alt.Chart(filter_df2).mark_line(point=alt.OverlayMarkDef(size=100), tooltip=True).encode(
                x = alt.X("year:N", title="Year"),
                y= alt.Y("overall_course_rate", title="Overall Course Rate"),
                color=alt.Color("course_name_code:N", legend=alt.Legend(title="Course Name", labelFontSize=12)),
                opacity=alt.condition(selection_legend, alt.value(1), alt.value(0.2)),
                # strokeDash="instructor_combined",
                tooltip = [alt.Tooltip(field = "course_name", title = "Course Name", type = "nominal"),
                        alt.Tooltip(field = "year", title = "Year", type = "quantitative"),
                        alt.Tooltip(field = "overall_course_rate", title ="Avg Overall Course Rating", type = "quantitative", format=".2f"),
                        alt.Tooltip(field = "instructor_combined", title ="Instructor", type = "nominal"),
                        alt.Tooltip(field = "responses", title ="Avg Responses", type = "quantitative", format=".2f")
                ],
            ).properties(
                title="Compare Course Ratings Over the years", 
                width=750,
                height=500
            ).add_selection(
                selection_legend
            )

            st.altair_chart(compare_rating_over_years)




    elif curr_page == 2:
        st.header("Compare Departments")
        #Creating  a list of department for the search
        # dept_df["dept_name_college"] = dept_df["dept"] + ' '  + dept_df["college"]
        dept_list = set(dept_df['dept_name_college'].to_list())

        #--- DEPARTMENT SEARCH Streamlit component --#
        #options is the name of the array that contains selected options
        options_dept = st.multiselect('Select department for comparison', dept_list)

        options = st.multiselect(
        'Please Select Features You Want to Compare',
        ['Overall teaching rate','Overall course rate', 'Interest in student learning', 'Clearly explain course requirements', 'Clear learning objectives & goals', 'Demonstrate importance of subject matter','Instructor provides feedback to students to improve','Explains subject matter of course','Show respect for all students'],
        ['Overall teaching rate','Overall course rate'])



        # convert options to column names
        options_columns = [options_map_to_column[option] for option in options]
        print(options_dept)

        if(len(options_dept)>0):
            # filter_df1 = dept_df.loc[dept_df['year'] == 2021]
            # filter_df2 = filter_df1.groupby(['dept_name_college'])[options_columns].mean().reset_index()
            # filter_df3 = filter_df2.loc[filter_df2['dept_name_college'].isin(options_dept)]

            filter_df1 = dept_df.loc[dept_df['year'] == 2021]
            filter_df1 = filter_df1.loc[filter_df1['dept_name_college'].isin(options_dept)]

            columns_filter = options_columns + ['dept_name_college', 'total_students', 'hrs_per_week', 'responses']
            filter_df2 = filter_df1[columns_filter].groupby(['dept_name_college']).agg(
                dept_name_college = ('dept_name_college', 'first'),
                total_students=('total_students', 'sum'),
                hrs_per_week = ('hrs_per_week', 'mean'),
                responses=('responses', 'sum'))
            filter_df3 = filter_df1[columns_filter]


            reshaped_filter_df = filter_df3.melt(id_vars=['dept_name_college', 'total_students', 'hrs_per_week', 'responses'], var_name = 'Judge Parameter', value_name = 'Rating').sort_values(by='dept_name_college').reset_index(drop=True)
            selection_legend = alt.selection_multi(fields=['dept_name_college'], bind='legend')

            with st.expander("See Detailed Department Info"):
                # cols = st.columns(course_options_length)

                for index, row in filter_df2.iterrows():
                    course_name = row['dept_name_college']
                    total_students = row['total_students']
                    hrs_per_week = row['hrs_per_week']
                    responses = row['responses']
                    st.text("Name: {} \n Total Students: {:d} \n Avg Hrs per Week: {:.2f} \n Total Responses: {:d}".format(course_name, int(total_students), hrs_per_week, int(responses)))
                    # st.text("Name: "+ course_name + "\n"+ "Instructor: "+ instructor + "\n"+ "Hrs per Week: "+ str(hrs_per_week) + "\n"+ "Responses: "+ str(responses))


            st.markdown("""---""")

            st.subheader("Compare departments based on different metrics")

            compare_dept_ratings = alt.Chart(reshaped_filter_df).mark_bar(tooltip=True).transform_calculate(
                y="split(datum.y, '_')"
            ).encode(
                y=alt.Y('dept_name_college:O', type="nominal", axis=alt.Axis(title=None, labels=False)),
                x=alt.X('Rating:Q',axis=alt.Axis(grid=False)),
                color=alt.Color('dept_name_college:N',legend=alt.Legend(title="Department Name", labelFontSize=12)),
                opacity=alt.condition(selection_legend, alt.value(1), alt.value(0.2)),
                row=alt.Row('Judge Parameter:N', header=alt.Header(labelAngle=0, labelAlign="left", labelFontSize=8)),
            ).properties(
                title="Compare Ratings for Selected Departments", 
                width=400,
            ).configure_title(
                anchor='middle',
            ).add_selection(
                selection_legend
            ).configure_legend(labelLimit= 0)


            st.altair_chart(compare_dept_ratings)

            st.markdown("""---""")

            # second chart
            st.subheader("Compare departments over time")

            columns_filter = options_columns + ['dept_name_college', 'total_students', 'hrs_per_week', 'responses', 'year']
            filter_dept_df = dept_df2.loc[dept_df2['dept_name_college'].isin(options_dept)]
            formatted_filter_dept_df = filter_dept_df[columns_filter]
            selection_legend = alt.selection_multi(fields=['dept_name_college'], bind='legend')

            compare_dept_rating_over_years = alt.Chart(formatted_filter_dept_df).mark_line(point=alt.OverlayMarkDef(size=100), tooltip=True).encode(
                x = alt.X("year:N", title="Year"),
                y= alt.Y("overall_course_rate", title="Overall Course Rate"),
                color=alt.Color("dept_name_college:N", legend=alt.Legend(title="Department Name", labelFontSize=12)),
                opacity=alt.condition(selection_legend, alt.value(1), alt.value(0.2)),
                tooltip = [
                    alt.Tooltip(field = "dept_name_college", title = "Department Name", type = "nominal"),
                    alt.Tooltip(field = "year", title = "Year", type = "quantitative"),
                    alt.Tooltip(field = "overall_course_rate", title ="Avg Overall Course Rating", type = "quantitative", format=".2f")
                ]
            ).properties(
                title="Compare Course Ratings Over the years", 
                width=750,
                height=500
            ).add_selection(
                selection_legend
            )

            st.altair_chart(compare_dept_rating_over_years)


    elif curr_page == 3:
        st.header("Compare Instructors")
        #--- 3. INSTRUCTOR SEARCH dataprep----#

        #Creating  a list of instructors for the search
        instructor_list = instructor_df_all_year['instructor'].to_list()

        #---INSTRUCTOR SEARCH Streamlit component--#
        #options is the name of the array that contains selected options
        options_instructor = st.multiselect('Select instructors for comparison', instructor_list)

        options = st.multiselect(
        'Please Select Features You Want to Compare',
        ['Overall teaching rate','Overall course rate', 'Interest in student learning', 'Clearly explain course requirements', 'Clear learning objectives & goals', 'Demonstrate importance of subject matter','Instructor provides feedback to students to improve','Explains subject matter of course','Show respect for all students'],
        ['Overall teaching rate','Overall course rate'])
 

        # convert options to column names
        options_columns = [options_map_to_column[option] for option in options]

        if(len(options_instructor)>0):
           
            st.markdown("""---""")
            st.subheader("Compare instructors based on different metrics")

            # first chart
            filter_df1 = instructor_df_all_year.groupby(['instructor'])[options_columns].mean().reset_index()
            filter_df = filter_df1.loc[instructor_df_all_year['instructor'].isin(options_instructor)]

            reshaped_filter_df = filter_df.melt(id_vars=['instructor'], var_name = 'Judge Parameter', value_name = 'Rating').sort_values(by='instructor').reset_index(drop=True)
            selection_legend = alt.selection_multi(fields=['instructor'], bind='legend')

            compare_inst_ratings = alt.Chart(reshaped_filter_df).mark_bar(tooltip=True).transform_calculate(
                y="split(datum.y, '_')"
            ).encode(
                y=alt.Y('instructor:O', type="nominal", axis=alt.Axis(title=None, labels=False)),
                x=alt.X('Rating:Q',axis=alt.Axis(grid=False)),
                color=alt.Color('instructor:N',legend=alt.Legend(title="Instructor ", labelFontSize=12)),
                opacity=alt.condition(selection_legend, alt.value(1), alt.value(0.2)),
                row=alt.Row('Judge Parameter:N', header=alt.Header(labelAngle=0, labelAlign="left", labelFontSize=8)),
                tooltip = [
                    alt.Tooltip(field = "instructor", title = "Instructor Name", type = "nominal"),
                    alt.Tooltip(field = "Rating", title ="Avg Rating", type = "quantitative", format=".2f")
                ]
            ).properties(
                title="Compare Ratings for Selected Instructors", 
                width=400,
            ).configure_title(
                anchor='middle',
            ).add_selection(
                selection_legend
            ).configure_legend(labelLimit= 0)


            st.altair_chart(compare_inst_ratings)

            st.markdown("""---""")

            st.subheader("Compare Instructors over time")


            filter_df2 = instructor_df_by_year.loc[instructor_df_by_year['instructor'].isin(options_instructor)]

            selection_legend = alt.selection_multi(fields=['instructor'], bind='legend')

            compare_inst_rating_over_years = alt.Chart(filter_df2).mark_line(point=alt.OverlayMarkDef(size=100), tooltip=True).encode(
                x = alt.X("year:N", title="Year"),
                y= alt.Y("overall_teaching_rate", title="Overall Teaching Rate"),
                color=alt.Color("instructor:N", legend=alt.Legend(title="Instructor Name", labelFontSize=12)),
                opacity=alt.condition(selection_legend, alt.value(1), alt.value(0.2)),
                tooltip = [
                    alt.Tooltip(field = "instructor", title = "Instructor Name", type = "nominal"),
                    alt.Tooltip(field = "year", title = "Year", type = "quantitative"),
                    alt.Tooltip(field = "overall_teaching_rate", title ="Avg Overall Teaching Rating", type = "quantitative", format=".2f")
                ]
            ).properties(
                title="Compare Instructor Ratings Over the years",
                width=750,
                height=500
            ).add_selection(
                selection_legend
            )

            st.altair_chart(compare_inst_rating_over_years)
            

    # st.write(currPage)
    # st.markdown("You've clicked %s times!" % int(num_clicks))

    # st.markdown("---")
    # st.subheader("Component with variable args")

    # Create a second instance of our component whose `name` arg will vary
    # based on a text_input widget.
    #
    # We use the special "key" argument to assign a fixed identity to this
    # component instance. By default, when a component's arguments change,
    # it is considered a new instance and will be re-mounted on the frontend
    # and lose its current state. In this case, we want to vary the component's
    # "name" argument without having it get recreated.
    # name_input = st.text_input("Enter a name", value="Streamlit")
    # num_clicks = my_component(name_input, key="foo")
    # st.markdown("You've clicked %s times!" % int(num_clicks))
