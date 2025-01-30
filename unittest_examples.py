with self.assertRaises(SomeException):
    do_something()
    
with self.assertRaises(SomeException) as cm:
    do_something()

the_exception = cm.exception
self.assertEqual(the_exception.error_code, 3)


# ----------
self.assertRaisesRegex(ValueError, "invalid literal for.*XYZ'$", int, 'XYZ')
# or
with self.assertRaisesRegex(ValueError, 'literal'):
   int('XYZ')


# ----------
with self.assertWarns(SomeWarning):
    do_something()

with self.assertWarns(SomeWarning) as cm:
    do_something()

self.assertIn('myfile.py', cm.filename)
self.assertEqual(320, cm.lineno)


# ----------
self.assertWarnsRegex(DeprecationWarning,
                      r'legacy_function\(\) is deprecated',
                      legacy_function, 'XYZ')
# or
with self.assertWarnsRegex(RuntimeWarning, 'unsafe frobnicating'):
    frobnicate('/etc/passwd')


# ----------
with self.assertLogs('foo', level='INFO') as cm:
   logging.getLogger('foo').info('first message')
   logging.getLogger('foo.bar').error('second message')
self.assertEqual(cm.output, ['INFO:foo:first message',
                             'ERROR:foo.bar:second message'])


# ----------
self.assertGreaterEqual(3, 4)

