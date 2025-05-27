import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    ## solving for characteristic equation
    a,b = matrix[0]
    c,d = matrix[1]
    trace = a + d
    determinant = (a*d) - (b*c)

    discriminant = math.sqrt(trace**2 - 4*determinant)
    lambda1 = (trace + discriminant) / 2
    lambda2 = (trace - discriminant) / 2
	
    eigenvalues = sorted([lambda1,lambda2], reverse = True)
    return eigenvalues