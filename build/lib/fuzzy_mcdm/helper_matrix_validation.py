from .matrixvalidation.core import Matrix_check 



def matrix_validate(criteria_names, alternative_names, matrix_per_criteria, criteria_comparison):
    # Instantiate Matrix_check object
    matrix_checker = Matrix_check(criteria_names, alternative_names, matrix_per_criteria, criteria_comparison)

    # Call methods of Matrix_check object
    try:
        matrix_checker.check_dimentions_and_dtype()
    except ValueError as e:
        print(f"Error: {e}")
    # return consistency.const(a)

