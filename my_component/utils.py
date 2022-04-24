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
    dept_df = df.groupby(['dept'])
    dept_df = dept_df.agg(
        college=('college', 'max'),
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
    dept_df = dept_df.reset_index()
    return dept_df