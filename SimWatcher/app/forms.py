from wtforms import Form, StringField, TextAreaField, validators


class SimulationForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    description = TextAreaField('Description', [validators.Length(min=1)])
    topic = StringField('Topic', [validators.Length(min=1, max=20)])


class RunForm(Form):
    parent = StringField('Parent run', [validators.Length(min=1)])
    description = TextAreaField('Description', [validators.Length(min=1)])
    inputs = TextAreaField('Inputs', [validators.Length(min=1)])
    binary = TextAreaField('Binary', [validators.Length(min=1)])
    files = TextAreaField('Other files')


class QueryForm(Form):
    pass
