# ------------------------------------------------------- #
# Util functions
# ------------------------------------------------------- #


# Convert main df to course_df
def get_course_df(df):
    course_df = df.groupby(['year', 'semester', "num", 'course_name'])
    course_df = course_df.agg(
        college=('college', 'max'),
        dept=('dept', 'max'),
        section=('section', 'max'),
        instructor=('instructor', 'max'),
        course_level=('course_level', 'max'),
        hrs_per_week=('hrs_per_week', 'mean'),
        total_students=('total_students', 'mean'),
        responses=('responses', 'mean'),
        response_rate=('response_rate', 'mean'),
        interest_in_student_learning=('interest_in_student_learning', 'mean'),
        clearly_explain_course_requirements=('clearly_explain_course_requirements', 'mean'),
        clear_learning_objectives_and_goals=('clear_learning_objectives_and_goals', 'mean'),
        instructor_provides_feedback=('instructor_provides_feedback', 'mean'),
        demonstrate_importance_of_subject_matter=('demonstrate_importance_of_subject_matter', 'mean'),
        explains_subject_matter_of_course=('explains_subject_matter_of_course', 'mean'),
        show_respect_for_all_students=('show_respect_for_all_students', 'mean'),
        overall_teaching_rate=('overall_teaching_rate', 'mean'),
        overall_course_rate=('overall_course_rate', 'mean')
    )
    course_df = course_df.reset_index()
    return course_df

def get_course_df2(course_df):
    course_df2 = course_df.groupby(['course_name_code', 'year']).agg(
        course_name_code_year = ('course_name_code_year', 'first'),
        hrs_per_week = ('hrs_per_week', 'mean'),
        course_name=('course_name', 'max'), 
        responses=('responses', 'mean'), 
        num=('num', 'max'), 
        instructor_combined=('instructor', lambda x: ' - '.join(x)), 
        interest_in_student_learning=('interest_in_student_learning', 'mean'),
        clearly_explain_course_requirements=('clearly_explain_course_requirements', 'mean'),
        clear_learning_objectives_and_goals=('clear_learning_objectives_and_goals', 'mean'),
        instructor_provides_feedback=('instructor_provides_feedback', 'mean'),
        demonstrate_importance_of_subject_matter=('demonstrate_importance_of_subject_matter', 'mean'),
        explains_subject_matter_of_course=('explains_subject_matter_of_course', 'mean'),
        show_respect_for_all_students=('show_respect_for_all_students', 'mean'),
        overall_teaching_rate=('overall_teaching_rate', 'mean'),
        overall_course_rate=('overall_course_rate', 'mean'))
    course_df2 = course_df2.reset_index()
    return course_df2

def get_instructor_df(df):
    instructor_df = df.groupby(['instructor'])
    instructor_df = instructor_df.agg(
        college=('college', 'max'),
        dept=('dept', 'max'),
        section=('section', 'max'),
        hrs_per_week=('hrs_per_week', 'mean'),
        total_students=('total_students', 'mean'),
        responses=('responses', 'mean'),
        response_rate=('response_rate', 'mean'),
        interest_in_student_learning=('interest_in_student_learning', 'mean'),
        clearly_explain_course_requirements=('clearly_explain_course_requirements', 'mean'),
        clear_learning_objectives_and_goals=('clear_learning_objectives_and_goals', 'mean'),
        instructor_provides_feedback=('instructor_provides_feedback', 'mean'),
        demonstrate_importance_of_subject_matter=('demonstrate_importance_of_subject_matter', 'mean'),
        explains_subject_matter_of_course=('explains_subject_matter_of_course', 'mean'),
        show_respect_for_all_students=('show_respect_for_all_students', 'mean'),
        overall_teaching_rate=('overall_teaching_rate', 'mean'),
        overall_course_rate=('overall_course_rate', 'mean')
    )
    instructor_df = instructor_df.reset_index()
    return instructor_df

def get_dept_df(df):
    dept_df = df.groupby(['dept', 'year', 'semester'])
    dept_df = dept_df.agg(
        college=('college', 'max'),
        hrs_per_week=('hrs_per_week', 'mean'),
        total_students=('total_students', 'sum'),
        responses=('responses', 'sum'),
        response_rate=('response_rate', 'mean'),
        interest_in_student_learning=('interest_in_student_learning', 'mean'),
        clearly_explain_course_requirements=('clearly_explain_course_requirements', 'mean'),
        clear_learning_objectives_and_goals=('clear_learning_objectives_and_goals', 'mean'),
        instructor_provides_feedback=('instructor_provides_feedback', 'mean'),
        demonstrate_importance_of_subject_matter=('demonstrate_importance_of_subject_matter', 'mean'),
        explains_subject_matter_of_course=('explains_subject_matter_of_course', 'mean'),
        show_respect_for_all_students=('show_respect_for_all_students', 'mean'),
        overall_teaching_rate=('overall_teaching_rate', 'mean'),
        overall_course_rate=('overall_course_rate', 'mean')
    )
    dept_df = dept_df.reset_index()
    return dept_df

def get_dept_df2(dept_df):
    dept_df2 = dept_df.groupby(['dept_name_college', 'year']).agg(
        total_students=('total_students', 'sum'),
        hrs_per_week = ('hrs_per_week', 'mean'),
        responses=('responses', 'sum'), 
        interest_in_student_learning=('interest_in_student_learning', 'mean'),
        clearly_explain_course_requirements=('clearly_explain_course_requirements', 'mean'),
        clear_learning_objectives_and_goals=('clear_learning_objectives_and_goals', 'mean'),
        instructor_provides_feedback=('instructor_provides_feedback', 'mean'),
        demonstrate_importance_of_subject_matter=('demonstrate_importance_of_subject_matter', 'mean'),
        explains_subject_matter_of_course=('explains_subject_matter_of_course', 'mean'),
        show_respect_for_all_students=('show_respect_for_all_students', 'mean'),
        overall_teaching_rate=('overall_teaching_rate', 'mean'),
        overall_course_rate=('overall_course_rate', 'mean'))
    dept_df2 = dept_df2.reset_index()
    return dept_df2

options_map_to_columns = {
    'Interest in student learning': 'interest_in_student_learning',
    'Clearly explain course requirements': 'clearly_explain_course_requirements',
    'Clear learning objectives & goals': 'clear_learning_objectives_and_goals',
    'Demonstrate importance of subject matter': 'demonstrate_importance_of_subject_matter',
    'Instructor provides feedback to students to improve': 'instructor_provides_feedback',
    'Explains subject matter of course': 'explains_subject_matter_of_course',
    'Show respect for all students': 'show_respect_for_all_students',
    'Overall teaching rate': 'overall_teaching_rate',
    'Overall course rate': 'overall_course_rate'
}