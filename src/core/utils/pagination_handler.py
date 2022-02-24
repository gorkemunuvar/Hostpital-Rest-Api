def get_start_and_end(page):
    """Returns start and end row values for pagination.
       Every page returns 10 rows."""
    if page < 1:
       page = 1

    start = (page - 1)  * 10 - 1
    end = page * 10 - 1
    
    return start, end
