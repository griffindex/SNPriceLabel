import labels
from reportlab.graphics import shapes

# Create an 4x6 portrait (102mm x 152mm) sheets with 4 columns and 9 rows of
# labels. Each label is 13mm x 19mm with a 2mm rounded corner. The margins are
# automatically calculated.
specs = labels.Specification(102, 152, 4, 9, 19, 13, corner_radius=2)

# Create a function to draw each label. This will be given the ReportLab drawing
# object to draw on, the dimensions (NB. these will be in points, the unit
# ReportLab uses) of the label, and the object to render.
def draw_label(label, width, height, obj):
    # Just convert the object to a string and print this at the bottom left of
    # the label.
    label.add(shapes.String(1, 1, str(obj), fontName="Helvetica", fontSize=10))

# Create the sheet.
sheet = labels.Sheet(specs, draw_label, border=True)


# Add a couple of labels.

sheet.add_label("TEST", count=4)

# We can also add each item from an iterable.
#sheet.add_labels(range("test"))

# Note that any oversize label is automatically trimmed to prevent it messing up
# other labels.
#sheet.add_label("Oversized label here")

# Save the file and we are done.
sheet.save('basic.pdf')
print("{0:d} label(s) output on {1:d} page(s).".format(sheet.label_count, sheet.page_count))
