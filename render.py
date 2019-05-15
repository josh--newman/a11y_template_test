from jinja2 import Template
import json

def render_report():
  # open the template file
  with open("a11y_template.html", "r") as read_file:
    html = read_file.read()

  # open the json file
  with open("a11y.json", "r") as file_json:
    data = json.load(file_json)

  # create jinja template
  template = Template(html)

  # render template with json data
  rendered_file = template.render(data)

  # write rendered template file
  with open("ally.html", "w") as write_file:
    write_file.write(rendered_file)

render_report()
