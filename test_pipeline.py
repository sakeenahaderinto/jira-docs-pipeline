import copy
import contextlib
import io
import unittest
from pathlib import Path
from pipeline import load_documents, page_flags, print_inventory

class LineageTests(unittest.TestCase):
    def test_export_diagnostics_and_preservation(self):
        docs = load_documents(Path('exports/jira-help-2025-03-07'))
        original = copy.deepcopy(docs)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            print_inventory(docs)
        text = output.getvalue()
        self.assertEqual(docs, original)
        self.assertEqual(text.count('FLAG url shared by pages:'), 2)
        self.assertEqual(text.count('FLAG headings duplicate section headings:'), 1)
        self.assertIn('title gaps: 0\nurl gaps: 2\nlast_updated gaps: 7\nheadings gaps: 40', text)

    def test_duplicate_checks_for_lists_and_encoded_lists(self):
        for headings in (['Repeated', 'Repeated'], '["Repeated", "Repeated"]'):
            flags = page_flags({'headings': headings})
            self.assertTrue(any('duplicate section' in reason for _, reason in flags))
        for headings in ('invalid json', '[{}, null]', ['Unique']):
            self.assertFalse(any('duplicate section' in reason for _, reason in page_flags({'headings': headings})))

    def test_body_metadata_disagreements(self):
        page = {
            'title': 'Record title', 'url': 'https://example.com/record',
            'last_updated': '2025-02-11',
            'body_markdown': '---\ntitle: Body title\nsource_url: https://example.com/body\nlast_updated: 2025-01-30\n---\n# Body title',
        }
        flags = page_flags(page)
        mismatches = [(field, reason) for field, reason in flags if 'disagrees with' in reason]
        self.assertEqual([field for field, _ in mismatches], ['title', 'url', 'last_updated', 'title'])
        self.assertTrue(any('2025-02-11' in reason and '2025-01-30' in reason for _, reason in mismatches))
        page.update(title='Body title', url='https://example.com/body', last_updated='2025-01-30')
        self.assertFalse(any('disagrees with' in reason for _, reason in page_flags(page)))
        for body in (None, '', '---\ntitle: unfinished', '# Body title'):
            page['body_markdown'] = body
            self.assertFalse(any('disagrees with' in reason for _, reason in page_flags(page)))

    def test_title_validation(self):
        for page in ({}, {'title': None}, {'title': ' '}, {'title': 42}):
            self.assertTrue(any(field == 'title' for field, _ in page_flags(page)))
        self.assertFalse(any(field == 'title' for field, _ in page_flags({'title': 'Valid'})))

if __name__ == '__main__':
    unittest.main()
