import matplotlib.font_manager as fm
import random
from openpyxl.styles import Font

# Get the list of font names
font_names = [f.name for f in fm.fontManager.ttflist]

def get_random_font():
    # font_list = ["Calibri", "Arial", ""]
    # font_names
    ft = Font(name=random.choice(font_names),
         size=random.choice(list(range(5, 15))),
         bold = random.choice([False, True, False]),
         italic = random.choice([False, True]),
        #  underline = random.choice(['doubleAccounting', 'single', 'singleAccounting', 'double']),
        #  color = random.choice(['FF000000', ])
         )
    
    return ft

def auto_adjust_column_width(sheet, column:str, buffer:int=2):
    # Iterate over all columns in the sheet

    for cell in sheet[column]:
        max_length = 0
        # Find the maximum length of the text in the column
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        # Adjust the column width
        adjusted_width = max_length + buffer  # Adding a little extra space
        sheet.column_dimensions[column].width = adjusted_width