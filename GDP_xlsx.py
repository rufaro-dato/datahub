from dataflows import Flow, load, dump_to_path, dump_to_zip, printer, add_metadata
from dataflows import sort_rows, filter_rows, find_replace, delete_fields, set_type, validate, unpivot




def GDP_xlsx():
    flow = Flow(
        # Load inputs
        load('GDP.xlsx', format='xlsx', ),
        # Process them (if necessary)
        # Save the results
        add_metadata(name='GDP_xlsx', title='''GDP.xlsx'''),
        printer(),
        dump_to_path('GDP_xlsx'),
    )
    flow.process()


if __name__ == '__main__':
    GDP_xlsx()