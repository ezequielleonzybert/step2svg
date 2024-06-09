from build123d import import_step, section, BuildSketch, BuildLine, add, ExportSVG, Plane

def step2svg(files):

    for file in files:
        filename = file.split("/")[-1]
        if is_step(filename):
            model = import_step(file)
            sec = section(model, Plane.XY, clean=False)

            with BuildSketch() as sketch:
                with BuildLine() as lines:
                    for edge in sec.edges():
                        add(edge)
                    add(lines._obj)
                shape = sketch.consolidate_edges()
            
            exporter = ExportSVG()
            exporter.add_shape(shape)
            exporter.write(filename + ".svg")

def is_step(filename):
    extension = filename.split(".")[-1]
    if extension == "step" or extension =="stp":
        return True
    else:
        return False