def calculate_area(shape, dimension):
    """
    Calculates the area based on the shape and dimension provided.
    
    Parameters:
    shape (str): The type of shape ("square", "circle", or "triangle")
    dimension (dict): Dictionary containing necessary dimensions

    Returns:
    float: Calculated area
    """
    if shape == "square":
        return dimension['side'] ** 2
    elif shape == "circle":
        from math import pi
        return pi * (dimension['radius'] ** 2)
    elif shape == "triangle":
        return 0.5 * dimension['base'] * dimension['height']
    else:
        raise ValueError("Unsupported shape provided.")

def test_calculate_area():
    """Test cases for the calculate_area function."""
    assert calculate_area("square", {"side": 4}) == 16
    assert round(calculate_area("circle", {"radius": 3}), 2) == 28.27
    assert calculate_area("triangle", {"base": 10, "height": 5}) == 25
    try:
        calculate_area("hexagon", {"side": 2})
    except ValueError as e:
        assert str(e) == "Unsupported shape provided."

if __name__ == "__main__":
    print("Area of square:", calculate_area("square", {"side": 5}))
    print("Area of circle:", calculate_area("circle", {"radius": 2}))
    print("Area of triangle:", calculate_area("triangle", {"base": 6, "height": 4}))




