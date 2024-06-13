def embed_to_html_table(data):
    """
    Converts an embedded string representation of data into an HTML table.

    Args:
        data: String containing data in a tabular format.

    Returns:
        String containing the HTML table representation of the data.
    """

    # Split the data into rows
    rows = data.strip().split("\n")  # Remove leading/trailing whitespace and split by newline

    # Split the first row (headers)
    headers = rows[0].split("\t") if "\t" in rows[0] else rows[0].split(",")
    # Use tab or comma as delimiter, whichever is present

    # Create the HTML table structure
    html_table = "<table>"
    html_table += "<tr>" + "<th>" + "</th>".join(headers) + "</tr>"  # Create table header row

    # Add data rows
    for row in rows[1:]:
        cells = row.split("\t") if "\t" in row else row.split(",")
        html_table += "<tr>" + "<td>" + "</td>".join(cells) + "</tr>"

    html_table += "</table>"
    return html_table

# Example usage
data = """Column1  Column2  Column3
-------  --------  --------
Data 1   Data A    Data X
Data 2   Data B    Data Y
Data 3   Data C    Data Z
"""

html_table = embed_to_html_table(data)
print(html_table)
