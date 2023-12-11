from dataflows import Flow, load, dump_to_path, dump_to_zip, printer, add_metadata
from dataflows import sort_rows, filter_rows, find_replace, delete_fields, set_type, validate, unpivot




def GDP_csv():
    flow = Flow(
        # Load inputs
        load('GDP.csv', format='csv', ),
        # Process them (if necessary)
        # Save the results
        add_metadata(name='GDP_csv', title='''GDP.csv'''),
        printer(),
        dump_to_path('GDP_csv'),
    )
    flow.process()


if __name__ == '__main__':
    GDP_csv()