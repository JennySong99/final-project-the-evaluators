import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
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
if not _RELEASE:
    import streamlit as st
    import pandas as pd
    import altair as alt
    import numpy as np
    from utils import get_course_df
    from utils import get_instructor_df
    from utils import get_dept_df

    # st.set_page_config(layout="wide")

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
    instructor_df = get_instructor_df(df)
    dept_df = get_dept_df(df)

    # ------------------------------------------------------- #
    # Main
    # ------------------------------------------------------- #

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    curr_state = my_component(0)
    curr_page = 0
    if curr_state:
        curr_page = curr_state["currPage"]
    # st.write(curr_page)
    # if(curr_state and "currPage" in curr_state):
    #     curr_page = curr_state["currPage"]
    if curr_page == 0:
        # -- Header -- #
        st.header("What Courses to take?")
        st.markdown("Because your time is precious, and the tuition is high, please make the right decision.")
        st.markdown("Learn about CMU courses from the faculty course evaluation data. Explore and compare courses you are interested in before making the decision.")

        st.markdown("""---""")
        # -- Top Trend Section -- #
        trend_cols = st.columns(3)
        top_courses = course_df.sort_values('overall_course_rate', ascending=False).head(5)
        top_instructors = instructor_df.sort_values('overall_teaching_rate', ascending=False).head(5)
        top_depts = instructor_df.sort_values(['overall_course_rate', 'overall_teaching_rate'], ascending=False).head(5)
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
                alt.Tooltip("hrs_per_week", title="Hrs per Week"),
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
    elif curr_page == 2:
        st.header("Compare Departments")
    elif curr_page == 3:
        st.header("Compare Instructors")
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


# import altair as alt
# from vega_datasets import data

# source = data.unemployment_across_industries.url

# selection = alt.selection_multi(fields=['series'], bind='legend')

# alt.Chart(source).mark_area().encode(
#     alt.X('yearmonth(date):T', axis=alt.Axis(domain=False, format='%Y', tickSize=0)),
#     alt.Y('sum(count):Q', stack='center', axis=None),
#     alt.Color('series:N', scale=alt.Scale(scheme='category20b')),
#     opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
# ).add_selection(
#     selection
# )