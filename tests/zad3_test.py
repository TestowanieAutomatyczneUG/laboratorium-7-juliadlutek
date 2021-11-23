import unittest
import src.zad3.zad3 as zad3
import re

invoice = {
  "customer": "BigCo",
  "performances": [
    {
      "playID": "hamlet",
      "audience": 55
    },
    {
      "playID": "as-like",
      "audience": 35
    },
    {
      "playID": "othello",
      "audience": 40
    }
  ]
}
plays = {
  "hamlet": {"name": "Hamlet", "type": "tragedy"},
  "as-like": {"name": "As You Like It", "type": "comedy"},
  "othello": {"name": "Othello", "type": "tragedy"}
}

invoice2 = {
  "customer": "BigCo",
  "performances": [
    {
      "playID": "othello",
      "audience": 40
    }
  ]
}

plays2 = {
  "othello": {"name": "Othello", "type": "other"}
}

invoice3 = {
  "customer": "BigCo"
}

class StatementTest(unittest.TestCase):
    def test_correct_result(self):
        self.assertMultiLineEqual(zad3.statement(invoice, plays), "Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n")
    def test_icorrect_play_type(self):
        with self.assertRaises(ValueError):
            zad3.statement(invoice2, plays2)
    def test_incorrect_data_structure(self):
        with self.assertRaises(KeyError):
            zad3.statement(invoice3, plays2)

