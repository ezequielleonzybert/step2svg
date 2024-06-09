from build123d import import_step, section, BuildSketch, BuildLine, add, ExportSVG, Plane

def convert(paths):
    for path in paths:
        path_parts = path.split("/")
        filename = path_parts[-1]
        folder = "/".join(path_parts[:-1])
        if is_step(filename):
            model = import_step(path)
            sec = section(model, Plane.XY, clean=False)

            with BuildSketch() as sketch:
                with BuildLine() as lines:
                    for edge in sec.edges():
                        add(edge)
                    add(lines._obj)
                shape = sketch.consolidate_edges()
            
            exporter = ExportSVG()
            exporter.add_shape(shape)
            exporter.write(folder + "/" + filename + ".svg")

def is_step(filename):
    extension = filename.split(".")[-1]
    if extension == "step" or extension =="stp":
        return True
    else:
        return False