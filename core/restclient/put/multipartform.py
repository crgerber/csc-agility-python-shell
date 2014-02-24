'''
Created on Dec 13, 2012

@author: dawood
'''
import itertools
import mimetools
import mimetypes
from cStringIO import StringIO
import urllib2
from fileinput import filename
CONTENT_TYPE_MULTIPART_FORM_DATA = 'multipart/form-data'
CONTENT_TYPE_MULTIPART_MIXED = 'multipart/mixed'

class MultiPartForm(object):
    """Accumulate the data to be used when posting a form."""

    
    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = mimetools.choose_boundary()
        return
    
    def get_content_type(self):
        return '%s; boundary=%s' % (CONTENT_TYPE_MULTIPART_FORM_DATA if not self.files else CONTENT_TYPE_MULTIPART_MIXED, self.boundary)

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, value))
        return

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        """Add a file to be uploaded."""
        body = fileHandle.read()
        if mimetype is None:
            mimetype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        self.files.append((fieldname, filename, mimetype, body))
        return
    
    def add_archive(self, archive):
        parts = archive.getFormParts()#handling the multi-part envelop of the attachment upload
        [self.add_file(part.attachmentName, part.fileName, part.getFileHandle(), part.mimetype) for part in parts]
    
    def __str__(self):
        """Return a string representing the form data, including attached files."""
        # Build a list of lists, each containing "lines" of the
        # request.  Each part is separated by a boundary string.
        # Once the list is built, return a string where each
        # line is separated by '\r\n'.  
        parts = []
        part_boundary = '--' + self.boundary
        
        # Add the form fields
        parts.extend(
            [ part_boundary,
              'Content-Disposition: form-data; name="%s"' % name,
              '',
              value,
            ]
            for name, value in self.form_fields
            )
        
        # Add the files to upload, first the xml envelop then the attachment file
#        part_boundary,
#              'Content-Disposition: form-data; name="%s"; filename="%s"' %('attachment', 'envelop.xml'),
#              'Content-Type: %s' % 'application/xml',
#              '',
#              '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
#<Attachment xmlns="http://servicemesh.com/agility/api">
#    <name>%s</name>
#</Attachment>''' % field_name,
        
        parts.extend(
            [part_boundary,
              'Content-Disposition: form-data; name="%s"; filename="%s"' %(field_name, filename),
              'Content-Type: %s' % content_type,
              '',
              body,
            ]
            for field_name, filename, content_type, body in self.files
            )
        
        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        return '\r\n'.join(flattened)

if __name__ == '__main__':
    # Create the form with simple fields
    form = MultiPartForm()
    form.add_field('firstname', 'Doug')
    form.add_field('lastname', 'Hellmann')
    
    # Add a fake file
    form.add_file('biography', 'bio.txt', 
                  fileHandle=StringIO('Python developer and blogger.'))

    # Build the request
    request = urllib2.Request('http://localhost:8080/')
    request.add_header('User-agent', 'PyMOTW (http://www.doughellmann.com/PyMOTW/)')
    body = str(form)
    request.add_header('Content-type', form.get_content_type())
    request.add_header('Content-length', len(body))
    request.add_data(body)

    print
    print 'OUTGOING DATA:'
    print request.get_data()

    print
    print 'SERVER RESPONSE:'
    print urllib2.urlopen(request).read()