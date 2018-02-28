"""Upload a CSV file or Plaso file to Timesketch."""

from __future__ import unicode_literals

_short_description = 'Uploads a .plaso file to Timesketch.'

contents = {
    'name': 'timesketch_upload',
    'short_description': _short_description,
    'collectors': [{
        'name': 'FilesystemCollector',
        'args': {
            'paths': '@file',
            'verbose': True,
        },
    }],
    'processors': [],
    'exporters': [{
        'name': 'TimesketchExporter',
        'args': {
            'ts_endpoint': '@ts_endpoint',
            'ts_username': '@ts_username',
            'ts_password': '@ts_password',
            'incident_id': '@incident_id',
            'sketch_id': '@sketch_id',
            'verbose': True,
        }
    }],
}

args = [
    ('file', 'Path to CSV file or Plaso storage file', None),
    ('--sketch_id', 'Sketch to which the timeline should be added', None),
    ('--incident_id', 'Incident ID (used for Timesketch description)', None)
]
